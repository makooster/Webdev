x = int(input())
d = int(input())


cnt = 0

while x > 0:

    n = x % 10
    
    if n == d:
        cnt += 1
    
    x //= 10

print(cnt)