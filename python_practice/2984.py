password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
# 아래에 코드를 작성하시오.

life_start = password.find("life") 
#단어 life 가 시작하는 첫번째 문자열 위치 찾아서 선언
#_start 붙는 이유: 정확한 위치의 단어 참조학 위함임.
is_start = password.find("is")
short_start = password.find("short")
## you부터는 뒤집어서 출력임. 슬라이싱 후 뒤집기
uoy_start = password.find("uoy")
deen_start = password.find("deen")
python_start = password.find("python")
## 단어 첫번째 문자에 해당하는 위치 찾았으니까 슬라이싱 시작

life = password[life_start : life_start + 4]
is_word = password[is_start : is_start + 2]
# 파이썬 기존 변수에 is 있음. 겹치지 않게 피해서 _word 붙여줌
short = password[uoy_start : is_start + 5]
python = password[python_start : python_start + 6]

# 뒤집힌 문자열 슬라이싱 후 뒤집기
uoy = password[uoy_start : uoy_start + 3]
you = uoy[::-1] # 뒤집는 표현식을 선언하면 됨

deen = password[deen_start : deen_start + 4]
need = deen[::-1]

# 출력
print(f'{life} {is_word} short, {you} {need} "{python}".')

#문자열 내부이므로 공백 인식, 문자열 조합이니까 + 등 연산 필요 x
# 글자 뒤집기? [::-1]
# 문자열 기니까 .find() 사용해서 단어 첫 알파벳 찾기


