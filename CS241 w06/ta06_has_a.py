class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def prompt_for_point(self):
        self.x = int(input('Enter x: '))
        self.y = int(input('Enter y: '))

    def display(self):
        print('Center:')
        print('({}, {})'.format(self.x, self.y))


class Circle:
    def __init__(self):
        self.radius = 0
        self.center = Point()

    def prompt_for_circle(self):
        self.center.prompt_for_point()
        self.radius = int(input("Enter radius: "))

    def display(self):
        self.center.display()
        print('Radius: {}'.format(self.radius))


def main():
    circle = Circle()
    circle.prompt_for_circle()
    print()
    circle.display()


if __name__ == '__main__':
    main()















