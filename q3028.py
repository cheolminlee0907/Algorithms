ball = ['O','X','X']
shuffle = input()

for i in shuffle:
    if i == 'A':
        ball[0],ball[1] = ball[1],ball[0]
    elif i == 'B':
        ball[1],ball[2] = ball[2],ball[1]
    elif i == 'C':
        ball[0],ball[2] = ball[2],ball[0]

if ball.index('O') == 0:
    print(1)
elif ball.index('O') == 1:
    print(2)
else:
    print(3)
