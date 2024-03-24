n = input()

d = 0

for i in range(len(n)):

    x = int(n[-(i + 1)])

    d += x * (2**i)

print(d)