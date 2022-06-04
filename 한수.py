def sol(n):
    cnt=0
    for i in range(1,n+1):
        a= list(map(int,str(i)))
        if 100<= i <1000:
            if a[1]-a[0] == a[2]-a[1]:
                cnt+=1
        elif i<100:
            cnt += 1

    return cnt


    
