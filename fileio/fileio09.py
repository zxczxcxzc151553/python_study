import pickle

# 바이너리 파일 입력
with open(file="fileio/bin.pickle", mode= "br" ) as file_editor:
    my_data = pickle.load(file_editor)
    
print(my_data)

