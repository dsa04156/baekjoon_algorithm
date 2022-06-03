T = int(input())
for i in range(T):
    sum=0
    count = 0
    N_list = list(map(int,input().split()))
    for j in range(1,N_list[0]+1):
        sum += N_list[j]
    average = sum / N_list[0]
    for x in range(1,N_list[0]+1):
        if N_list[x] > average:
            count +=1
    c =round(count/N_list[0]*100,3)
    res = "{:.3f}".format(c)

    print("{}%".format(res))
