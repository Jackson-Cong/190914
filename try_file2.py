# -*- coding: UTF-8 -*-

filename = 'test.txt'
f = open(filename, 'r')

print('第一个文件内容如下：')
texts = f.read()
print(texts)


f.close()
