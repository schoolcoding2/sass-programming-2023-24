# Functions and Recursion
# Author: Emily 
# 7 December 2023

import time

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
    

def fibonacci_itr(n:int) -> int:
    """Returns the nth Fibonacci number.
    Calculated iteratively."""
    last_num = 0
    num = 1
    result = 1

    for i in range(n-1):
        result = num + last_num

        num, last_num = result, num
        return result
# itr = iterator 
    
# print(factorial(100))

print(fibonacci(5), fibonacci_itr(5))

# calculate how much time has elasped
time_initial = time.perf_counter() 
fibonacci(20)
time_final = time.perf_counter()

print(f"Recursive:{time_final - time_initial}")

time_initial = time.perf_counter()
fibonacci_itr(20)

time_final = time.perf_counter()

print(f"Iterative:{time_final - time_initial}")


# iteration is a lot faster to run than loops


