import datetime

def solution(a, b):
    answer = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = datetime.date(2016,a,b).weekday()
    return answer[day]