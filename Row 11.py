def search(a,b,c):
    first=0
    last=c-1
    while first<=last:
        mid=(first+last)//2
        if a[mid]==b:
            return 0
        elif a[mid]<b:
            first=mid+1
        else:
            last=mid-1
    return 1

t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    ma=list(set(map(int,input().split())))
    m=len(ma)
    na=list(set(map(int,input().split())))
    n=len(na)
    m1=m
    n1=n
    if m>n:
        na.sort()
        for i1 in ma:
            f= search(na,i1,n)
            if f==1:
                n1+=1
        print(n1)
    else:
        ma.sort()
        for i2 in na:
            f= search(ma,i2,m)
            if f==1:
                m1+=1
        print(m1)
    
