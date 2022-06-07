v = input()
s= v.lower()
alpha = 'abcdefghijklmnopqrstuvwxyz'

d=[]
for i in alpha:
    d.append(s.count(i))
m = max(d)
if d.count(m)>1:
    print('?')
else:
    c = d.index(m)
    print(alpha[c].upper())
