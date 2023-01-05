# Fat API Security

- **[POST]** generate pasword {length, special_characters}
```python
from fastapi import FastAPI
import secrets

app = FastAPI()

@app.get("/user")
def create_user() -> User:
  data = {"username":generate_secret(),
          "password": generate_secret(is_password = True)}
  user = User(**data)
  service = Service()
  service.add_user(user)
  return user

@app.post("/login")
def login(validate_user: User):
  service = Service()
  if service.validate_user(validate_user):
    return "shrug"
```
- **[POST]** login accepting user as login credentials

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/login")
def login(validate_user: User):
  service = Service()
  if service.validate_user(validate_user):
    return "shrug"
  else:
    # Return an error if the password is incorrect
    raise HTTPException(status_code=401, detail="Failed to login")
```

**TODO: Secure the quotes endpoint** 

---

Back [== HOME ==>](../README.md)