# coding: utf-8
import os

list_dir = os.listdir(".")

f2 = open("result.txt", 'w')
f2.write('')
f2.close()

for name in list_dir:
	f = open(name)
	pys = f.read().count('python') 

	if pys > 0:
		print('got ' + str(pys) + ' "python\'s" in file ' + name)
		f2 = open("ffw", 'a')
		f2.write(str(name) + str(' --> ') + str(pys) + '\r\n')
		f2.close()
