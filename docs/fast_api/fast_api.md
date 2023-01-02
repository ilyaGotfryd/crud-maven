# Fast API
## Intro
![logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
[https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
```
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
```

## Getting started
### install FastAPI

In repl.it on the left side find "packages" icon. Click it and search for "fastapi". Install fastapi package. 

![packages_icon](https://media.githubusercontent.com/media/ilyaGotfryd/crud-maven/main/docs/images/packages_btn.png)

### install uvicorn
`uvicorn` is a server and not a package so we need to use a different tool to install it. We will use a different package manager also available in this system called `PIP` which is default PyPi package manager tool. Navigate to shell icon and click it to open console.

![shell_icon](https://media.githubusercontent.com/media/ilyaGotfryd/crud-maven/main/docs/images/shell_btn.png) 

Enter
```bash
pip install uvicorn
```
---
### Implement first endpoint
- **[GET]** hello world

Create `main.py` file in `/fast_api` folder. Add hello world end point.
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

```

### Launch and access Swagger docs
Start the uvicorn application by pointing to root Python module and app object. Also bind it to external traffic by adding `--host 0.0.0.0` to the command and set `--reload` flag to pick up updates as we will make them.
```bash
uvicorn fast_api.main:app --reload --host 0.0.0.0
```
The browser window will open on the right and will give you the base URL for your publically available hosted service. Copy that URL and paste it into a new browser window and append `/docs` to it. After letting it reload for a little bit you will see sweager documentation for your newly minted API. Let's explore.

---
## Let's get some funny quotes from a large list
- **[GET]** pass in ID as part of URL get a quote and author back

First let's define the `Quote` class we will be fetching.

```Python
from typing import Optional
from pydantic import BaseModel

class Quote(BaseModel):
  id: int
  quote: str
  speaker: Optional[str]
  actor: Optional[str]
  piece: Optional[str]

```

Then get quote by id that we will pass in URL as a path parameter

- **[GET]** get quote by ID
```python
from fast_api.quotes import get_quote

...

@app.get("/quotes/{quote_id}")
def get_quote_by_id(item_id: int) -> Quote:
  quote_dict = get_quote(item_id)
  return Quote(**quote_dict)
```

Let's fetch some quotes and see how it plays out.

## 
- **[POST]** generate pasword {length, special_characters}
```python
from fastapi import FastAPI
import secrets

app = FastAPI()

@app.post("/generate-credentials")
async def generate_credentials():
    # Generate a random username and password
    username = secrets.token_urlsafe(16)
    password = secrets.token_urlsafe(16)

    # Store the username and password in the Repl.it key-value data store
    data = {
        "username": username,
        "password": password
    }
    url = "https://repl.it/data/put/{username}/{key}"
    requests.put(url, json=data)

    # Return the username and password to the client
    return {"username": username, "password": password}
```
- **[POST]** validate password fits rules {password: str, length:int, upper_case:bool, special_chars:bool, lower_case:bool} 

```python
from fastapi import FastAPI
from fastapi_security import OAuth2PasswordBearer

app = FastAPI()

# Create an OAuth2PasswordBearer security scheme
security = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/verify-credentials")
async def verify_credentials(username: str, password: str):
    # Retrieve the username and password from the Repl.it key-value data store
    url = "https://repl.it/data/get/{username}/{key}"
    response = requests.get(url)
    data = response.json()

    # Verify the password
    if data["password"] == password:
        # Generate and return an access token
        token = security.create_access_token(data={"sub": username})
        return {"access_token": token}
    else:
        # Return an error if the password is incorrect
        raise HTTPException(status_code=401, detail="Incorrect password")
```

**TODO: Secure the quotes endpoint** 