#coding: utf-8

what_we_do = 3
file_name = 'sname'
sname_list = []

with open(file_name) as f:
    for i in f.readlines():
    	sname_list.append(i.strip().split(';'))

print('============================================================')

# print(sname_list.sort())

flwi = full_list_with_indexes = []

def each_el_of_list(l):
	for i, e in enumerate(l):
		k=0
		sa = []
		while k < len(e):
			sa.append(e[k])
			k = k + 1
		print(str(i) + ' -> ' + sa[0] + ' ' + sa[1])
		flwi.insert(i, sa)


each_el_of_list(sname_list)

def show_one_by_index(fl):
	x = int(input("введите индекс студента : "))
	if fl[int(x)]:
		print(' '.join(fl[x]))

def show_comprehensions(fl):
	text = 'Студент {} {}'
	x = input("введите индекс студента : ")
	if str(x).count(';') and len(x.split(';'))==2:
		#comp = x.split()
		if ( len(fl) > int(x.split(';')[0]) >= 0 ) and (( len(fl) >= int(x.split(';')[1]) > 0 )):
			for i in fl[int(x.split(';')[0]):int(x.split(';')[1])]:
				print(text.format(i[0],i[1]))
		else:
			print('срез указан не верно')
	else:
		print('введены не корректные данные')

def show_with_letter_in_name(fl):
	text = 'в имени {} студента {} {} содержится буква {}'
	x = input("введите букву искомую в имени : ")
	if x:
		for i in fl:
			if i[1].lower().count(x.lower()):
				print(text.format(i[1].strip(), i[0].strip(), i[1].strip(), x)) #strip??

def group_by_name(fl):
	uniq_names = []

	for i in fl:
		name = str(i[1].strip())
		if name not in uniq_names:
			uniq_names.append( name )
			
	return uniq_names

while True:
	what_we_do = input('0 - вывести по номеру имя и фамилию, 1 - вывести срез, 2 - найти по букве, 3 вывести сгруппировав по именам, 4 выход : ')

	if str(what_we_do) not in ['0','1','2','3','4']:
		print ('введено не корректное значение')
	else:
		what_we_do = int(what_we_do)

	if what_we_do  == 0:
		show_one_by_index(flwi)

	if what_we_do == 1:
		show_comprehensions(flwi)

	if what_we_do == 2:
		show_with_letter_in_name(flwi)

	if what_we_do == 3:
		grps = []
		uniq_names = group_by_name(flwi)

		for i, u in enumerate(uniq_names):
			print('группа имён '+ u.strip())
			for f in flwi:
				if f[1].strip() == u.strip():
					print('\t' + f[0] + ' ' + f[1])
	if what_we_do == 4:
		break


print('============================================================')