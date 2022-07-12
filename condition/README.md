# Condition
## Boolean Expression


| operation | description              | 
|-----------|--------------------------|
| ==        | equals                   |
| !=        | different                | 
| \<        | less than                |
| \>        | greater than             |
| \<=       | less than or equal to    |
| \>=       | greater than or equal to |


## Not Operation

### example
```
>>> print(not True)
False

>>> print(not False)
True
```

## if statement

is a programming conditional statement that, if proved true, performs a function or displays information.

```
 if boolean condition:
    print("true")
 elif boolean condition:
    print("next")
 else:
    print("end")
```


### and 
logical operator

```
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
```

### or 
logical operator
```
    if last_number == 0 
        or last_number == 2
        or last_number == 4:
        print("odd number)
        
```

### Nested If
```
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
```

### pass statement
`if` statements cannot be empty, but if you for some reason have an `if` statement with no content, put in the `pass` statement to avoid getting an error.

`pass` keyword means that do not work. or to doing to do it.
```
a = 33
b = 200

if b > a:
  pass
```
