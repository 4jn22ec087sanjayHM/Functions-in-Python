employee = [
    ("Sanjay", 30000),
    ("Rahul", 45000),
    ("Priya", 28000),
    ("Arun", 50000)
]
salary=sorted(employee, key=lambda employee:employee[1],reverse=True)
print(salary)
