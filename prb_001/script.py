'''def prb():
    sum = 0
    for x in range(1, 1000):
        if (x % 3 == 0) or (x % 5 == 0):
            sum = sum + x
    return sum


print(prb())
'''
#print(sum((x for x in range(1, 1000) if ((x % 3 == 0) or (x % 5 == 0)))))
print(sum((x for x in range(1, 1000) if ((x % 3 == 0) or (x % 5 == 0)))))
