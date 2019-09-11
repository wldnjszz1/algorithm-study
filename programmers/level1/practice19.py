def solution(s):
    ss = s.split(" ")
    for i, string in enumerate(ss):
        for idx, alphabet in enumerate(string):
            if idx % 2 == 0:
                string = string[:idx] + string[idx].upper() + string[idx + 1:]
            else:
                string = string[:idx] + string[idx].lower() + string[idx + 1:]
        ss[i] = string
    return " ".join(ss)