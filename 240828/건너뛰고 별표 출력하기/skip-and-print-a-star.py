n = int(input())

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print('\n')

for i in range(n, 0, -1):
    for j in range(i - 1):
        print('*', end='')
    print('\n')