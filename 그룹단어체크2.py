n=int(input())
count=n
for i in range(n):
    s = input()
    for j in range(len(s)-1):
        if s[j] != s[j+1]:
            d = s[j+1:]
            if s[j] in d:
                count -=1
                break
print(count)