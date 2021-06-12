import bisect
inf = float('inf')

def LIS(seq):
    n = len(seq)
    lis = [inf] * n
    ret = [0] * n
 
    for i in range(n):
        idx = bisect.bisect_left(lis, seq[i])
        lis[idx] = min(lis[idx], seq[i])
        ret[i] = idx + 1
    
    return ret
    return n - lis.count(inf) #longest increasing subsequence

seq = [2, 5, 6, 2, 1, 5, 7, 3, 10, 5, 9]

print(LIS(seq))