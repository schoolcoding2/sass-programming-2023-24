
goes inside the function
default does not exist inside the function

the variable only exists once the function runs

there's default both inside and outside

def some_function 
default = "cat"

return "something"

``` python

# if we say some_function 
print(some_function)

# we would get "something"

# if we say 
print(default)

# the code will break since it only exists within the function

```

example:
```def specia(numbers):
for x in numbers:
for y in numbers:
if x < y: 
return x+y

print(special([3,1,2]))
```

in this example, there is a loop within a loop

so for the first loop:
x is set as term 0 

x = 3

y goes down the list  
1. y = 3 
2. y = 1
3. y = 2

check if x < y 
 1. no 3 = 3
 2. no 3 > 1
 3. no 3 > 2


x then moves down to term 1

x = 1

y goes down the list
1. yes 1 < 3
2. no 1 = 1
3. yes. 1< 2

take the first term in which we receive a yes

thus 

x = 1, y = 3

given the code telling us to do x +y 
then,

1 + 3 = 4

Therefore, the answer is 4



