def findBraces():
    user = 'stacks06.txt'
    jOpen = open(user, "r")
    stack = []
    for i in jOpen:
        k = i.strip()
        for ch in k:
            # if current character is an open one just add to the stack
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            # if current character is any type of closing brace: ), }, ]
            if ch == ')' or ch == ']' or ch == '}':
                # If the stack is empty (nothing to compare)
                if len(stack) == 0:
                    # Quit now, it doesn't match
                    return "not balance"
                lastch = stack.pop()
                # if they match (meaning closing of the same type):
                # We're good
                # Pop the opening brace off the stack
                # If they don't match
                # Quit now, and tell them the braces don't match
                if lastch == '(' and (ch != ')'):
                    return "not balanced"
                if lastch == '[' and (ch != ']'):
                    return "not balanced"
                if lastch == '{' and (ch != '}'):
                    return "not balanced"
    # after reading the complete file
    # If there is anything on the stack, the braces didn't match
    if len(stack) != 0:
        return "not balanced"
    return "Balanced"

print(findBraces())