a = int(input())
for j in range(a):
    ox = list(input())
    point = 0
    k = 1
    for i in range(len(ox)):
        if ox[i] == 'O':
            point += k
            k+=1
        else:
            k = 1
    print(point)
