students = [
    {"name": "Little Genius", "age": 12, "iq": 125},
    {"name": "student One", "age": 19, "iq": 102, },
    {"name": "student Two", "age": 20, "iq": 89},
    {"name": "student Third", "age": 21, "iq": 95},
    {"name": "Ent Stu", "age": 22, "iq": 93},
    {"name": "U Che Nic", "age": 25, "iq": 97},
    {"name": "Stuard Pidleton", "age": 29, "iq": 80},
]
students.sort()
students.sort(key=lambda x: x.get("name"))

filter(lambda x: x.get("age") > 21, students)