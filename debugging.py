import pdb

def factorial(n):
    if n == 0:
        return 1
    else:
        result = n * factorial(n - 1)
        return result

# Set a breakpoint to debug the factorial function
pdb.set_trace()

number = 5
fact = factorial(number)
print(f"The factorial of {number} is {fact}")
