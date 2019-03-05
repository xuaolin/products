with open('products.csv', 'r') as f:
	for line in f:
		s = line.strip().split(',')
		name = s[0]
		price = s[1]
		print(s)
		# advanced way for line 4-6
		# name, price = line.strip().split(',')
		# products.append([name, price])
		# print(products)
products = []
while True:
	name = input('please enter the name of the product:')
	if name == 'q':
		break
	price = input('please enter the price:')
	p=[]
	p.append(name)
	p.append(price)
	products.append(p)
	#advanced way for line 7 - 10
	#products.append(p[name, price])
print(products)

for p in products:
	print(p[0], 'price is' , p[1])

with open('products.csv', 'w') as f:
	f.write('products,price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')