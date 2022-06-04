def solve(a):
    n = len(a)
    ans=0
    for i in range(n):
        ans += a[i]
    return ans

print(solve([1,2,3,4,5,6]))