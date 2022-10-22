

from symbol import term


temp = "가나다"
# 문자열은 요소를 번호로 가져올수있다.
# temp[0]= '가'

# temp[0] = "라"
#  실행시 에러발생(TypeError: 'str' object does not support item assignment)
#  ->문자열은 불변이라 요소를 변경할수 없다.

temp = "라"
# 실행됨 변수에 다른 문자열을 넣을 수는 있다.

del temp
# 출력시 에러발생(NameError: name 'temp' is not defined)
# 변수를 삭제한다.

temp = "가나다"
temp = "라"
temp = "가나다"
# 문자열, 숫자는 메모리 어딘가에 저장되어 다시 불러와진다.
# id(temp)=3056975602736
# id(temp)=3056975512800
# id(temp)=3056975602736

temp = "가나다\n라마바"
# 문자열을 여러줄로 출력하고 싶다면 \n
# 가나다
# 라마바

# temp ="""
# 가나다
# 마바사"""
temp = '그가 말했다.''"안녕하세요."'
# 쌍따옴표를 문자열안에 넣고싶을때 홀따옴표로 감싼다
# 그가말했다. "안녕하세요"

temp = "나는 생각했다. '잠온다'"
# 나는 생각했다. '잠온다'

temp = """그가 말했다. "안녕하세요" 나는 생각했다. '잠온다' \n"""
# 쌍따옴표를 홀따옴표로 모두 넣을 경우""" 또는 '''를 사용
# 그가 말했다. "안녕하세요" 나는 생각했다. '잠온다' "

print(f"{temp}")

temp = temp[0:3]
# 시퀀스는 대괄호를 이용해서 잘라낼 수 있다.
# temp '그가'

temp = "가나다라"
temp = temp[-4]
# # temp='가'

temp = "가나다라"
temp = temp[1:]
# 1번부터 끝까지

temp = "1234"
temp = temp[5:100]
# temp= ''

# for item in temp:
#     print(item)
# 문자열은 반복가능

temp = ("가나" 
        "다")
# 

# temp = len(temp)
# 문자열의 길이를 알고 싶으면 len 함수사용

temp = temp[len(temp) - 1]
# temp='다'
# 역순출력

temp = "가나다라"

temp = f"한글은 {temp}"
# f"""" f'' 를 이용해서 변수를 문자열에 입력가능
# temp='한글은 가나다라'

temp = "가나다라"
temp = "한글은" + temp
# temp='한글은가나다라'

temp = "가나다라"
temp = "한글은 %s" % temp
# temp='한글은 가나다라'

temp = "가나다라"
temp = temp.startswith('가나')
# temp=True

temp = "가나다라"
temp = temp.index("가")
#해당 문자열의 요소번호를 리턴
# temp=0

temp = "1"
temp = temp.zfil(2)
# 빈 자리수를 0으로 채움

temp = "1"
temp = temp.rjust(5, "1")


print(f"{temp=}")


