n = 5
arr1 = [9,20,28,18,11]
arr2=[30, 1, 21, 17, 28]
for i in range(n):
    arr1[i] = format(arr1[i],'b')
    arr1[i]= arr1[i].zfill(5)
    arr2[i] = format(arr2[i],'b')
    arr2[i]= arr2[i].zfill(5)
arr1 = list(map(list,arr1))
arr2 = list(map(list,arr2))

N_list = [[1 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if arr1[i][j] == arr2[i][j] =='0':
            N_list[i][j] ='0'

for z in range(n):
    for y in range(n):
        if N_list[z][y] == 1:
            N_list[z][y] = '#'
        else:
            N_list[z][y] = " "
print(N_list)