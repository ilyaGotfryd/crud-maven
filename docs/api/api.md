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

Create `main.py` file in `/api` folder. Add hello world end point.
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
uvicorn api.main:app --reload --host 0.0.0.0
```
The browser window will open on the right and will give you the base URL for your publically available hosted service. Copy that URL and paste it into a new browser window and append `/docs` to it. After letting it reload for a little bit you will see sweager documentation for your newly minted API. Let's explore.

---
## Let's get some funny quotes from a large list
- **[GET]** pass in ID as part of URL get a quote and author back

First let's define the `Quote` class we will be fetching.

```python
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
from api.quotes import get_quote

...

@app.get("/quotes/{quote_id}")
def get_quote_by_id(item_id: int) -> Quote:
  quote_dict = get_quote(item_id)
  return Quote(**quote_dict)
```

Let's fetch some quotes and see how it plays out.

---

Next [== Fast API Security==>](./api_security.md)
