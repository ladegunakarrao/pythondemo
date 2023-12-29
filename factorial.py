def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Taking input from the user
num = int(input("Enter a number to find its factorial: "))

# Checking if the number is negative
if num < 0:
    print("Factorial cannot be found for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")
