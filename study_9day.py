# 두 번 이상 나온 이름 찾기
# 입력: 이름이 n개 들어 있는 리스트
# 출력: 이름 n개 중 반복되는 이름의 집합

def find_same_name(a):
    n = len(a)                  # 리스트의 자료 개수를 n에 저장
    result = set()              # 결과를 저장할 빈 집합
    for i in range(0, n-1):     # 0부터 n-2까지 반복
        for j in range(i+1, n):     # i+1 부터 n-1까지 반복
            if a[i] == a[j]:        # 이름이 같으면
                result.add(a[i])    #찾은 이름을 result에 추가
    return result

name = ["Tom", "Jerry", "Mike", "Tom"]  # 대소문자 유의: 파이썬은 대소문자를 구분함
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name))
print(find_same_name(name2))


# 연습 문제

# n명에서 두 명을 뽑아 짝으로 만드는 모든 경우를 찾는 알고리즘
# 입력: n명의 이름이 들어 있는 리스트
# 출력: 두 명을 뽑아 만들 수 있는 모든 짝

def print_pairs(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(a[i], "-", a[j])

name = ["Tom", "Jerry", "Mike"]
print_pairs(name)
print()

name2 = ["Tom", "Jerry", "Mike", "John"]
print_pairs(name2)