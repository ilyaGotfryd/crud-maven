# Pydantic
## Testing
Let's introduce testing into the mix to help us explore this subject with a better feedback loop.
Let's start with [Testing Basics with Pytest](../testing/pytest_basics.md).
Now that we have created a `test/test_service.py` and `test/__init__.py` in our `test` folder in the root and installed `pytest` we can proceed to building things out.

We will be working ander `fast_api` folder in the root as we will be building a service that we will later use in our CRUD app.

Create `fast_api/service.py` and let's go in there and create our user model.

```python
from pydantic import BaseModel

class User(BaseModel):
  username: str
  password: str
```
Let's mess with the model creation and see what vaslidation we get out of the box.

`test/service.py`
```python
from fast_api.service import User

def test_user_creation():
    user = User(username="fail")
    assert user
```
In `Console` run
```bash
pytest test
```
Let's try fiew other combinations.

## Basics, serialization, deserialization
We created a `User` model from pydantic `BaseModel` and we autmatically got type checking and required validation. Let's run some tests to see what JSON serialization and deserialization looks like.

`test/test_service.py`
```python
def test_user_json():
  user = User(username='short', password='simple')
  assert user.json() == '{"username": "short", "password": "simple"}'
  another_user = User.parse_raw('{"username": "ninja", "password": "secure"}')
  assert another_user == User(username="ninja",password="secure")
```
##Creating User Service
Let's create user service and store that user in replit own key value store for later use

`fast_api/service.py`
```python
from replit import db
from pydantic import BaseModel

class User(BaseModel):
  username: str
  password: str

class Service:
  def add_user(self,user: User):
    """
    params:
        user - user to be stored
    returns: None
    """
    if user.username not in db.keys():
      db[user.username] = user.json()
      
  def validate_password(self,unverified_user:User):
    """
    params:
        unverified_user - user who's password we want to validate
    returns:
        True or False based on user presence and password match
    """
    user = None
    if unverified_user.username in db.keys():
      user = User.parse_raw(db[unverified_user.username])
    return user is not None and user == unverified_user
```
Pydantic created a trivial key value store wrapper that behaves as if it is a dictionarry that we examined earlier. True ORMs will definitely be more complex, however this is all we are loking for here.

Let's introduce some test coverage to make sure that this works.

`test\service.py`
```python
from fast_api import Service, User

def test_add_user_check_pwd():
  service = Service()
  user = User(username="special", password="secret")
  service.add_user(user)
  assert service.validate_password(user)
```
## Custom validation

Let's introduce password validation to make things difficult.

```python
from pydantic import BaseModel, ValidationError, validator
import re
password_matcher = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")

class User(BaseModel):
  username: str
  password: str

  @validator('password')
  def validate_pwd(cls, v):
    if not password_matcher.match(v):
      return ValidationError('Password did not match requirements')
    return v
```

At this point if you run `pytest test` your tests will fail with validation error.

Let's fix them and create validation test.

`test/test_service.py`
```python
import pytest
from pydantic import ValidationError

def test_validation_fail():
    with putest.raises(ValidationError) as err:
        user = User(username="this", password="will fail")
    assert str(err) == 'Password did not match requirements'
```