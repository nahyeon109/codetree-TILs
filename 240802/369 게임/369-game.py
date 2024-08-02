n = int(input())

for i in range(1, n+1):
    if i%3 == 0:
        print(0, end=' ')
    else:
        result3 = (str(i).find('3'))
        result6 = (str(i).find('6'))
        result9 = (str(i).find('9'))
        if result3 != -1 or result6 != -1 or result9 != -1:
            print(0, end=' ')
        else:
            print(i, end=' ')