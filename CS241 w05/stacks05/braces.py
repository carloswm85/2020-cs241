stack_files = ['stacks01.txt', 'stacks02.txt', 'stacks03.txt','stacks04.txt', 'stacks05.txt', 'stacks06.txt']
# stack_files = ['stacks04.txt', 'stacks05.txt', 'stacks06.txt']
# RESULTS: NB B B NB NB B
print('Files are: {}'.format(stack_files))

def braces(braces_file):
    open_brace = ['(', '[', '{']
    close_brace = [')', ']', '}']
    stack = []
    with open(braces_file) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(lines) == 0:
                return  'Not balanced'
            content = line.strip()
            if content in open_brace:
                stack.append(content)
            elif content in close_brace:
                if len(stack) == 0:
                    return 'Not Balanced'
                popped = stack.pop()
                if content == ')' and popped != '(':
                    return 'Not Balanced'
                if content == ']' and popped != '[':
                    return 'Not Balanced'
                if content == '}' and popped != '{':
                    return 'Not Balanced'
        if len(stack) != 0:
            return 'Not Balanced'
        return 'Balanced'


for file in stack_files:
    print(braces(file))