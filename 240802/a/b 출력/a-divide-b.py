a, b =map(int, input().split())

for i in range(21):
    m  = a // b
    n = a % b
    a = n * 10

    # print(m, end='')
    if m != 0:
        print('.', end='')
    print(m, end='')