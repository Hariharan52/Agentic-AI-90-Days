import json

student = {
    "name": "Hari",
    "age": 23,
    "skills": ["Python", "Java", "AI"]
}

with open("student.json",'w') as file:
    json.dump(student, file, indent = 4)