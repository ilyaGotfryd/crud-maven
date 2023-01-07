# Fast API Security

we will need `python-multipart` to support parts of FastAPI security framework.
```bash
pip install python-multipart
```

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

[security basics] (https://fastapi.tiangolo.com/tutorial/security/first-steps/)

---

Back [== HOME ==>](../README.md)