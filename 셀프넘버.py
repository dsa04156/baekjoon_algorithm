def sol(n):
    n = str(n)
    length = len(n)
    n=int(n)
    a=[]
    m=n
    p=0
    sum=0
    for i in range(length-1,-1,-1):
        a.append(m//(10**i))
        m=m-a[p]*(10**i)
        p+=1
    for j in range(length):
        sum += a[j]
    sum += n
    if sum <100:
        sol(sum)
    return sum
    

set_a = []
for i in range(1,10000):
    set_a.append(sol(i))
set_a = set(set_a)

set_b = [i for i in range(1,10000)]
set_b = set(set_b)
set_b = set_b - set_a
set_b = list(set_b)
set_b.sort()
for i in range(len(set_b)):
    print(set_b[i])