cnt = 0

while cnt <= 3:
    try:
        n = int(input())
        if n%2 == 0:
            cnt += 1
            print(n//2)
    except EOFError:
        break