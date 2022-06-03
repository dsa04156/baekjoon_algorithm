N = int(input())
i,M=0,100
p=N

    


while N!=M:
    if p<10:
        M = p*10+p
        p = M
        i+=1
    else:
        a = p//10
        b = p-a*10
        sum = a+b
        if sum >=10:
            sum %= 10
        M = b*10 + sum
        p=M
        i+=1
print(i)