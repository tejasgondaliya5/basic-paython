a = [10 , 20 , 30 , 40 , 50 , 60 , 70]

def inc(n):
	return n + 2
	
x = map(inc , a)
print(x)
print(type(x))
print()

print("***************************************")

print()
a = [10 , 20 , 30 , 40 , 50 , 60 , 70]

def inc(n):
	return n + 2
	
x = list(map(inc , a))
print(type(x))
print(a)
print(x)
for i in x:
	print(i)
print()

print("......................................................................")

print()
a = [10 , 20 , 30 , 40 , 50 , 60 , 70]
	
x = list(map(lambda n : (n+2) , a))

print(type(x))
print(a)
print(x)
for i in x:
	print(i)
print()

print("......................................................................")

print()
a = [10 , 20 , 30 , 40 , 50 , 60 , 70]
b = [1 , 2 , 3 , 4 , 5 , 6 , 7]
x = list(map(lambda n,m : (n+m) , a,b))

print(type(x))
print(a)
print(b)
print()

print(x)
for i in x:
	print(i)
print()
