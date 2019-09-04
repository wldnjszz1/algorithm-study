def solution(array, commands):
    start = list()
    last = list()
    pick = list()
    aanswer = list()
    answer = list()
    for i in range(len(commands)):
        start.append(commands[i][0])
        last.append(commands[i][1])
        pick.append(commands[i][2])
    for i in range(len(start)):
        c = array.copy()
        c = array[start[i]-1:last[i]]
        c.sort()
        aanswer.append(c)
    for i in range(len(pick)):
        answer.append(aanswer[i][pick[i]-1])
    return answer