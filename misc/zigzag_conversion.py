# zigzag conversion problem

def zigzag_conversion(s, num_rows):
    if num_rows < 2:
        return s
    flag = True
    val = 0
    answer = [""] * len(s)
    for c in s:
        answer[val] += c
        if val == num_rows - 1:
            flag = False
        elif val == 0:
            flag = True 
        val += 1 if flag else -1
    return ''.join(answer)

num_rows = 4

print(zigzag_conversion(s, num_rows))
