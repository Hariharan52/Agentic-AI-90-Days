'''file = open("student.txt", "r")

content = file.read()

print(content)

file.close()'''

with open("student.txt", 'r') as file:
    content = file.read()
    print(content)