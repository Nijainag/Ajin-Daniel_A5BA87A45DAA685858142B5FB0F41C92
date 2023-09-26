# 1.1 implement a recursive function to calculate the factorial of a given number
"""
1!=1×1
2!=2×1!--->2×1
3!=3×2!--->3×2×1
.
.
10!=10×9!--->10×9×8×.....×1
formula-n×(n-1)!
"""


def recursive_factorial(n):
  if n == 1:
    return n
  else:
    return n * recursive_factorial(n - 1)  #function calling itself


#taking input from the user
number = int(input("Enter a value: "))
print("The factorial of", number, "is", recursive_factorial(number))