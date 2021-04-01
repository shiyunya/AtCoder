mod = pow(10,9) + 7

# pが素数のとき，a^(p-1) ~ 1 (mod p) → aの逆数は a^(p-2)
def modiv(a,b):# a/b (on mod)
    return a*pow(b,mod-2,mod)%mod
print(modiv(15,3))