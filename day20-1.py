def removeOuterParentheses(s):
    res, bal = "", 0
    for c in s:
        if c == '(' and bal > 0: res += c
        if c == ')' and bal > 1: res += c
        bal += 1 if c == '(' else -1
    return res

s = input("Enter parentheses string: ")
print(removeOuterParentheses(s))