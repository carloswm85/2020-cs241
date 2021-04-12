from collections import deque


class Student:
    def __init__(self):
        self.name = 'No name'
        self.course = 'No course'

    def prompt(self):
        self.name = input('Enter name: ')
        self.course = input('Enter course: ')

    def display(self):
        print('Student name: {}\nStudent course: {}'.format(self.name, self.course))


class HelpSystem:
    def __init__(self):
        self.waiting_list = deque()

    def is_student_waiting(self):
        if len(self.waiting_list) == 0:
            return False
        else:
            return True

    def add_to_waiting_list(self, student):
        self.waiting_list.append(student)

    def help_next_student(self):
        if len(self.waiting_list) == 0:
            print('No one to help.')
        else:
            student = self.waiting_list.popleft()
            print('Now helping {} with {}'.format(student.name, student.course))


def main():
    waiting_list = HelpSystem()
    run = True

    while run:
        print('\nOptions:')
        print('1. Add a new student')
        print('2. Help next student')
        print('3. Quit')
        selection = int(input('Enter selection: '))
        print()

        if selection == 1:
            new_student = Student();
            new_student.prompt()
            new_student.display()
            waiting_list.add_to_waiting_list(new_student)
        elif selection == 2:
            waiting_list.help_next_student()
        else:
            run = False
    else:
        print('Goodbye')


if __name__ == '__main__':
    main()
