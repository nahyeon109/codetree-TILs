n = int(input())
cnt = 0
while True:
    if n == 1:
        break
    else:
        cnt += 1
        if n%2 == 0:
            n = n/2
        elif n%2 == 1:
            n = (n*3) + 1

print(cnt)