#......................................................................................

def disp(a):
	print("disp function " + a())
	
def show():
	return "show function"
	
disp(show)
print()

#2....................................................................................
def disp(a):
	return "disp function " + a()
	
def show():
	return "show function"
	
a = disp(show)
print(a)
print()

#3....................................................................................
def disp():
	def show():
		return "show function "
	print("disp function")
	return show
	
a = disp()
print(a())
print()

#4...................................................................................

def disp(a):
	print( "disp function ")
	return a 
	
def show():
	return "show function"
	
a = disp(show)
print(a())
