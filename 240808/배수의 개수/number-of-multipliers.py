cnt_third = 0
cnt_fifth = 0 

for i in range(10):
    n = int(input())
    if n%3 == 0:
        cnt_third += 1
    if n%5 == 0:
        cnt_fifth += 1

print(cnt_third, cnt_fifth)