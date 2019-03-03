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
print(products)