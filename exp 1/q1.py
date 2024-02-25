#Write a Python program to find the factorial of a number using while loop

num = int(input("Please enter a number: "))
factorial = 1

while num >= 1:
    factorial = factorial * num
    num = num - 1
print("The factorial of the number is", factorial)
