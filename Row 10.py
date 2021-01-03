# expecting unit space separated inputs here

a=list(map(int,input().split()))
n=len(a)
i=0
j=n-1
k=0
l=0
while i<j:
    if a[i]<=0:
        i+=1
    else:
        k=-1
    if a[j]>=0:
        j-=1
    else:
        l=-1
        
    if k==-1 and l==-1:
        a[i],a[j]=a[j],a[i]
        k=0
        l=0
        
print(a)