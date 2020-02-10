# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 1
# 입력 : n
# 출력 : 1부터 n까지의 숫자를 더한 값

def sum_n(n):
    s = 0               # 합을 계산할 변수
    for i in range(1, n + 1):   # 1부터 n까지 반복(n+1은 제외)
        s = s + i
    return s

print(sum_n(10))        # 1부터 10까지의 합(입력:10, 출력 55)
print(sum_n(100))       # 1부터 100까지의 합(입력:100, 출력 5050)


# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 2
# 입력: n
# 출력 : 1부터 n까지의 숫자를 더한 값

def sum_n(n):
    return n * (n+1) //2    # 슬래시 두 개(//)는 정수 나눗셈을 의미

print(sum_n(10))
print(sum_n(100))


# 연습 문제
def sum_n(n):
     s = 0
     for i in range(1, n + 1):
         s = s + i * i
     return s

print(sum_n(10))
print(sum_n(100))

def sum_n(n):
     s = 0
     return n * (n+1) * (2*n+1) // 6

print(sum_n(10))
print(sum_n(100))