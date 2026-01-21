"""
1. Compare Two Numbers

    Write a program that asks for two integers and prints:
        "x is less than y"
        "x is greater than y"
        "x is equal to y"
    Use if, elif, else.
"""

x = int(input("What's x? "))
y = int(input("What's y"))

if x < y :
    print("x is less than y")
elif x > y :
    print("x is greater than y")
else:
    print("x is equal to y")
