for _ in range(int(input())):
    strr=input()
    l1=[int(i) for i in strr]
    count=0 
    l=[]
    for i in range(len(strr)):
        x=l1[i]
        while count<x:   
            l.append('(')
            count+=1
        while count>x:
            l.append(')')
            count-=1
        l.append(x)
    while count:
        l.append(')')
        count-=1
    my_string=''.join(str(key) for key in l)
    print('Case #{}: {}'.format(_+1,my_string)) 
