class product:
    def __init__(self,price,id1,quantity):
        self.price=price
        self.id1=id1
        self.quantity=quantity
class inventory:
	item={}
	quant={}
	def __init__(self):
		self.item={}
		self.quant={}
	def add(self,product):
		self.item[product.id1]=product.price
		self.quant[product.id1]=product.quantity
	def sum(self):
		sum=0
		for num in self.item:
			sum+=self.item[num]*self.quant[num]
		return sum

inventory1=inventory()
num=int(input("Enter number of products\n"))
for i in range(num):
	a=int(input("enter the price of price\n"))
	b=int(input("enter the id of product\n"))
	c=int(input("enter the quantity of product\n"))
	inventory1.add(product(a,b,c))
print("the sum of all product is \n")
total=inventory1.sum()
print(total)