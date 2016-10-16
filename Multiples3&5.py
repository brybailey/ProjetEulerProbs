
mult35 = [x for x in range(0,1000) if x%3 == 0 or x%5 ==0]


def multiples():
    sum = 0
   
    for x in mult35:
        sum += x
    return sum

print multiples()
