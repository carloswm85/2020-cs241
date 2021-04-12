def prompt_filename():
    file_name = input("Enter file name: ")
    return file_name

def prompt_word():
    word = input('What word do you want to find? Write it here: ')
    return word

def parse_file(parseable_file, findable_word):
    counted_words = 0
    # counting_words = [0, 0]
    opened_file = open(parseable_file, 'r', encoding='utf8')
    for line in opened_file:
        words = line.split()
        for word in words:
            new_word = word.strip('.,—”“')
            lower_word = new_word.lower()
            if lower_word.startswith(findable_word):
                counted_words += 1
                
    opened_file.close()
    return counted_words

def main():
    file_name_main = prompt_filename()
    print("Opening file", file_name_main)
    findable_word_main = prompt_word()
    num = parse_file(file_name_main, findable_word_main)
    print('The word "', findable_word_main, '" occurs', num, 'times in this file')
    
if __name__ == "__main__":
    main()