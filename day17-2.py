def postfix_to_prefix():
    s, ops = [], '+-*/'
    for ch in input("Enter postfix: "):
        s.append(ch if ch not in ops else ch + s.pop(-2) + s.pop())
    print("Prefix:", s[0])

postfix_to_prefix()