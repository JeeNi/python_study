# 키보드로 거북이 조종하기
import turtle as t

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def blank():
    t.clear()

t.shape("turtle")
t.speed(0)
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")
t.listen()



# 마우스로 거북이 조종하기
import turtle as t

t.speed(0)
t.pensize(2)
t.hideturtle()
t.onscreenclick(t.goto)



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



# 타자 게임
import random
import time

w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
n = 1
print("[타자 게임] 준비되면 엔터")
input()
start = time.time()

q = random.choice(w)
while n <= 5:
    print("*문제", n)
    print(q)
    x = input()
    if q == x:
        print("통과!")
        n = n + 1
        q = random.choice(w)
    else:
        print("오타! 다시 도전!")

end = time.time()
et = end - start
et = format(et, ".2f")
print("타자 시간 : ", et, "초")



# 거북이 대포 게임
import turtle as t
import random

def turn_up():
	t.left(2)


def turn_down():
	t.right(2)


def fire():
	ang = t.heading()
	while t.ycor() > 0:
		t.forward(15)
		t.right(5)

    d = t.distance(target, 0)
    t.sety(random.randint(10, 100))
	if d < 25:
		t.color("blue")
		t.write("Good!", False, "center", ("", 15))
	else:
		t.color("red")
		t.write("Bad!", False, "center", ("",15))
		t.color("black")
		t.goto(-200, 10)
		t.setheading(ang)


t.goto(-300, 0)
t.down()
t.goto(300, 0)

target = random.randint(50, 150)

t.pensize(3)
t.color("green")
t.up()
t.goto(target -25, 2)
t.down()
t.goto(target + 25, 2)

t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")

t.listen(0)