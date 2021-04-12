class Phone:
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number(self):
        self.area_code = input('Area Code: ')
        self.prefix = input('Prefix: ')
        self.suffix = input('Suffix: ')

    def display(self):
        print('Phone info:')
        print('({}){}-{}'.format(self.area_code, self.prefix, self.suffix))


class Smartphone(Phone):
    def __init__(self):
        self.email = ''
        super().__init__()

    def prompt(self):
        super().prompt_number()
        self.email = input('Email: ')

    def display(self):
        super().display()
        print(self.email)

def main():
    phone = Phone()
    s_phone = Smartphone()

    print('Phone:')
    phone.prompt_number()
    print()
    phone.display()
    print()

    print('Smart phone:')
    s_phone.prompt()
    print()
    s_phone.display()


if __name__ == '__main__':
    main()