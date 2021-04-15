def disp ():
	def show():
		print("show function")
	print("disp function")
	show()
	
disp()
print()

#..............................................................................
print("new nested function : ")
def disp ():
	def show():
		return "show function"
	result = show() + "disp function"
	add = show() , "disp function"
	return result , add
	
a , b = disp()
print("a = " , a)
print("b = " , b)
print()
#...............................................................................
print("new nested function :")
def add(x , y):
	def sub(p , q):
		r = p - q
		print(r)
	z = x + y
	print(z)
	print("given subtrect value : ")
	a = int(input("enter value of a : "))
	b = int(input("enter value of b : "))
	sub(a , b)

print("addition value :")
a = int(input("enter value of a : "))
b = int(input("enter value of b : "))
add(a , b)	
		