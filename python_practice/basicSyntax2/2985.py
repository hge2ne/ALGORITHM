# 아래에 코드를 작성하시오.

zero_list = [0] 
many_zero_list = ( zero_list * 25000 ) #list는 인덱스있음 
numbers = range(1,11)
length = len(many_zero_list)

print(zero_list)
print(length)
print(list(numbers))
print(list(numbers[3:])) #현재 list(인덱스o, 슬라이스 가능) 
