#!/usr/bin/python3

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # 这里演示的是去重功能
print('orange' in basket) # 快速判断元素是否在集合内
print('crabgrass' in basket)
# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b) # 集合a中包含而集合b中不包含的元素
print(a | b) # 集合a或b中包含的所有元素
print(a & b) # 集合a和b中都包含了的元素
print(a ^ b) # 不同时包含于a和b的元素