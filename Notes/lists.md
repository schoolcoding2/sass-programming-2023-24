In python, lists are a collection of items
We store values inside of lists
The values of the items can be of different [[types]]
**order matters** in a list
MAKE SURE TO SEPARATE EACH LIST ITEM BY A COMMA
# creating a list
to make a list, we use brackets [] to surround our lists
We separate the individual items with commas

```
python
some_list= ["Jimmy", "Sara", "Frederique"]
```


jimmy comes before sara, sara comes before Frederique

For "sets" and "dictionaries" order doesn't matter

# Access Elements in the list

we can access the individual things from lists using **bracket notation** 
In the example below, we'll use bracket notation to access "Sara"

```
python
some_list[1]            # "sara"
some_list[0]           # "Jimmy"
some_list[2]           # "Frederique"
some_list[-1]          # "Frederique" counts from the end 
some_list[-2]         # "sara"   
```


We can go backwards to access the item from the **back** / end of the list

Inside the brackets [index], we give the *index* of the item we want
Python uses 0-index counting, which means we start counting at 0

semantic error- off by 1 error **so be careful when counting**

c++, java (other languages call lists "arrays")

# 2-Dimensional Lists

so far, all the lists we've used are one-dimensional

```python
some_list = ["blue", "red", "green"]
```

We can create two-dimensional lists that are in short, are multiple lists inside a bigger list. 

```python
some_2d_list = [
	[1,2,3], 
	[4,5,6],
	[7,8,9]
	
 #          row column 
some_2d_list[0][0] # -> 1
some_2d_list[0][1] # -> 2
]
```
humans know 2-d lists very well; it has rooms and columns 

Recall that we can access negative indices through bracket notation 
# Tuples 

Tuples (toopels or tuhpels) 
like lists EXCEPT for one main component.
Tuples are **immutuable** meaning that you cannot change the contents of a tuple


Because they are immutable they have some performance benefits. 

```python

some_tuple = (1,2,3,4,5)

```

To create a tuple, use **parentheses** instead of brackets

### Images and Tuples 

The basic unit of measurement in images is a pixel
The pixel information is stored in a tuple of three-values

(3-tuple). 

The 3-tuple tells us that for ONE PORTION of the image, what the RED, GREEN, BLUE values are. `(red,green, blue)`

```python
       r,   g,    b

RED - (255,  0,   0 )
BLUE - (0,   0,   255 )
Green - (0,  255,  0 )
```





