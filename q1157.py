word = input('Put in word: ').upper()

word_list = list(set(word))
cnt = []
for i in word_list:
    cnt.append(word.count(i))

if cnt.count(max(cnt))>=2:
        print('?')
else:
        loc = cnt.index(max(cnt))
        print(word_list[loc])

