def Add(Num):
    Sum = 0
    for i in range(Num):
        if i%4 == 0:
            Sum += i

    return Sum

print(Add(400))