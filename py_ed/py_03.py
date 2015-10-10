# coding: utf-8

a = [1, -20, 38, 0, 40]
b = [88, -20, 48, 4, 33, 2]
i = 0

cl = min(len(a), len(b))

while i < cl-1:
	print('числа ' + str(a[i]) + ' и ' + str(b[i]))
	print('наименьшее число - ' + str(min(a[i],b[i])))
	if (abs(a[i]-b[i])<15):
		print('поздравления')
	else:
		print('не поздравления')
	print('\r\n')
	i=i+1
