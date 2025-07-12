# Python excercise to find factorial of a number
# Author: Anuj Savant
# Date: 12/07/25

num = int(input("Enter the number:"))

for i in range(1, num):
    num = num * i

print(f"The factorial of number is = {num}")