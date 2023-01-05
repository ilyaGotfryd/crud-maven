# crud-maven
Python - beginner to CRUD maven. Talk initially prepared for CodeMash 2023 pre-compiler session

[==> Github Pages==>](https://ilyagotfryd.github.io/crud-maven/)

## Getting started
We are going to use https://repl.it to run all of the practice exercises for this course. Click the link below to launch this repo using the web based IDE.
<hr /><br/>

[![Run on Repl.it](https://repl.it/badge/github/ilyaGotfryd/crud-maven)](https://repl.it/github/ilyaGotfryd/crud-maven)

<hr />

## Python basics
### Data
- variables
- strings
  - multiline strings
  - fstrings
- date
  - date math
- install mypy
  - typehint example
### Flow control
- if
- loops
  - for range(0, n)
  - "for each"
  - enumerate
- case match (not available in Python 3.8 from repl.it)
### Collections
- tuple
  - unrolling tuple
- list
  - list comprehansion
  - list splicing `test[start:end:step]`
  - conditional list comprehansion /filtering
- dictionary
  - dictionary comprehansion
- set
  - set math
# Functions, modules, and decorators
- functions
  - sturcture and type hints
  - import standard library modules
  - build a password generator function
- decorators
  - review basic AOP conepts
  - import performance decorator
  - apply performance decorator
  - pass in different params into function
  - pass different params into decorator
# Pydantic
## Basics, serialization, deserialization
## Custom validation
# Fast API
## Getting started
- install FastAPI
- install uvicorn
- **[GET]** hello world
   - access Swagger docs
## Password suggestion endpoints
- **[GET]** pass in ID as part of URL get a quote and author back
- **[POST]** generate pasword {length, special_characters}
- **[POST]** validate password fits rules {password: str, length:int, upper_case:bool, special_chars:bool, lower_case:bool} 
