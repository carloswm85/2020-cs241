from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self):
        self.name = ""

    @abstractmethod
    def display(self):
        print("{}".format(self.name))

    @abstractmethod
    def get_paycheck(self):
        return 0


class HourlyEmployee(Employee):
    def __init__(self):
        self.hourly_wage = 0
        self.hours = 0
        super().__init__()

    def display(self):
        print('{} - ${:.2f}/hour'.format(self.name, self.hourly_wage))

    def get_paycheck(self):
        self.paycheck = self.hourly_wage * self.hours
        return self.paycheck


class SalaryEmployee(Employee):
    def __init__(self):
        self.salary = 0
        super().__init__()

    def display(self):
        print("{} - ${:.2f}/year".format(self.name, self.salary))

    def get_paycheck(self):
        self.paycheck = self.salary / 24
        return self.paycheckh


def display_employee_data(employee):
    employee.display()
    employee.get_paycheck()


def main():
    employees = []
    command = ''

    while command != 'q':
        command = input('Please enter "h" for hourly employee, "s" for salary employee or "q" to quit: ')

        if command == 'h':
            employee = HourlyEmployee()
            employee.name = input('Enter name:')
            employee.hourly_wage = float(input("Please enter your hourly wage: "))
            employee.hours = int(input('Enter number of hours: '))
            employees.append(employee)
        elif command == 's':
            employee = SalaryEmployee()
            employee.name = input('Enter name:')
            employee.salary = float(input("Enter salary: "))
            employees.append(employee)

    for item in employees:
        display_employee_data(item)


if __name__ == '__main__':
    main()
