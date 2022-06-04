def solution(x):
    x = str(x)
    length = len(x)
    x=int(x)
    y=x
    a=[]

    for i in range(length-1,-1,-1):
        num = x//(10**i)
        a.append(num)
        x = x - num*(10**i)
    sum=0
    for j in range(length):
        sum += a[j]

    if y%sum==0:
        return True
    else:
        return False

print(solution(123))
