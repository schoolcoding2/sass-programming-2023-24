
# Format strings
we can evaluate inside of strings using f-strings.
To create an f-string, we put an f before the opening quote.


``` python
fave_food = input ( "what's your favourite food")
print (f ''.. {fave_food} sounds good.'')
```




# String Methods

[methods] are functions that we can use on [Objects].

String methods allow us to **modify** and work with strings.

Say for example, we want to make all characters of a string lowercase.

'''python
mr_ubial_yelling= "PLEASE PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower())  # it lowercases the letters


print ()
print = function
() is a string


## `.lower`()

The .lower() method takes a string and converts all UPPERCASE characters to lowercase.

We can use ``.lower()`` to help with [[Errors#Semantic errors|errors]]

## ``.upper()

` 

The .upper() method converts all lowercase characters to uppercase in a string


## `.strip(str)


The `.strip()` method removes characters from the beginning to the end of the string. 

```python
user_feeling = input ("How are you feeling?")

# "good" "Good " "GOOD!" "good." "good?"
if user_feeling.lower().stript("!.,?") == "good":
	print("That's great!")

```

## `.split(str)` --> List

The `.split()` method splits a string into a [[lists]] separating the string based on the characters you give it.


```python
grocery_str = "eggs milk cheese hotwheels"

grocery_list = grocery_list .split("")

```


# list membership takes place

 you use "in" to verify 
