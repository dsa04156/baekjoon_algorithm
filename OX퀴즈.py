T = int(input())
for i in range(T):
    grade = 0
    i=1
    N_list = list(map(str,input()))
    for j in range(len(N_list)):
        if N_list[j] == 'O':
            grade += i
            i+=1
        else:
            i=1
    print(grade)