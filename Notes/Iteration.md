---
tags:
  - notes
  - slss
  - y2023
  - programming-level-1-2
---
# Iteration

![Loop from Giphy](https://media1.giphy.com/media/6HsjDOBPwY1eIS6kE0/giphy.gif?cid=ecf05e47u4wu0hvl9m1juhmryx7t9tw7httc7qnwe9k8shyg&ep=v1_gifs_search&rid=giphy.gif&ct=g)

We can repeat our instructions using *iteration* or *loops*.

iteration = repeat

More detailed information can be found [here](https://runestone.academy/ns/books/published/thinkcspy/Strings/TraversalandtheforLoopByItem.html). 

# Iterating over a [[List]]

Say, for example, we want to repeat instructions for all items inside of a list. Python has a way that we can do this.

```python
for <item> in <list>:
	<code block>
```

We can use the rules above to iterate over a list, that is, repeat the code block for every `item` in the list.

Think of it this way. We have a list of groceries below. As you can see, Mr. Ubial has his priorities straight.

```python
groceries = ["hot wheels", "ice cream", "video games"]
```

What if you wanted to print out a formatted version of the list, something useful like putting a bullet in front of the item and putting everything on a new line.

We could do something like this:

```python
for item in groceries:
	print(f"* {item}")
	print("---")
```

Which would output this:

```console
* hotwheels
---
* ice cream
---
* video games
---
```

If we imagine that we're looping through every item in the list, the `<item>` name represents that individual item.
## Search - A Practical Example

We can implement a basic type of search algorithm using loops, one is called [linear search](https://en.wikipedia.org/wiki/Linear_search).

It goes something like this:

```pseudocodeish
for <item> in <list>:
	if <item> == <item you want to find>:
		<do something with the item>
```

Here's a practical example. Let's say that we're looking to see if Jasmine Soto is in the list. We can do this:

```python
names = ['Elizabeth Singleton', 'Raymond Mitchell', 'Steven Murphy', 'Daniel Terry', 'Glenn Fisher', 'Jasmine Soto', 'Deborah Hicks', 'Beverly Ryan', 'Jason Smith', 'Jason Washington']

for name in names:
	if name == "Jasmine Soto":
		print("We found her!")
		break
else: # If we reach the end of the list
	print("we didn't find them.")

```

# Iterating *n* Number of Times
we can iterate/loop for any number of times.
In python, we do it in a *strange* way. 
```python
for <name> in range(<some positive number>):
	<code block>
	
```
e.g.
```python

# Print out Mr.Ubial is cool. ten times
for_in range(10):
	print("Mr.Ubial is cool")
	
```

for really large numbers, you can use the underscore (__) to indicate a comma

Recall that when we iterate over lists, the item tells us the current element that we are on.

When we iterate using range(), the item tells us **how many times we've looped since the beginning.**

For example, we can leverage this in the way below:

```python
for i in range(5)
	print(i)
	
```

i helps us count how many iterations we have done
**recount that python is a zero sum language, PYTHON BEGINS COUNTING AT 0**

Simply put, i is a counter. It counts how many times we are looping.



# `Range(<number>)`

	`range()`` is a function that gives you a sequence of numbers starting at 0 by default. 
	we can technically change where it starts but BY DEFAULT IT IS 0. 
By default it also goes up by 1. Finally, it stops right before the number that we provide as input.

```python
range(100) # sequence(0,1,2,3,4,5,6,7,8 ..., 99)
```


```python
list(range(100))
```
We can modify range() to start, stop, and count up/down by different numbers.

```python
range(<stop>)
range(<start>, <stop>)
range(<start>,<stop>,<step>)
```

# Can we start at another number?
	yes! 
for i in range (1,100):
	print(i)

^ means to start at 1 and goes until 99


REMEMBER THAT THE ALGORITHM WILL STOP AT THE NUMBER BEFORE

# Can we count by any other number 
for i in range(0,101,3):
	print(i)


e.g. 
```python
range(0,100)  # Sequence(0,1,2, ..., 99)
range(-10,10) #sequence(-10,-9,-8,... 9)
range(0,100,2) # sequence(0,2,4, ... 9)
range(100,0,-1) #sequence(100, 99, 98, ... 1)
```
**recount that python is a zero sum language, PYTHON BEGINS COUNTING AT 0**



  
  
  







