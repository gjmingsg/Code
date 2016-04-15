def merge(A, m, B, n):
    k = m + n
    while k>0:
        k-=1
        if (n == 0 or (m > 0 and A[m-1] > B[n-1])):
            m-=1
            A[k]=A[m]
        else:
            n-=1
            A[k]=B[n]
    print "%r"% A
