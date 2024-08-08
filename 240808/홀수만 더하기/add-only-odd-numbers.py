n = int(input())

sum = 0
for i in range(n):
    m = int(input())
    if m%3 == 0 and m%2 != 0:
        sum += m

print(sum)