def gf(a,b,c):
    if c == 0:
        return a
    elif c == 1:
        return b
    else:
        return gf(a,b,c-1) + gf(a,b,c-2)
ans = gf(3,4,50) % 1000000007
print(ans)

def gf_iter(a,b,c):
        if c == 0:
            return a
        elif c == 1:
            return b
        else:
            for i in range(c-1):
                tmp = a + b
                a = b
                b = tmp
            return b

                

