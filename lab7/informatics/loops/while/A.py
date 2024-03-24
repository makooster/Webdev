a = int(input())

# for i in range(1, a):
#     if int(i**0.5) ** 2 == i:
#         print(i)
i = 1

while i <= a:
    if int(i**0.5) ** 2 == i:
        print(i)
    i += 1