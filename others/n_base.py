# n進数(2 <= n <= 10)
# n > 10 の時は，numを適宜変更
def nsin(n,x):
    ret = 0
    digit = 0
    num = [str(i) for i in range(n)]
    s = ''
    while x:
        ret += (x % n) * pow(n,digit)
        s = num[x%n] + s
        x //= n
        digit += 1
    return s
    #return ret

print(nsin(2,10))