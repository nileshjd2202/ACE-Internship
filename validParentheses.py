s = "()[]{}"

stack = []
mapping = {')': '(', '}': '{', ']': '['}
for c in s:
    if c in mapping.values():
        stack.append(c)
    elif c in mapping.keys():
        if not stack or mapping[c] != stack.pop():
            print(False)
print(not stack)