score = int(input("What is your score?"))
"""
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# can we tighten this up, make it better code

if 90 <= score <= 100: # this is not possible in other languages!
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
"""
# can we reduce questions further? can we optimise further? more maintenanable longer term
if score >= 90: 
    print("Grade: A")
elif score >= 80: # elif means mutuall exclusive! if we change to an if then every one will run
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
