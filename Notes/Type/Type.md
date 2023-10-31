In Python, data can be grouped in categories called Types. 

| Name      | Example    | 
|---           |---                | 
|string of `str` |`hello world!`        | 
|list           | [1,2,3,4,5]      |
|boolean or `bool`| `True` `false`      |
|integer or `int` |`1,-10,1205`        |
|float           | `1.2 -432.21 1.0.  |

NOTE: 1.O and 1 are stored differently in the computer 
CONCLUSION:
 uses: describes the data used in code
 
```python
favourite_food = "bibimbap"
my_age = 17
my_age_float = 17.0
# my_age_float is of type float

```

17 is a different type of data than bibimbap

idea that every-piece of data being stored on the computer
type = groups similar ideas/entities together 

NOT primitive type 

 ## Converting types
There are some **special functions** built in python that helps to convert data from one type to another.

```python
intro_string = "My age is"
my_age = 17

# Recall that we can take one string and add another string to it

"My name is" + "Jim"          # "My name isJim"
"My name is" + "" +"Jim"      # "My name is Jim"

intro_string + my_age         # This is going to break 
```