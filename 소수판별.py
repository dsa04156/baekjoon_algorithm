nums = [1,2,3,4] #1

a=[]
for x in nums:
    for y in nums:
        for z in nums:
            if x!=y and y!=z and z!=x:
                sum = x+y+z
                a.append(sum)
a = set(a)
a = list(a)

b= []

for i in range(len(a)):
    p=1
    for j in range(2,a[i]):
        if a[i]%j==0:
            p = 0
            break
    if p==1:
        b.append(a[i])

print(len(b))