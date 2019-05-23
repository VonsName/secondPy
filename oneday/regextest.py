# __author:  Administrator
# __date:  2019/5/23/023

import re

# . -> 匹配除换行符"\n"以外所有的字符
# re.S re.DOTALL 这2种模式下能匹配所有的
# \ -> 转义字符
# re.findall() 找所有
res = re.findall(".", "n\n", re.DOTALL)

# [] -> a[bcd]e {abe ace ade}
res1 = re.findall("a[bcd]+e", "abcdde")

# | -> 表示或的意思

res2 = re.findall("abe|ace|res", "res")

# \d 数字(0-9) \D 非数字 相当于^\d
# \s 空白字符(空格\r\n\f\v) \S非空白字符 相当于^\s
# \w 字母以及数字(A-Za-z0-9) \W 非字母数字 相当于^\w
# * 0次或多次
# + 1次或多次 贪婪匹配
# ? 0次或1次  非贪婪匹配
# {m} m次

print(res)
print(res1)
print(res2)

# re.sub() 替换
strs = "q1w3er2o"
res3 = re.sub("\D", "_", strs)
print(res3)

# re.search() 找一个

res3 = re.search("\d", strs)
print(res3)

# re.match() 从头找一个,如果开头没有,就直接返回
strs1 = "q1w3er2o"
res3 = re.match("\d", strs1)
print(res3)

# re.compile() 编译
c = re.compile("\d")
res3 = c.match(strs1)
print(res3)

res3 = re.findall(r"a\\nb", "a\\nb")
print(res3)
