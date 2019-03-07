import os #operating system
#读取档案
def read_file(filename):
	products = []
	if os.path.isfile(filename): #检查档案是否存在
		print('yeah! file is found!')
		with open(filename, 'r', encoding='utf-8') as f:
			for line in f:
				if 'products,price' in line: #当读取到products跟price的时候，自动跳到下一行
					continue
				name, price = line.strip().split(',') #.strip是忽略换行符号\n, .split(',')是用来切割，每当读取到逗号，自动分开前后的字符串，并且将读到的字符分别存入name,跟price的list当中
				products.append([name, price]) #将清单name跟清单price存入二维清单products里
		print(products)
	else:
		print('file is not found')
	return products

#让使用者输入
def input_data(products):
	while True:
		name = input('please enter the name of product: ')
		if name == 'q':
			break
		price = input('please enter the price of product: ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

#印出所有购买记录
def output_data(products):
	for p in products:
		print(p[0], 'price is: ', p[1])

#写入档案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('products,price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

products = read_file('products.csv')
products = input_data(products)
output_data(products)
write_file('products.csv', products)
