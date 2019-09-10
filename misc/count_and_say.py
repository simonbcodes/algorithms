# count and say the number out loud, then make the next number based on what you said. This probably shouldn't be run for N greater than 30ish

def count_and_say(n):
    seq = '1'
    for _ in range(n - 1):
        i = 0
        new_seq = ''
        while i < len(seq):
            j = 0
            while i + j < len(seq) and seq[i] == seq[i + j]:
                j += 1
            new_seq += str(j) + seq[i]
            i += j
        seq = new_seq
    return seq

print(count_and_say(20))
