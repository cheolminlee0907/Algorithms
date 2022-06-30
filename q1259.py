flag = True
while flag:
    a = str(input())
    if a[0] =='0':
        flag = False
    else:
        if a == a[::-1]:
            print('yes')
        else:
            print('no')
