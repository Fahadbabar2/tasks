m1 = int(input("Mark 1: "))
m2 = int(input("Mark 2: "))
m3 = int(input("Mark 3: "))

total = m1 + m2 + m3
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("Total:", total)
print("Average:", average)
print("Grade:", grade)
