n = int(input())

k = int(input())

if k % n == 0:
    print(int(k/n))
else:
    print(k//n)