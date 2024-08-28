a, b = map(int, input().split())

satisfied = False

for i in range(a, b):
    if 1920%i == 0 and 2880%1 == 0:
        satisfied = True
        break
    

if satisfied == True:
    print(1)
else:
    print(0)