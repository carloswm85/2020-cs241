class Student(object):
    def __init__(self):
        self.FirstName = "Mike"
        self.LastName = "Mono"
        self.id = 0
        
def prompt_student():
    new_student = Student()
    new_student.FirstName = input("Please enter your first name: ")
    new_student.LastName = input("Please enter your last name: ")
    new_student.id = input("Please enter your id number: ")
    return new_student

def display_student(student_object):
    print("\nYour information:")
    print(student_object.id, "-", student_object.FirstName, student_object.LastName)
    
def main():
    user = prompt_student()
    display_student(user)

if __name__ == "__main__":
    main()

