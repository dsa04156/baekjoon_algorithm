N=5
stages = [2,1,2,6,2,4,3,3]
d = []
a=[]
dic = {}
for i in range(1,N+1):
    d.append(stages.count(i) / len(stages))
    while i in stages:
        stages.remove(i)
for j in range(1,N+1):
    dic[j]=d[j-1]
print(dic)

# dic = sorted(dic.items(), key = lambda item: item[0], reverse = True)
dic = sorted(dic.items(), key = lambda item: item[1], reverse = True)
for i in range(N):
    a.append(dic[i][0])

print(a)
