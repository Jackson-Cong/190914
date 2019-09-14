# -*- coding: UTF-8 -*-

filename = 'test.txt'
f = open(filename, 'a') #append model

for i in range(6):
    append_data = '\nPlease append this row.'
    f.write(append_data)

f.close()
