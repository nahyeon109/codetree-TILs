z_1, t_1 = input().split()
z_2, t_2 = input().split()
z_3, t_3 = input().split()

danger = 0

if z_1 == 'Y' and int(t_1) >= 37:
    danger += 1
if z_2 == 'Y' and int(t_2) >= 37:
    danger += 1
if z_3 == 'Y' and int(t_3) >= 37:
    danger += 1

print('E' if danger >= 2 else 'N')