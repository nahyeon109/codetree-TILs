satsified = False

n = int(input())
for i in range(n+1, 2):
    if n%i == 0:
        satsified = True

if satsified == True:
    print('N')
else:
    print('C')