a,b,c = map(int, input().split())

sum = a+b+c
avg = int(sum / 3)
result = int(sum - avg)

print(sum)
print(avg)
print(result)