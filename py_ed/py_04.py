# coding: utf-8


def sum(x,y):
	return float(x+y)

def diff(x,y):
	return x-y

def div(x,y):
	if (y!=0):
		return(x/y)
	else:
		return('деление на ноль')

def mul(x,y):
	return(x*y)

print("Для выхода в поле \"операция\" введи 0")
while True:
	x = float(input("введите число X:"))
	y = float(input("введите число Y:"))
	d = str(raw_input("операция (/,*,+,-):"))
	if (d == '0'):
		break
	if d=='+':
		print(sum(x,y))
	elif d=='-':
		print(diff(x,y))
	elif d=='*':
		print(mul(x,y))
	elif d=='/':
		print(div(x,y))
	else:
		print("данное действие не предусмотрено")
