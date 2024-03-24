a = int(input())

cnt = 0

while a > 0:
    n = a % 10
    cnt += n
    a //= 10

print(cnt)


