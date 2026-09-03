print("------------------------------------Adding_employee------------------------------------------")
employees = []
def add_employee():
    employee_id=int(input("Employee id: "))
    employee_name = (input("Employee name: "))
    employee_age = int(input("Employee age: "))
    employee_department = (input("Employee department: "))
    employee_salary = float(input("Employee salary: "))
    employee={
        "id":employee_id,
        "name":employee_name,
        "age":employee_age,
        "department":employee_department,
        "salary":employee_salary

    }
    employees.append(employee)
add_employee()
print("-------------------------------------------------------------------------------")
add_employee()
print("-------------------------------------------------------------------------------")
add_employee()
print(employees)
print("-------------------------------------------------------------------------------")

def display_employees():
    print("==================Display_employee=========================")
    for emp in employees:
        print("ID:",emp["id"])
        print("Name:", emp["name"])
        print("Age:",emp["age"])
        print("Department:",emp["department"])
        print("salary",emp["salary"])
        print("-----------------------------------------------------")


def search_employee(employee_id):


    employee_id = int(input("Enter employee ID: "))

    found = False

    for emp in employees:
        if emp["id"] == employee_id:
            print("ID:", emp["id"])
            print("Name:", emp["name"])
            print("Age:", emp["age"])
            print("Department:", emp["department"])
            print("salary", emp["salary"])

            found = True


    if not found:
        print("Employee not found")
search_employee(1)

def calculate_salary():
    employee_id=int(input("enter the employee id"))
    found=False
    for emp in employees:
        if emp["id"]==employee_id:

            Bonus=emp["salary"]*0.10
            total=emp["salary"]+Bonus
            found=True
            return total

    if not found:
        print("user id not found")
        return None
total_salary=calculate_salary()
if total_salary is not None:
    print("total Salary after adding bonus",total_salary)


def filter_employees():
    minimum_salary = int(input("Enter minimum salary: "))

    filtered_employees = filter(
        lambda emp: emp["salary"] >= minimum_salary,
        employees
    )
    for emp in filtered_employees:
        print(emp)
filter_employees()

def sort_employees():
    print("-----------------------------sorted employee-------------------------------")
    sorted_employee=sorted(employees,key=lambda emp:emp["salary"])
    for emp in sorted_employee:
        print(emp)
sort_employees()