# should be an O(n) solution 'sliding window'. could be optimized with a dict.

def longest_substring_without_repeating_characters(s):
    streak = []
    max_substring = 0
    for c in s:
        if c in streak:
            max_substring = max(len(streak), max_substring)
            last_appeared = streak.index(c)
            streak = streak[last_appeared + 1:]
        streak.append(c)
    max_substring = max(len(streak), max_substring)
    return max_substring
