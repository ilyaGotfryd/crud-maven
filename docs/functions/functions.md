# Functions, modules, and decorators
## functions
- sturcture and type hints
  - let's refactor and take it through steps

```python
# print Greetings to you <name>
# wrap it in funciton - SCOPE with tab!
# pass in name - type hints
# add default value support
# add params (repeat_count, first_name="Anonymous", last_name="")
# call with only last name
# unroll dictionarry params into it {"first_name": "Blah", "last_name": "Test"}
# return formatted greeting - add return typehint
# print result

def greeting(repeat_count: int, first_name: str = "Anonymous", last_name="") -> str:
  result = []
  for _ in range(0, repeat_count):
    result.append(f"Greetings to {first_name} {last_name}")
  return "\n".join(result)

greeting(2, "Ilya Gotfyrd")
greeting(5)
greeting(3, last_name="DonkeyLobster")
params = {'first_name': 'Interesting', 'last_name': 'Person'}
greet_me = greeting(2, **params)
print(greet_me)

# create function that takes in 2 numbers and returns tuple (sum, diff, multiple)
# unroll the result
from typing import Tuple
def compute( a:int, b:int) -> Tuple[int, int, int]:
  return a+b, a-b, a*b

test = compute(3,7)
print(test)
sum, diff, mult = compute(12,75)
print(sum, diff, mult)
```

---

Next [== Decorators ==>](./decorators.md)