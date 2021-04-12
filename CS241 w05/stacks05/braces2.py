braces = []

print()
run = True

stack_files = ['stacks01.txt', 'stacks02.txt', 'stacks03.txt','stacks04.txt', 'stacks05.txt', 'stacks06.txt']
# stack_files = ['stacks04.txt', 'stacks05.txt', 'stacks06.txt']
print('Files are: {}'.format(stack_files))

open_brace = ['(', '[', '{']
close_brace = [')', ']', '}']

for filename in stack_files:
    print(filename)
    file_object = open(filename, 'r')
    lines = file_object.readlines()
    if len(lines) == 0:
        print('Empty.')
    else:
        for line in lines:
            line_content = line.split()
            for content in line_content:
                if content in open_brace:
                    braces.append(content)
                    balanced = False
                elif content in close_brace:
                    try:
                        test = braces.pop()
                        if content == ')' and test == '(':
                            balanced = True
                        elif content == ']' and test == '[':
                            balanced = True
                        elif  content == '}' and test == '{':
                            balanced = True
                        else:
                            balanced = False
                            break;
                    except IndexError:
                        print('Error')
        if balanced:
            print('Balanced.')
        else:
            print('Not balanced.')
    file_object.close()
    braces = []


