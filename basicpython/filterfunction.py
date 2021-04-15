a = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]

def high_marks(n):
	if n>=50:
		return True
		
result = filter(high_marks , a) # a = 10 (not return) , second time a = 20 (not return) , 5th time     													   a = 50 (return 50 then store variable)
print(result) #print object to result not value
for i in result:
	print(i)
	
	
#..................................................................................

print()
a = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]

def high_marks(n):
	if n>=50:
		return True
		
result = list(filter(high_marks , a))
print(result)  #print list becouse object convert to list
for i in result:
	print(i)
	
#.........................................................................

print()
print("using lambda function : ")
a = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
		
result = list(filter(lambda n : (n >= 50) , a))  #lambda and def function work is same 

print(result) #print object to result not value
for i in result:
	print(i)
