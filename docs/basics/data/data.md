# Data

## Setup
Comment out first print in `main.py` 
import data.py from basics folder
```python
from basics import data
```

that will import and evaluate entire content of the file

---
Let's look at native anything and everything related with literals, variables and basic typing.

**Python** is a dynamically strongly typed language. Unlike *JavaScript* it DOES NOT support type coersion
- variables
  - int, double, bool
  - look up variable type
  ```python
  test = 123
  print(type(test))
  ```
  - cause a type error by adding bool and int
---
- strings
  - string literal
  - multiline strings
    - multiline code comment comment
  - fstrings
    - define `donkey_lobster`
    - inject `donkey_lobster` into an fstring
---
- date
  - import various utility classes from datetime
  ```python
  from datetime import date, datetime, timedelta
  ```
  - date math
    - now, today, 3 days ago, 7 hours ago, start date minus end date
---

- install mypy
```bash
pip install mypy
```
- typehint example

in data.py init an int variable and assign 

---

Next [== Flow Control ==>](../flow_control/flow_control.md)