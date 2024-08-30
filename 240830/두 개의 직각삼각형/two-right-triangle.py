n = int(input())

for i in range(n):
    for j in range(2):
        if j == 0:
            for _ in range(n - i):
                print('*', end='')
            for _ in range(i):
                print(' ', end='')
        else:
            for _ in range(i):
                print(' ', end='')
            for _ in range(n - i):
                print('*', end='')
    print()