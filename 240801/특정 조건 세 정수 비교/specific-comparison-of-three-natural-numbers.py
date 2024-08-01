a,b,c = map(int, input().split())

first = 0
second = 0
if a <= b and a <= c:
    first = 1
else:
    first = 0

if a == b == c:
    second = 1
else:
    second = 0

print(first, second)