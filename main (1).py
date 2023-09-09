#Implement a recursive function to calculate the factorial of a given number 
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Input from the user
num = int(input("Enter a number= "))

# Check if the number is negative
if num < 0:
  print("factorial is not defined for negative number.")
elif num == 0:
  print("The factorial of 8 is 1")
else:
  result = factorial(num)
  print(f"The factorial of {num} is {result}")