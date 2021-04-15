a = int(input("1. how many row print : "))
for i in range(a):
	for j in range(i):
		print("*",end=" ")
	print()

	
a = int(input("2. how many row print : "))
for i in range(a):
	for j in range(a-i-1):
		print("*",end=" ")
	print()


	
a = int(input("3. how many row print : "))
for i in range(a):
	for j in range(i+1):
		print(j,end=" ")
	print()

a = int(input("4. how many row print : "))
for i in range(a):
	for j in range(a-i):
		print(j,end=" ")
	print()
	
	
a = int(input("5. how many row print : "))
for i in range(a+1):
	for j in range(i):
		print(i,end=" ")
	print()

a = int(input("6. how many row print : "))
for i in range(a,0,-1):
	for j in range(0,i):
		print(i,end=" ")
	print()
	
b = int(input("7. how many row print : "))
for i in range(b):
	for j in range(i):
		print("*",end=" ")
	print("*")
	
a = int(input("8. how many row print : "))
for i in range(a,0,-1):
	for j in range(i):
		print(a,end=" ")
	print()
	

a = int(input("9. how many row print : "))
for i in range(a):
	for j in range(i,0,-1):
		print(j,end=" ")
	print()
	
a = int(input("10. how many row print : "))
for i in range(a):
	for j in range(a-i-1):
		print(" ",end=" ")
	for j in range(i):
		print("*  ",end=" ")
	print()
	
	
a = int(input("11. how many row print : "))
for i in range(a):
	for j in range(i):
		print(" ",end=" ")
	for j in range(a-i-1):
		print("*  ",end=" ")
	print()
	
n =int(input("12. enter how many rows print : "))
for i in range(65 , n+65):
	for j in range(65 , i+1):
		print(chr(j) , end=" ")
	print()
	
n =int(input("13 enter how many rows print : "))

for i in range(65 , n+65):
	for j in range(65 , i+1):
		print(chr(i) , end=" ")
	print()
	
n =int(input("14. enter how many rows print : "))
a = 65 #ASSCI value A

for i in range(n):
	for j in range(i+1):
		print(chr(a) , end=" ")
		a+=1
	print()
	
n =int(input("15.enter how many rows print : "))
a = 97 #ASSCI value A

for i in range(n):
	for j in range(i+1):
		print(chr(a) , end=" ")
		a+=1
	print()
	
n =int(input("16. enter how many rows print : "))
for i in range(65+n,64,-1):
	for j in range(65 , i+1):
		print(chr(j) , end=" ")
	print()