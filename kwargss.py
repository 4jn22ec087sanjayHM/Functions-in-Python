


def create_employee(**details):
    for key,values in details.items():
        print(key,":" ,values)


 create_employee(
       name="Sanjay",
        age=22,
        department="Python",
        salary=30000,
        city="Shivamogga"
    )
def create_employee(name, age, department, salary):
    print("Name:",name)
    print("age:",age)
    print("department:",department)
    print("Salary:",salary)


employee = {
    "name": "Sanjay",
    "age": 22,
    "department": "Python",
    "salary": 30000
}
create_employee(**employee)
def process_order(customer, *items, **details):
    print(customer)
    for item in items:
        print(item)
    for key,value in details.items():
        print("Additional details: ",key,value)
process_order(
        "Sanjay",
        "Laptop",
        "Mouse",
        "Keyboard",
        city="Shivamogga",
        payment="UPI"
    )
def calculate_student_marks(english, python, sql):
    total=english+python+sql
    percentage=((total)/300)*100
    if percentage>=40:
        result="pass"
    else:
        result="fail"
    return total,percentage,result


total, percentage, result = calculate_student_marks(78, 92, 85)
print(total)
print(percentage)
print(result)