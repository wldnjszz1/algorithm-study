import string


def solution(s, n):
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    s = list(s)
    for idx, ss in enumerate(s):
        if ss in alphabet_lower:
            position = (alphabet_lower.index(ss) + n) % 26
            s[idx] = alphabet_lower[position]
        elif ss in alphabet_upper:
            position = (alphabet_upper.index(ss) + n) % 26
            s[idx] = alphabet_upper[position]
        else:
            pass

    return ''.join(s)