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


jimmy comes before sara, sara comes before frederique

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
