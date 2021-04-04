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
import bisect
import heapq
import re
from itertools import accumulate
from itertools import permutations
from itertools import combinations
from collections import Counter
from collections import deque
from collections import defaultdict
from decimal import Decimal
inf = float('inf')
dic = defaultdict(lambda:0)

n = N()
print(n)