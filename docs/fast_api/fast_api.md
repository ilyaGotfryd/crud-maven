# Fast API

## Getting started
- install FastAPI
```
In repl.it on the left side find "packages" icon. Click it and search for "fastapi". Install fastapi package
```
- install uvicorn

`uvicorn` is a server and not a package so we need to use a different tool to install it. We will use a different package manager also available in this system called `PIP` which is default PyPi package manager tool. Navigate to 
- **[GET]** hello world
   - access Swagger docs
---
## Password suggestion endpoints
- **[GET]** pass in ID as part of URL get a quote and author back
- **[POST]** generate pasword {length, special_characters}
- **[POST]** validate password fits rules {password: str, length:int, upper_case:bool, special_chars:bool, lower_case:bool} 