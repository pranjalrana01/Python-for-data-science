score = 855

if(score >= 101):
    print("this is not proper score for grading")
    exit()

if score >= 90:
    grade = "A"
elif score >=80:
    grade = "B"
elif score >=70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("your grade is", grade)