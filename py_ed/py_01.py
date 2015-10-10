# coding: utf-8

import math
import os
import random

arr = []
i = 0
file_name = 'fhw_source_data.txt'

f2 = open(file_name, 'w')
f2.write('')


while i < 5:
	tmp = round(random.random() * 1000, 2)
	print ("Число номер " + str(i+1) + " " + str(tmp))
	i=i+1
	f2.write(str(tmp) + "\r\n")

f2.close()



f = open(file_name)
file_content = f.read()

print('===============================================================')

with open(file_name) as f:
    for i in f.readlines():
    	arr.append(float(i))

if len(arr) >= 5:
	t_sum = arr[0]+arr[1]
	t_sqrt_i = round(math.sqrt(arr[2]*arr[3]),2)
	print('сумма первых двух чисел ' + str(t_sum))
	print('корень от результата перемножения третьего и четвёртого числа ' + str(t_sqrt_i))
	print('максимальный результат первых двух дейтсвий ' + str(max(t_sum, t_sqrt_i)))
	print('косинус от пятого числа ' + str(round(math.cos(arr[4]),2)))
else:
	print("Недостаточное количество элементов")
