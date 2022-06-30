l = int(input())
m = input()
def hash(l,m):
    word = 'abcdefghijklmnopqrstuvwxyz'
    cnt = 0
    for i in range(l):
        cnt += (word.index(m[i])+1)*(31**i)
    return cnt%1234567891

print(hash(l,m))
