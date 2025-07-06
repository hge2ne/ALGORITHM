n = int(input())
num_list = list(map(int, input().split()))

# List 정렬
# list는 index가 0부터 시작 ex) [a,b,c,d,e] => c의 index 는 2
num_list.sort()

# print(num_list)
# // -> 몫 구하기  / -> 나누기(소수 나올 수 있음) ex) 3/2 == 1.5(double)
print(num_list[n // 2])
