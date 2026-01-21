"""
7. Simple Grade Program
    Ask for a score and print:
        A, B, C, D, or F

    Using:
        if score >= 90:
        elif score >= 80:
        ...
"""

score = int(input("what's your mark? "))

if score >= 90:
    print("Your Grade is: A")
elif score >= 80:
    print("Your Grade is: B")
elif score >= 70:
    print("Your Grade is: C")
elif score >= 60:
    print("Your Grade is: D")
else:
    print("Your Grade is: F")

