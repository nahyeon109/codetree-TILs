c, n = input().split()

n = int(n)

if c == 'A':
    for i in range(1, n+1):
        print(i, end=' ')
        i += 1
elif c == 'D':
    while n >= 1:
        print(n, end=' ')
        n -= 1