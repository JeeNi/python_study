# 키보드로 거북이 조종하기
# import turtle as t
#
# def turn_right():
#     t.setheading(0)
#     t.forward(10)
#
# def turn_up():
#     t.setheading(90)
#     t.forward(10)
#
# def turn_left():
#     t.setheading(180)
#     t.forward(10)
#
# def turn_down():
#     t.setheading(270)
#     t.forward(10)
#
# def blank():
#     t.clear()
#
# t.shape("turtle")
# t.speed(0)
# t.onkeypress(turn_right, "Right")
# t.onkeypress(turn_up, "Up")
# t.onkeypress(turn_left, "Left")
# t.onkeypress(turn_down, "Down")
# t.onkeypress(blank, "Escape")
# t.listen()



# 마우스로 거북이 조종하기
# import turtle as t
#
# t.speed(0)
# t.pensize(2)
# t.hideturtle()
# t.onscreenclick(t.goto)



# 계산 맞히기 게임
import random

def make_question():
    a = random.randint(1, 40)
    b = random.randint(1, 20)
    op = random.randint(1, 3)

    q = str(a)

    if op == 1:
        q = q + "+"
    if op == 2:
        q = q + "-"
    if op == 3:
        q = q + "*"

    q = q + str(b)

    return q

sc1 = 0
sc2 = 0

for x in range(5):
    q = make_question()
    print(q)
    ans = input("=")
    r = int(ans)

if eval(q) == r:
    print("정답!")
    sc1 = sc1 + 1
else:
    print("오답!")
    sc2 = sc2 + 1

print("정답 : ", sc1, "오답 : ", sc2)
if sc2 == 0:
    print("당신은 천재입니다!")