# generator function
# yield statement
# next function

# generator function
def disp(a , b):
	yield a
	yield b
	
result = disp(10 , 20)
print(result)
print(type(result))
print()

print(".....................................................................")

print()
result = list(disp(10 , 20))
print(result)
print(type(result))
print()
print(".............................................................")

print()
x , y = disp(10 , 20)
print(x)
print(y)
print()

#..........................................................................

print("next function : ")
print()
def show(a , b):
	while a <= b:
		yield a
		a+=1
c = (show(1 , 10))
print(c)
print(next(c))
print(next(c))
print(next(c))
print()
print("using forloop : ")
for i in c:       # for loop no used karo to pan print thayeli value na ave baki ni value j forloop ma chale
	print(i)