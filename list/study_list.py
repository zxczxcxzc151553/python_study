temp = [1,2] + [3,4]
temp.append(5)
temp.remove(1)

temp = [1,1,1,1,1]
temp.remove(1)
# 모든 같은  데이터를 지우지 않은다 1개만지운다
# [1, 1, 1, 1]

def check(num):
    if num == 1:
        return False
    elif num == 2:
        return False
    else:
        return True
# print(check(1))
# print(check(1))
temp = [1,1,1,2,3]
temp = filter(check, temp)
temp = list(temp)

# temp = list(filter(check,[1,1,1,1,1]))

print(temp)


temp = [1,2,3,4,5]
temp = [[1,2],[3,4]]

# print(temp[0][0])

temp = [
    (1, 2),
    (3, 4)
]

temp = [
    {"key": "value", "name": "이름"},
    {"b": "d", "aa": "dd"}
]

# print(temp[0])
print(temp[0]["name"])
