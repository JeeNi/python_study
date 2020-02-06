# number = 15
# if number % 3 == 0:
#     print('{}은 3의 배수입니다.'.format((number)))
# print
#
# print("7+4 = ", 7+4)
# print("7*4 = ", 7*4)
# print("7/4 = ", 7/4)
# print("2**3 = ", 2**3)
# print("5%3 = ", 5%3)
#
# for x in range(10):
#     print("Hello")
#
# for x in range(3):
#     print(100)
#     print(200)
# print(300)

# import random
# a = random.randint(1, 30)
# b = random.randint(1, 30)
#
# print(a, "+", b, "=")
# x = input()
# c = int(x)
#
# if a + b == c:
#     print("천재!")
# else :
#     print("바보?")

# print("[1-10]")
# x = 1
#
# while x <= 10: # 명령문 뒤에 '무엇'에 해당하는 조건을 적는다. 판단 조건이 True인 동안
#     print(x)   # 반족 실행할 내용 부분을 반복한다.
#     x = x + 1
#
# s = 0
# x = 1
# while x <= 10:
#     s = s + x
#     print("x: ", x, " sum : ", s)
#     x = x + 1

# import random
# n= random.randint(1, 30)
# while True:
#     x = input("맞혀 보세요?")
#     g = int(x)
#     if g == n:
#         print("정답")
#         break
#     if g < n:
#         print("너무 작아요.")
#     if g > n:
#         print("너무 커요.")

def hello():                    # '인자'는 필요없으면 생략가능
    print("Hello Python!")
    #return 함수의 결괏값          # 결괏값이 없을 때는 생략

hello()
hello()
hello()

def hello2(name):
    print("Hello", name)
hello2("Justin")
hello2("John")
hello2("JeeNi")

def square(a):
    c = a * a
    return c

def triangle(a, h):
    c = a * h / 2
    c = a * h / 2
    return c

s1 = 4
s2 = square(s1)
print(s1, s2)
print(triangle(3, 4))

def sum_func(n):
    s = 0
    for x in range(1, n+1):
        s = s + x
    return  s
print(sum_func(10))
print(sum_func(100))

def factorial(n):
    fact = 1
    for x in range(1, n+1):
        fact = fact * x
    return fact
print(factorial(5))
print(factorial(10))

import turtle as t
def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)
def polyfon2(n, a):
    for x in range(n):
        t.forward(a)
        t.left(360/n)

polygon(3)
polygon(5)

t.up()
t.forward(100)
t.down()

polyfon2(3, 50)
polyfon2(5, 50)

import turtle as t
t.bgcolor("black")
t.speed(0)

for x in range(200):
    if x %3 == 0:
        t.color("red")
    if x %3 == 1:
        t.color("yellow")
    if x %3 == 2:
        t.color("blue")
    t.forward(x * 2)
    t.left(119)