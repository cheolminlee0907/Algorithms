str = 'cambridge'.upper()

word = input()

for i in word:
    if i in str:
        word = word.replace(i,'')
print(word)