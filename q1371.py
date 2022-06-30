alphabet = 'abcdefghijklmnopqrstuvwxyz'
import sys

str1 = sys.stdin.read().replace('\n', '').replace(' ','')

dic = {}
for chr in alphabet:
       cnt = str1.count(chr)
       dic[chr] = cnt

num = max(dic.values())
ret = ''
for key, value in dic.items():
    if value == num:
        ret+=key
print(ret)
