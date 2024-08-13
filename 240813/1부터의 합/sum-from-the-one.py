n = int(input())

m = 0
for i in range(1, 101):
    m += i
    if(m >= n):
        print(i)
        break