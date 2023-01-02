# Functions, modules, and decorators
## functions
- sturcture and type hints
- import standard library modules
- build a password generator function

```python
from random import shuffle, choice

legal_chars_lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
legal_chars_upper = [c.upper() for c in legal_chars_lower]
legal_nums = [chr(i) for i in range(ord('0'), ord('9')+1)]
special_chars = [c for c in "!@#$%^&*()"]

def generate_credentials(pwd_length = 16, username_length = 12):
  pwd = [choice(legal_chars_lower) for _ in range(0, pwd_length//3)]
  pwd += [choice(legal_chars_upper) for _ in range(0, pwd_length//3)]
  pwd += [choice(legal_nums) for _ in range(0, pwd_length//3)]
  pwd += [choice(special_chars) for _ in range(0, pwd_length - len(pwd))]
  shuffle(pwd)
  username = [choice(legal_chars_lower) for _ in range(0, username_length//2)]
  username += [choice(legal_chars_upper) for _ in range(0, username_length - len(username))]
  shuffle(username)
  return "".join(username), "".join(pwd)
# import logging decorator
# decorate the password function
# run and see the output

username, password = generate_credentials()
print(username)
print(len(username))
print(password)
print(len(password))
```

## decorators
- review basic AOP conepts
- import performance decorator
- apply performance decorator
- pass in different params into function
- pass different params into decorator