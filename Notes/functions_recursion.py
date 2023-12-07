# Functions and Recursion
# Author: Ubial
# 7 December 2023

def factorial(n: int) -> int:
    """Return the nth factorial. 
    Done recursively. 

    Example:
        factorial(3) -> 3! -> 6
    """

    if n == 0 or n == 1:
        return 1    

    elif n > 1:
        return factorial(n-1) * n 
    
def fibonacci(n:int) -> int:
    """Return the nth Fibonacci number calculated recursively"""
    if n in [1,2]:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n -2) 
    

# print(fibonacci=(100))

print(fibonacci(20))


