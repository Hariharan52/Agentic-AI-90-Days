def cal_average(marks):
    return sum(marks) / len(marks)

def cal_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 50:
        return 'c'
    else:
        return 'Fail'


name = input("Enter Student Name:")

marks = []

for i in range(1,6):
    mark = int(input(f"Enter subject {i} mark: "))
    marks.append(mark)

average = cal_average(marks)
grade = cal_grade(average)

print("Student Report:")
print("Name: ",name)
print("Total Marks: ", sum(marks))
print("Average: ", round(average,2))
print("Grade: ",grade)