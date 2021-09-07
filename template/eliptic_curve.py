inf = float('inf')
mod = 7
a = 3
b = 2
O = (inf, inf) #Additive identity element

def e(x) : #eliptic curve
    return ((x ** 3) + (x * a) + b) % mod

def addition(p, q):
    if p == q:
        return twice(p)
    if p[0] == q[0] and p[1] == - q[1] % mod:
        return O
    if p == O:
        return q
    if q == O:
        return q

    s = (q[1] - p[1]) * ((q[0] - p[0]) ** (mod - 2))
    s %= mod
    x = s ** 2 - p[0] - q[0]
    x %= mod
    y = -(s * (x - p[0]) + p[1])
    y %= mod
    return (x, y)

def twice(p):
    s = (3 * (p[0] ** 2) + a) * ((p[1] * 2) ** (mod - 2))
    s %= mod
    x = s ** 2 - p[0] - p[0]
    x %= mod
    y = -(s * (x - p[0]) + p[1])
    y %= mod
    return (x, y)

xy = []

for x in range(mod):
    for y in range(mod):
        yy = (y ** 2) % mod
        if e(x) == yy:
            xy.append((x, y))
xy.append(O)

print(xy, len(xy))

p = xy[0]
ps = [p]

print(" ","P = ", p)
for i in range(2, 9 + 1):
    ps.append(addition(p, ps[i - 1 - 1]))
    print(i, "P = ", ps[i - 1])

print("2P + 2P =", addition(ps[1],ps[1]))