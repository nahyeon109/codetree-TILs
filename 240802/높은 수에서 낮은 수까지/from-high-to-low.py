a, b = map(int, input().split())

if a < b:
    while b >= a:
        print(b, end=' ')
        b -= 1
elif a > b:
    while a >= b:
        print(a, end=' ')
        a -= 1