t=int(input())
for i in range(t):
    m=int(input())
    ma=list(map(int,input().split()))
    ma.insert(0,ma[m-1])
    ma=ma[:m]
    for i1 in range(m):
        print(ma[i1],end=' ')
        
    print('')
