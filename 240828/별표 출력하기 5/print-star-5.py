n = int(input())

for i in range(n):
    for j in range(n):
        for b in range(n):
            print('*', end='')
        print('', end=' ')
    n -= 1
    print()