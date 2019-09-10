# Longest common substring, O(n * m) time with dynamic programming

def longest_common_substring(s1, s2):
    # construct bottom up array
    db = []
    for i in range(len(s1)):
        db.append([0] * len(s2))
    for i, s1_c in enumerate(s1):
        for j, s2_c in enumerate(s2):
            if s1_c == s2_c:
                db[i][j] = db[i - 1][j - 1] + 1
            else:
                db[i][j] = 0
    longest = 0
    pair = None
    for i, v in enumerate(db):
        for j, v2 in enumerate(v):
            if db[i][j] > longest:
                longest = db[i][j]
                pair = (i, j)
    return s1[pair[0] - 2:pair[0] + 1]


a = 'fdsaaa'
b = 'aaafdx'

print(longest_common_substring(a, b))
