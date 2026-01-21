"""
4. Even or Odd (With Function)
    Create:
        main()
        is_even(n) that returns True or False
    Use it to print "Even" or "Odd".
"""

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()