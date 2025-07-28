N = 9
data_1 = '123456789'
arr_1 = []

for char in data_1:
    arr_1.append(char) 
print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'

# 아래에 코드를 작성하시오.
arr_2 = data_2.split()

for num_str in arr_2: #arr_2 요소를 순회
    num_int = int(num_str) # 문자열인 num_str을 int 변환

    if num_int % 2 !=0: #num_int가 홀수 인지 확인 (직역 : 짝수가 아니면)
        print(num_int) #줄바꿈 대신 공백 추가하는 설정