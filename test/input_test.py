print("입력해주세요")
print("=" * 50)
n = int(input())
print("=" * 50)
print(type(n))
print(n)

# 정수형으로 입력값 받기
# (값 2개 입력 받고,변수 a와 b에 저장)
a, b = map(int, input().split())  # map : 리스트 요소를 지정된 함수로 처리하는 함수
# (지금은 여러개 데이터를 한번에 다른타입으로 변형하기 위해 사용)
# 주의 mpa 함수 : 반환값은 map 객체라서 list,tuple 형 변혼해야함.

# split : 문자열을 공백 기준으로 리스트 만들어줌
# 유형 1 .split(,) 쉼표 기준 분할
# 유형 2 .split(',',1)
