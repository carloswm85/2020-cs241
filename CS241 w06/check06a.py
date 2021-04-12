class Book:
    def __init__(self):
        self.title = ''
        self.author = ''
        self.publication_year = 0

    def prompt_book_info(self):
        self.title = input('Title: ')
        self.author = input('Author: ')
        self.publication_year = input('Publication Year: ')

    def display_book_info(self):
        print('{} ({}) by {}'.format(self.title, self.publication_year, self.author))


class TextBook(Book):
    def __init__(self):
        self.subject = ''
        super().__init__()

    def prompt_subject(self):
        self.subject = input('Subject: ')

    def display_subject(self):
        print('Subject: {}'.format(self.subject))


class PictureBook(Book):
    def __init__(self):
        self.illustrator = ''
        super().__init__()

    def prompt_illustrator(self):
        self.subject = input('Illustrator: ')

    def display_illustrator(self):
        print('Illustrated by {}'.format(self.subject))


def main():
    regular_book = Book()
    text_book = TextBook()
    picture_book = PictureBook()

    regular_book.prompt_book_info()
    print()
    regular_book.display_book_info()
    print()

    text_book.prompt_book_info()
    text_book.prompt_subject()
    print()
    text_book.display_book_info()
    text_book.display_subject()
    print()

    picture_book.prompt_book_info()
    picture_book.prompt_illustrator()
    print()
    picture_book.display_book_info()
    picture_book.display_illustrator()


if __name__ == '__main__':
    main()
