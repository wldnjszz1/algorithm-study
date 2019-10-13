def solution(bridge_length, weight, truck):
    q = [0] * bridge_length
    time = 0

    while q:
        q.pop(0)
        time += 1

        if truck:
            if sum(q) + truck[0] <= weight:
                q.append(truck.pop(0))
            else:
                q.append(0)

    return time