v = int(input())

t = int(input())

p = v * t - 109

k = v * t + 109

if v > 0:
    if p > 109:
        print(p % 109)
    else: 
        print(p)

elif v < 0:
    if abs(k) > 109:
        print(k % 109)
    else: 
        print(k)

elif v == 0 or t == 0:
    print(v * t)