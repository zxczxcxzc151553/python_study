#파일 삭제
import os

# 1번 방법
# if os.path.exists("test.txt"):
#     os.remove("fileio/test.txt")

# 2번방법
# os.system("rm test.txt")

# 폴더 및 파일삭제 
os.system("rm -rf fileio/")
