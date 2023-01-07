# Fast API Security

```bash
pip install python-multipart
```

- **[POST]** generate pasword {length, special_characters}

```python

from fastapi import FastAPI
from fast_api.utilities import generate_secret
from fast_api.service import Service, User

app = FastAPI()

@app.get("/user")
def create_user() -> User:
  data = {"username":generate_secret(),
          "password": generate_secret(is_password = True)}
  user = User(**data)
  service = Service()
  service.add_user(user)
  return user

```

- **[POST]** login accepting user as login credentials

we will need `python-multipart` to support parts of FastAPI security framework.

```python

from fastapi import FastAPI

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

```python

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
  print("  ~~~ get_quote_by_id", quote_id, user)
  quote_dict = get_quote(quote_id)
  
  return Quote(**quote_dict)
```

[Fast API security basics](https://fastapi.tiangolo.com/tutorial/security/first-steps/)

---

Back [== HOME ==>](../README.md)