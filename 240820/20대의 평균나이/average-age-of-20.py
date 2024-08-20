sum = 0
cnt = 0
while True:
    n = int(input())
    if n//10 > 2:
        break
    else:
        sum += n
        cnt += 1

print("{:.2f}".format(sum/cnt))