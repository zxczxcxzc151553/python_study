# try:
#     temp = "가나다"
#     temp[0] = "아"
# except exception as e:
#     print(e)
#     # e.with_traceback
#     # print("에러발생")
# finally:
#     print("마지막으로 할일을 하겠습니까?")
    
# print("넘어왔습니다.")
# temp = 1

# def my_func():
#     global temp
#     temp = 3
#     return temp

# print(my_func())
# print(temp)

# raise Exception("내가 만든 에러")

# parameter
# def my_func(num):
    # print(num)

# my_func(12)
# # argument, 인자, 인수

# my_func = lambda num : print(num)



# my_func(12)

# temp = list(filter(lambda num : num != 1, {1,2,3,1}))

# print(temp)

# def my_func():
#     while True:
#     yield 1
#     yield 2
#     yield 3
#     yield 5
#     yield 4
    
# my_yiele_data = my_func()

def check_str(data: str):
    return data.endswith("마")

print(check_str("가나다"))
