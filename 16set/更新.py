#!/usr/bin/python3

thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1,3})
print(thisset)

thisset.update([1,4],[5,6])
print(thisset)