def reverse_string(s):
    for i in range((len(s) - 1) // 2):
        s[i], s[len(s) - 1] = s[len(s) - 1], s[i]

string = 'henlo'
print(string)
reverse_string(string)
print(string)
