# plate
num = int(input())
plate_ls = []
for i in range(num):
    plt = input()
    plate_ls.append(plt)

for plate in plate_ls:
    ls = plate.split('-')
    alphabet = ['A','B','C','D',"E",'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    char = ls[0]
    pnt = 0
    i = 2
    for a in char:
        pnt += alphabet.index(a)*(26**i)
        i -=1
    if (abs(pnt-int(ls[1]))) <= 100:
        print('nice')
    else:
        print("not nice")

