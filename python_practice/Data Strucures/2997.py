def restructure_word(word, arr): #인자 순서왜 이럴까?
    for char in word: # word 안의 문자열 의 char 순회해야함
        if char.isdecimal(): # 문자열에서 숫자 찾기
            for _ in range(int(char)): #문자열 안 문자 개수만큼 반복
                arr.pop()
        else: 
            arr.remove(char)
    return arr
            
# 직역 : word 문자열 char 순회할거임. 
# 만약 문자열에 숫자가 포함된다면, 문자개수만큼 이하 조건 순회할거야
# 그리고 숫자를 끝에서 하나씩 제거함. 순회횟수만큼
# 만약 숫자가 문자열에 없으면 

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = [] #list임

arr.extend(original_word) #리스트 안에 있는 문자를 하나씩 풀어서 값을 합침
print(arr)

result = restructure_word(word, arr)

print(result) # 리스트
print(''.join(result)) # 리스트를 다시 문자열로 합침
