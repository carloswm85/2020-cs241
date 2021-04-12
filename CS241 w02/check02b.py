file_name = input("Enter file: ")

file = open(file_name, "r")

number_lines = 0
number_words = 0

for line in file:
    number_lines += 1
    words = line.split()
    for word in words:
        number_words += 1
        
file.close()
    
print("The file contains", number_lines,
      "lines and", number_words, "words.")
