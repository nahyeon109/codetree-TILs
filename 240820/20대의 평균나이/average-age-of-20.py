sum = 0
cnt = 0
while True:
    n = int(input())
    if n//10 > 2:
        print("{:.2f}".format(sum/cnt))
        break
    else:
        sum += n
        cnt += 1