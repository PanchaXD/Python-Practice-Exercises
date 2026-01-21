"""
10. Divisible by 2 and 5

    Ask for a number and print:
        "Divisible by both"
        "Not divisible by both"
    Use and.
"""


def main():
    x = int(input("What's x? "))

    if is_divisible(x):
        print("Divisible by both")
    else:
        print("Not divisible by both")

def is_divisible(n):
    if n % 2 == 0 and n % 5 == 0:
        return True
    else:
        return False


main()