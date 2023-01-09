- if
- loops
  - for range(0, n)
  - "for each"
  - enumerate

```python
# if
start = 12
end = 24
i = 21
if i>start and i<end:
  print(f"{i} is in range ({start}, {end})")

if i not in [13,15,17,19,25]:
  print(f"{i} is not in the list")
print ('-'*20,' loops')
  # loop
## for range(0, n)
for z in range(17,24):
  print(z)

print('*'*10)
## "for each"
for v in [32,25,'test', False, 'certain']:
  print(v)
## enumerate
for index, item in enumerate(['wiskey','tango','foxtrot','FTW!', 42]):
  print(f"{index}) {item}")
```

---

Next [== Collections ==>](../collections/collections.md)