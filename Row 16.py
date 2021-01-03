class Solution:
    def findDuplicate(self, nums):
        n=len(nums)
        check=[0]*(n+1)
        for i in nums:
            check[i]+=1
            if check[i]==2:
                return(i)
