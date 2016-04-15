def singleNumber(A):
    d={}
    for i in A:
        if d.has_key(i):
            d[i]+=1
        else:
            d[i]=1
    for i in d.keys():
        if d[i]==1:
            return i
        
