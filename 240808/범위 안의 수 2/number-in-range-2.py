sum = 0
cnt = 0

for i in range(10):
    n = int(input())
    if n > 0 and n <= 200:
        sum += n
        cnt += 1
    
avg = sum / cnt
avg = "{:.1f}".format(avg)

print(sum, avg)