def isBalanced(s):
    open = '([{'
    close = ')]}'
    match = {i: j for i, j in zip(close, open)}
    stack = []
    for c in s:
        if c in open:
            stack.append(c)
        elif stack and match.get(c) == stack[-1]:
            stack.pop()
        else:
            return 'NO'
    return('NO' if stack else 'YES')


a = '{(([])[])[]]}'

print(isBalanced(a))
