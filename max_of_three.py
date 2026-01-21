"""
6. Bigger of Three Numbers
    Ask for three integers and print the largest one.
"""

def main():
    x = int(input("What's x? "))   
    y = int(input("What's y? "))
    z = int(input("What's z? "))

    largest = biggest_of_three(x, y, z)
    print("The largest number is: ", largest)

def biggest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


main()