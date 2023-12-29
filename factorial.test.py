# Save this code in a file named test_factorial.py

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test cases for factorial function
def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive():
    assert factorial(5) == 120

def test_factorial_negative():
    assert factorial(-5) == None  # Factorial cannot be found for negative numbers

# Additional test cases for edge scenarios or large numbers
def test_factorial_large_number():
    assert factorial(10) == 3628800

def test_factorial_large_negative():
    assert factorial(-10) == None  # Factorial cannot be found for negative numbers
