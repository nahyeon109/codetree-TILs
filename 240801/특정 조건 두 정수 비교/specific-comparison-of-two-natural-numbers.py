a, b = map(int, input().split())

first = 0;
second = 0;
if a < b:
    first = 1
else:
    first = 0

if a == b:
    second = 1
else:
    second = 0

print(first, second)