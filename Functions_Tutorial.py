'''
Topics Covered
Introduction to Functions
Function Syntax and Structure
Function Parameters and Arguments
Return Statements and Return Values
Function Scope and Variable Visibility
Default Arguments and Keyword Arguments
Anonymous Functions (Lambda Functions)
Recursive Functions
Higher-Order Functions
Decorators
'''

#Topic 1: Introduction to Functions
#This topic provides a basic introduction to functions in Python.

#Code Example
# Function definition
def greet():
    print("Hello, world!")

# Function call
greet()

#Topic 2: Function Syntax and Structure
#This topic covers the syntax and structure of functions in Python, including function names, parameters, and the use of parentheses.

# Function definition with parameters
def greet(name):
    print("Hello, " + name + "!")

# Function call with argument
greet("Alice")


#Topic 3: Function Parameters and Arguments
#This topic explains the concepts of function parameters and arguments, including positional arguments and keyword arguments.

# Function definition with multiple parameters
def add_numbers(x, y):
    sum = x + y
    print("The sum is:", sum)

# Function call with positional arguments
add_numbers(5, 3)

# Function call with keyword arguments
add_numbers(y=2, x=7)

#Topic 4: Return Statements and Return Values
#This topic covers the usage of return statements in functions and understanding return values.

# Function with return statement
def multiply(x, y):
    product = x * y
    return product

# Function call and return value assignment
result = multiply(4, 6)
print("The result is:", result)


#Topic 5: Function Scope and Variable Visibility
#This topic explains the concept of function scope and the visibility of variables within functions.

# Global variable
global_var = "I'm a global variable"

# Function with local variable
def function():
    local_var = "I'm a local variable"
    print(local_var)

# Accessing global and local variables
print(global_var)
function()


#Topic 6: Default Arguments and Keyword Arguments
#This topic covers the usage of default arguments and keyword arguments in function definitions.

# Function with default argument
def greet(name="World"):
    print("Hello,", name + "!")

# Function call with default argument
greet()

# Function call with keyword argument
greet(name="Alice")


#Topic 7: Anonymous Functions (Lambda Functions)
#This topic introduces anonymous functions, also known as lambda functions, and their usage in Python.

# Lambda function to add two numbers
add = lambda x, y: x + y

# Calling the lambda function
result = add(3, 5)
print("The sum is:", result)


#Topic 8: Recursive Functions
#This topic covers recursive functions, which are functions that call themselves within their own definition.

# Recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the recursive function
result = factorial(5)
print("The factorial is:", result)


#Topic 9: Higher-Order Functions
#This topic explores higher-order functions, which are functions that can accept other functions as arguments or return functions as their output.

# Higher-order function to perform an operation on a number
def apply_operation(func, x):
    return func(x)

# Example functions to be used with the higher-order function
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

# Calling the higher-order function with different functions
result1 = apply_operation(square, 5)
result2 = apply_operation(cube, 3)

print("Result 1:", result1)
print("Result 2:", result2)


#Topic 10: Decorators
#This topic introduces decorators, which allow modifying the behavior of functions or adding functionality to existing functions.

# Decorator function to add extra functionality to a function
def greeting_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

# Function to be decorated
def greet():
    print("Hello, world!")

# Applying the decorator to the function
decorated_greet = greeting_decorator(greet)

# Calling the decorated function
decorated_greet()
