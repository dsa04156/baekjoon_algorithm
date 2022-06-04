arr = list(map(int,input().split()))
arr_set = set(arr)
arr_set = list(arr_set)
res = []

for i in range(len(arr_set)):
    if arr.count(arr_set[i]) >1:
        res.append(arr.count(arr_set[i]))
print(res)