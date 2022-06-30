n = int(input())
pattern = []
cnt = [0,0]

for i in range(n):
    pattern.append(list(input()))

print(pattern)

for i in range(n):
    row_cnt = 0
    col_cnt = 0
    for j in range(n):
        if pattern[i][j] == '.':
            row_cnt += 1
        else:
            row_cnt = 0
        if row_cnt == 2:
            cnt[0] += 1

        if pattern[j][i] == ".":
            col_cnt += 1
        else:
            col_cnt = 0
        if col_cnt == 2:
            cnt[1] += 1


print(cnt)
'''
for i in pattern:
    now = 0
    for j in range(len(i)):
        r_cnt = 0
        if i[j] == '.':
            now += 1
        else:
            now = 0
        if now == 2:
            r_cnt += 1
            now = 0
            cnt[0] += r_cnt
            break

pattern_T = [list(x) for x in zip(*pattern)]

for i in pattern_T:
    now = 0
    for j in range(len(i)):
        c_cnt = 0
        if i[j] == '.':
            now +=1
        else:
            now = 0
        if now == 2:
            c_cnt += 1
            now = 0
            cnt[1] += c_cnt
            break

print(f'{cnt[0]} {cnt[1]}')
'''
