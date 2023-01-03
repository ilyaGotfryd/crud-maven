- tuple
  - unrolling tuple
```python
# tuple
empty_tup = tuple()
print(empty_tup)
one_tup = (123,)
print(one_tup, type(one_tup))
some_tup = (234, False, 'testing', None)
print(some_tup, type(some_tup))
# unrolling tuple
id, is_good, name, stuff = some_tup
print(id, is_good, name, stuff)
```
- list
  - list comprehansion
  - list splicing `test[start:end:step]`
  - conditional list comprehansion /filtering

```python
print('-'*20, 'list')
# list
empty_list = list()
more_empty = []
print(empty_list, more_empty, type(more_empty))
one_list = [234]
print(one_list, type(one_list))
some_list = [345,'testing this guy', False, 234.56, None]
print(some_list, type(some_list))
# list splicing test[first:last:step]
splice_me = [i for i in range(0,20)]
print(splice_me)
print('from third', splice_me[2:])
print('three last ones', splice_me[-3:])
print('first 4 elements', splice_me[:4])
print('all but last 5', splice_me[:-5])
print('every third one', splice_me[::3])
print('reverse list', splice_me[::-1])
# list comprehansion
double_up = [i*2 for i in splice_me]
print(double_up)
# conditional list comprehansion /filtering
odd_values_only = [i for i in splice_me if i%2 != 0]
print("odd ones", odd_values_only)
```
- dictionary
  - dictionary comprehansion
```python
print('='*20, 'dictionary')
# dictionary
other_empty = dict()
empty_dict = {}
print(other_empty, empty_dict, type(empty_dict))
single_val = {'test': 123}
print(single_val)
complex_key = {('test', False): "some odd stuff"}
print(complex_key)
# bad_key = {[1,'blah']: 2345}
sample_dict = {'a':1, 123: 'two', False: 123.456 }
print(sample_dict)
print('Element False', sample_dict[False])
# dictionary comprehansion
chars_n_numbers = {chr(ord('a')+i): i+1 for i in range(0, 26)}
print(chars_n_numbers)
print([t for t in chars_n_numbers.items()])
# z_n_double = {some for some in chars_n_numbers.items()}
z_n_double = {k+'z': v*2 for k,v in chars_n_numbers.items()}
print(z_n_double)
```
- set
  - set math

```python
print('+'*20, 'set')
# set
empty_set = set()
single_set = {'test'}
print(single_set, type(single_set))
some_set = {'vase',1,4,3,2,5,1,7,6,3}
print(some_set, type(some_set))
# set math
first_set = {1,3,5,7,8,9}
second_set = {2,4,6,8,10}
print('or ', first_set | second_set)
print('and ', first_set & second_set)
print( 'xor', first_set ^ second_set)
print('subtract', first_set - second_set)
print('subtract', second_set - first_set)
```