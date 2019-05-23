# __author:  Administrator
# __date:  2018/8/9/009

# def main():
#     print('hello')
#
#
# dic = str({'1': '111'})
#
# f = open('test2', 'w')
# f.write(dic)
#
# f1 = open('test2', 'r')
# data = f1.read()
# print(data)
# # print(eval(data)['1'])
# print(foo.add(1, 2))
# if __name__ == '__main__':
#     main()
# print(__name__)


# json.dumps 序列化

# dic = {'name': 'aliex', 'age': 23}
# data = json.dumps(dic)
# f = open('json.txt', 'w')
# f.write(data)
# f.close()


# json.dump 序列化
# dic = {'name': 'aliex', 'age': 23}
# # f = open('json2.txt', 'w')
# # json.dump(dic, f)


# json.dump 反序列化
# f = open('json2.txt', 'r')
# data = json.load(f)
# print(data['name'])

# shelve
# s = shelve.open('shelve.txt')
# s['info'] = {'name': 'lisi', 'age': 23}

d = {'name': '23', 'age': 'lis'}
print(d.get('name'))
