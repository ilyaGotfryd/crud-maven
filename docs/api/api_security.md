# Fast API Security

```bash
pip install python-multipart
```

- **[POST]** generate pasword {length, special_characters}

```python

from fastapi import FastAPI
from api.utilities import generate_secret
from api.service import Service, User

app = FastAPI()

@app.get("/user")
def create_user() -> User:
  service = Service()
  user = User(username = generate_secret(), password = generate_secret(is_password = True))
  service.add_user(user)
  return user

```

- **[POST]** login accepting user as login credentials

we will need `python-multipart` to support parts of FastAPI security framework.

```python

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
  service = Service()
  validation_user = User(username=form_data.username, password=form_data.password)
  if service.validate_password(validation_user):
    return {"access_token": validation_user.username, "token_type": "bearer"}
  else:
    raise HTTPException(status_code=400, detail="Incorrect username or password")
```

## Securing our quotes
Now finally let's secure our quotes endpoint

`api/service.py`

```python
class Service:
  ...
  def user_by_username(self, username: str):
  user = None
  if username in db.keys():
    user = User.parse_raw(db[username])
  return user
```

`api/app.py`

```python
from fastapi import FastAPI, Depends, HTTPException, status

def authorized(token:str = Depends(oauth2_scheme)):
  service = Service()
  user = service.user_by_username(token)
  if user is not None:
    return user
  else:
    raise HTTPException(
              status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid authentication credentials",
              headers={"WWW-Authenticate": "Bearer"},
          )

@app.get("/quotes/{quote_id}")
def get_quote_by_id(quote_id: int, user:str = Depends(authorized)) -> Quote:
  quote_dict = get_quote(quote_id)
  
  return Quote(**quote_dict)
```

[Fast API security basics](https://fastapi.tiangolo.com/tutorial/security/first-steps/)

---

Back [== HOME ==>](../README.md)