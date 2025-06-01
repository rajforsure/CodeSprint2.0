def reverse_string_with_stack():
    stack = []

    s = input("Enter any string to reverse: ")

    for char in s:
        stack.append(char)

    reversed_str = ''
    while stack:
        reversed_str += stack.pop()

    print("Reversed string:", reversed_str)

reverse_string_with_stack()