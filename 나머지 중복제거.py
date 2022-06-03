N = int(input())
N_list = list(map(int,input().split()))
M = max(N_list)
sum =0
for i in range(N):
    N_list[i] = N_list[i]/M *100
    sum += N_list[i]
print(sum/N)