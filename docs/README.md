# crud-maven
Python - beginner to CRUD maven. Talk initially prepared for CodeMash 2023 pre-compiler session

## Getting started
We are going to use https://repl.it to run all of the practice exercises for this course. Click the link below to launch this repo using the web based IDE.
<hr /><br/>

[![Run on Repl.it](https://repl.it/badge/github/ilyaGotfryd/crud-maven)](https://repl.it/github/ilyaGotfryd/crud-maven)

<hr />

## Python basics [===>](./basics/basics.md)
### Data
Here we will look at all things variables and types.
### Flow control 
Conditionals and loops rule this section. First intro to Python scoping.
### Collections
This is one of Python's native superpowers. Datamunging for the win!
# Functions, modules, and decorators [===>](./funcitons/funcitons.md)
## functions
  How are the structured, playing with arguments, dealing with imports, Python scope strikes again. Let's practice some Python Fu.
## decorators
  What are they, where they come from, what do the look like on the inside.
# Pydantic [===>](./pydantic/pydantic.md)
## Basics, serialization, deserialization
## Custom validation
# Fast API [===>](./fast_api/fast_api.md)
## Getting started
- install FastAPI
- install uvicorn
- **[GET]** hello world
   - access Swagger docs
## Password suggestion endpoints
- **[GET]** pass in ID as part of URL get a quote and author back
- **[POST]** generate pasword {length, special_characters}
- **[POST]** validate password fits rules {password: str, length:int, upper_case:bool, special_chars:bool, lower_case:bool} 