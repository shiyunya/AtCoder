def extGCD(a,b):# returns d,x,y which ax + by = d where d = gcd(a,b)
    if b == 0:
        x = 1
        y = 0
        d = a
        return d,x,y
    else:
        d,y,x = extGCD(b,a%b)
        y -= a//b * x
        return d,x,y

def extGCD_notRecursive(a,b):# ax + by = gcd(a,b)
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    return x, y

def modinverse(a,m):# returns a_inverse on mod m
    b = m
    x,y = 1,0
    while b:
        q = a//b
        a,b = b,a-q*b
        x,y = y,x-q*y
        print(x,y)
    return x if x > 0 else x+m