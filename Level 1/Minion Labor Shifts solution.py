def solution(data, n):
    dup = data[:]
    for i in dup:        
        if data.count(i) > n:
            while i in data:
                data.remove(i)
    return data
