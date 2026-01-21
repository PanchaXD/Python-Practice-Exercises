"""
5. Multiple of 3

    Ask for a number and print:
        "Multiple of 3" if divisible by 3
        "Not a multiple of 3" otherwise
"""

def main():
    x = int(input("What's x? "))

    if is_multiple(x):
        print("Multiple of 3")
    else:
        print("Not a multiple of 3")

def is_multiple(n):
    if n % 3 == 0:
        return True
    else:
        return False

main()