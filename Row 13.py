def maxSubArraySum(a,size):
    msf=-(10**7)-1
    mrn=0
    for i in range(size):
        mrn=mrn+a[i]
        if a[i]>mrn:
            mrn=a[i]
           
        msf=max(msf,mrn)
        
    return msf
