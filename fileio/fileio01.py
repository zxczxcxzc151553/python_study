# open을 이용해서 파일을 생성하고 파일에디터를 호출한다.
file_editor = open(file="test.txt", mode="a", encoding="utf-8")

# write를 이용해서 내용을 입력한다.
file_editor.write("\n반갑습니다.")

# 파일에디터를 닫는다.
file_editor.close()