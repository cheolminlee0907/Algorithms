
ls = ['c=','c-','dz=','d-','nj','lj','s=','z=']

word = input()

for i in ls:
    exist = word.count(i)
    if exist != 0:
        word = word.replace(i,'*')

print(len(word))

