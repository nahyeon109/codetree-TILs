a, b = map(int, input().split())
sum = 0
temp = 0

if a > b:
    before = b
    after = a
elif b > a:
    before = a
    after = b
else:
    before, after = a

for i in range(before, after+1):
    if i%5 == 0:
        sum += i

print(sum)