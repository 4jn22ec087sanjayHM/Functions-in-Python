


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