n = int(input())

def answer(area):
    import math
    a = []
    
    while(1):
        a.append((int(math.sqrt(area))) ** 2)
        area = area - (int(math.sqrt(area)) ** 2)
        if area == 0:
            break
            
    return a
