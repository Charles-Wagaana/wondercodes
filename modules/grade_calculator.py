# Calculating the grade of a student in a subject.
marks = []
total_marks = 0
percentage_mark = None
while len(marks) < 5:
    mark = int(input("Enter mark: "))
    marks.append(mark)
    total_marks += mark
    percentage_mark = (total_marks/(len(marks)*100))*100

if percentage_mark < 50:
    print('Grade C')
elif 50 <= percentage_mark < 80:
    print('Grade B')
else:
    print('Grade A')
print(marks)
print(total_marks)
print("Percentage: {}%".format(int(percentage_mark)))




