# solution for the Minion Labor Shifts problem in Level 1

def solution(data, n):
    dup = data[:]
    for i in dup:        
        if data.count(i) > n:
            while i in data:
                data.remove(i)
    return data