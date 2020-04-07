for _ in range(int(input())):
    count=0
    c=0
    k=0
    N=int(input())
    matrix=[list(map(int,input().split())) for i in range(N)]
    for i in range(N):
        count+=matrix[i][i]
    for i in range(N):
        col=[row[i] for row in matrix]
        if(len(col)!=len(set(col))):
            c+=1
        if(len(matrix[i])!=len(set(matrix[i]))):
            k+=1
    print('Case #{}: {} {} {}'.format(_+1,count,k,c))
