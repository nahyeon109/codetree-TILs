a, b = map(int, input().split())

cnt = 0
sum = 0
for i in range(a, b+1):
    if i%5 == 0 or i%7 == 0:
       cnt += 1
       sum += i

avg = sum / cnt
avg = '{:.1f}'.format(avg)

print(sum, avg)