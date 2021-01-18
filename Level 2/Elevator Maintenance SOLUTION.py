def solution(l):
    l = [i.split('.') for i in l]
    
    for i in l:
        for j in range(len(i)):
            if len(i[j]) == 1:
                i[j] = '0'+i[j]

    l.sort()
    
    for i in l:
        for i in l:
            for j in range(len(i)):
                if i[j][0] == '0' and len(i[j]) == 2:
                    i[j] = i[j][1:]
                                        
    for i in range(len(l)):
        l[i] = '.'.join(l[i])

    return l
