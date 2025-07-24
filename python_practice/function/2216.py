# 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
negative = -3 # 변수 선언은 꼭 함수 밖에.

result = (abs(negative)) # def 로 함수 정의하지말고 기존 함수 abs 써라 result 만 선언하면됨

print(result)


# 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
empty_list = []
result = bool(empty_list)
print(result)
# bool() : 파이썬 내장함수, 값 넣으면 참, 거짓 여부 알려줌

# 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
my_list = [1, 2, 3, 4, 5]
result = sum(my_list)
print(result)

# 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
unsorted_list = ['하', '교', '캅', '의', '지', '가']

result = sorted(unsorted_list)

print(result)