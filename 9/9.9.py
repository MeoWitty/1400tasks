max_ball = 0
pobeditel_ball = 0
for sportsmen in range(8):
    for vid in range(5):
        ball = int(input())
        if ball > max_ball:
            max_ball = ball
    if sportsmen == 0:
        pobeditel_ball = ball
    elif ball > pobeditel_ball:
        pobeditel_ball = ball
print(max_ball)
print(pobeditel_ball)