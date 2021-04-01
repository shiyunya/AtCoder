def N():
    return int(input())
def L():
    return list(map(int,input().split()))
def NL(n):
    return [list(map(int,input().split())) for i in range(n)]
mod = pow(10,9)+7
#import numpy as np
import sys
sys.setrecursionlimit(2147483647)
import math
from itertools import accumulate
from itertools import permutations
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import heapq
import re
inf = float('inf')
dic = defaultdict(list)#lambda:0)
#from decimal import Decimal
from itertools import combinations

n = N()

mm = [[inf,-inf] for i in range(n+1)]
cs = set()
for i in range(n):
    x,c = L()
    mm[c][0] = min(mm[c][0],x)
    mm[c][1] = max(mm[c][1],x)
    cs.add(c)
dp = [[0,0]]
cs = sorted(list(cs))
p = 0
mm[0][0] = mm[0][1] = 0
#print(mm[:4])
for i in range(len(cs)):
    d = min(dp[i][1] + abs(mm[p][1] - mm[cs[i]][1]) ,dp[i][0] + abs(mm[p][0] - mm[cs[i]][1])) + abs(mm[cs[i]][1] - mm[cs[i]][0])
    u = min(dp[i][1] + abs(mm[p][1] - mm[cs[i]][0]) ,dp[i][0] + abs(mm[p][0] - mm[cs[i]][0])) + abs(mm[cs[i]][1] - mm[cs[i]][0])
    p = cs[i]
    #print(p)
    dp.append([d,u])
#print(dp)
#print(dp[i],mm[p])
print(min(dp[-1][1] + abs(mm[p][1]) , dp[-1][0] + abs(mm[p][0])))
