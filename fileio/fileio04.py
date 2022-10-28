#  파일을 읽기모드로 연다. 파일이 없으면 에러가 발생한다.
file_editor = open(file="test.txt", mode="r", encoding="utf-8")

# 파일을 읽는다.
text_list = file_editor.readlines()

# 파일에디터를 닫는다.
file_editor.close()

print(text_list)

# ['안녕하세요.\n', '반갑습니다.']