n = int(input())

sum = 0
cnt = 0
for i in range(n):
    m = int(input())
    sum += m
    cnt += 1

avg = "{:.1f}".format(sum / cnt)

print(sum, avg)