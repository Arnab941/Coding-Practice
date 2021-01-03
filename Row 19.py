class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x:x[0])
        n=len(intervals)
        a=[]
        a.append(intervals[0])
        j=0
        for i in range(1,n):
            if intervals[i][0]<=a[j][1]:
                a[j][1]=max(intervals[i][1],a[j][1])
            else:
                a.append(intervals[i])
                j+=1
                    
        return a
