def helper( arr):
    stack = []
    sign = '+'
    num = 0
    while len(arr) > 0:
        c = arr.pop(0)
        if c.isdigit():
            num = num*10 + int(c)
        if c == '(':
            num = helper(arr)
        if c == '+' or c == '-' or c == ')' or len(arr) == 0:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            sign = c
            num = 0
            if c == ')':
                break
    return sum(stack)
s="1+1"
s=list(s)

print(helper(s))
