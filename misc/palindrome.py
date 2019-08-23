"""
Check for palindromes.
"""


def is_palindrome(string):
    return string == string[::-1]


test = 'WOW'
print('{} ---> {}'.format(test, is_palindrome(test)))
test = 'nope'
print('{} ---> {}'.format(test, is_palindrome(test)))
test = 'dsafaslkfla;skfa'
print('{} ---> {}'.format(test, is_palindrome(test)))
test = 'racecar'
print('{} ---> {}'.format(test, is_palindrome(test)))
