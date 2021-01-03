t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    a=set(list(map(int,input().split())))
    b=set(list(map(int,input().split())))
    c=a.union(b)
    print(len(list(c)))
