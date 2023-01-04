# Fat API Security

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

---

Back [== HOME ==>](../README.md)