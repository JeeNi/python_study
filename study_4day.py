#소인수분해 프로그램
x = int(input("?"))
d = 2

while d <= x:
    if x % d == 0:
        print(d)
        x = x / d
    else:
        d = d + 1



#주사위 실험 프로그램
import random

total = 10000
ev = 0

for i in range(total):
    if random.randint(1, 6) == 2:
        ev = ev + 1

print(ev / total)



#도형에서의 확률 실험 프로그램
import random

total = 1000
ev = 0

for i in range(total):
    x = random.random()
    y = random.random()

    if x * x + y * y <= 1.0:
        ev = ev + 1

print((ev / total) * 4)



#이차방정식을 푸는 프로그램
import math
import sys

print("ax2 + bx + c = 0")

a = float(input("a? "))
b = float(input("b? "))
c = float(input("c? "))

if a == 0:
    print("a = 0 : 이차방정식이 아닙니다.")
    sys.exit()

D = b*b*-4*a*c

if D > 0:
    x1 = (-b+math.sqrt(D)) / (2*a)
    x2 = (-b-math.sqrt(D)) / (2*a)
    print("2개의 해 : ", x1, x2)

if D == 0:
    x = -b / (2*a)
    print("1개의 해 : ", x)

if D < 0:
    print("해가 없습니다.")



#함수의 그래프를 그리는 프로그램
import turtle as t

#그래프를 그릴 x 좌표 범위
x_min = -5
x_max = +5

#그래프를 그릴 y 좌표 범위
y_min = -5
y_max = +5

#그래프를 그릴 간격
space = 0.1

#그릴 함수의 리스트
func_list = ["y = x*x", "y = abs(x)", "y = 0.5*x + 1"]

#좌표 설정, 거북이 속도, 선 굵기
t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.speed(0)
t.pensize(2)

#x축 그리기
t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)

#y축 그리기
t.up()
t.goto(0, y_min)
t.down()
t.goto(0, y_max)

#그래프 그리기
t.color("green")
for func in func_list:
    x = x_min
    exec(func)
    t.up()
    t.goto(x, y)
    t.down()
    while x <= x_max:
        x = x + space
        exec(func)
        t.goto(x, y)






