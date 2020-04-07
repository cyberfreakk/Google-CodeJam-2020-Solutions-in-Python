for _ in range(int(input())):
    N=int(input())
    matrix=[list(map(int,input().split())) for i in range(N)]
    for i in range (N):
        matrix[i].append(i)
    imposs=0    
    l=[0,0]
    to=0
    other=1
    ans=[0 for i in range(N)]
    matrix.sort()
    for idx in range(N):
        idd=matrix[idx][2]
        if l[to]<=matrix[idx][0]:
            ans[idd]='C'
            l[to]=matrix[idx][1]
        elif l[other]<=matrix[idx][0]:
            ans[idd]="J"
            l[other]=matrix[idx][1]
        else:
            imposs=1
    my_list=''.join([str(elem) for elem in ans])
    if imposs==1:
        print('Case #{}: {}'.format(_+1,"IMPOSSIBLE"))
    else:
        print('Case #{}: {}'.format(_+1,my_list))
