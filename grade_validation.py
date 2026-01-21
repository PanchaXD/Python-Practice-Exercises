"""
8. Grade With Validation

    If the score is less than 0 or greater than 100, print:
        "Invalid score"
    Otherwise, print the grade.
"""

score = int(input("what's your mark? "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Your Grade is: A")
elif score >= 80:
    print("Your Grade is: B")
elif score >= 70:
    print("Your Grade is: C")
elif score >= 60:
    print("Your Grade is: D")
else:
    print("Your Grade is: F")