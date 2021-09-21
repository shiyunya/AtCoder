# xの立っているビット数
def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555) # 2bitごと
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333) # 4bitごと
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部
    return x & 0x0000007f

for i in range(10):
    print(popcount(i))