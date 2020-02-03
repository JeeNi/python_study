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

import random
a = random.randint(1, 30)
b = random.randint(1, 30)

print(a, "+", b, "=")
x = input()
c = int(x)

if a + b == c:
    print("천재!")
else :
    print("바보?")



