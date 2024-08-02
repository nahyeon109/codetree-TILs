n = int(input())
nums = [int(input()) for i in range(n)]

for j in nums:
    if j%3 == 0 and j%2 == 1:
        print(j)