"""
9. Equal or Not (Short Version)

    Ask for two numbers and print:
        "Equal" if x == y
        "Not equal" otherwise
    Use only one if and one else.
"""

x = int(input("what's x? "))
y = int(input("what's y? "))

if x == y:
    print("Equal")
else:
    print("Not equal")



x = int(input("What's x? "))

if x % 2 == 0 and x % 5 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")