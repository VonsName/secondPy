# __author:  Administrator
# __date:  2018/8/17/017

import re

res = re.findall('a[bc]d', 'abcd')

print(res)

# ^表示取反
res = re.findall('[^ab]', 'acdedbs')

print(res)

# \d表示匹配数字 \D表示取反 不匹配数字
res = re.findall('[\D]', '12abds3')
print(res)
# \b匹配字符边界  例如空格 , & 等
res = re.findall('[ma\bi]', 'i!am li si')
print(res)

# () +
res = re.findall('(ad)+', 'add')
print(res)

# 分组 如果匹配不到会报错
res = re.search('(?P<name>\w{5})/(?P<num>\d{2})', '23adasa/91a2a0987')
print(res.group('name'))
print(res.group('num'))

# ?: 取消组的优先级
res = re.findall('www.(?:\w+).com', 'www.baid1u.com')
print(res)  # ['www.baid1u.com']

res = re.findall('www.(\w+).com', 'www.baid1u.com')
print(res)  # ['baid1u']

# match 匹配第一个
res = re.match('a', 'abc bca').group()
print(res)
# search 匹配第一个
res = re.search('a', 'abc bca').group()
print(res)
# findall 匹配所有
res = re.findall('a', 'abc bca')
print(res)
# split
res = re.split('ab', 'abcd')  # 先按a分割得到bcd ，然后再按b分割得到cd
print(res)

# sub

res = re.sub('\d', 'abc', 'alev123', 1)
print(res)
