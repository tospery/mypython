#!/usr/bin/python3

thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset)
# thisset.remove("Facebook") # 不存在会发生错误

thisset.discard("Facebook") # 不存在不会发生错误
print(thisset)

thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()
print(x)