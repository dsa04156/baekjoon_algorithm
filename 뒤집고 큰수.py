# a,b = input().split()
# a= list(a)
# b = list(b)

# a.reverse()
# b.reverse()


# a = int(a[0])*100 + int(a[1])*10 + int(a[2])
# b = int(b[0])*100 + int(b[1])*10 + int(b[2])
# if a>b:
#     print(a)
# else:
#     print(b)

a,b = map(str,input().split())
print(max(int(a[2]+a[1]+a[0]),int(b[2]+b[1]+b[0])))
