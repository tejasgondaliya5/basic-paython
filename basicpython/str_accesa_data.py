str = "Tejas is a good boy"
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[-1])
print(str[-2]) 

print()
print("using for loop whitout index acess data :")
print()
for i in str:
	print(i)
	
print()
print("using for loop with index access data :")
print()
n = len(str)
for i in range (n):
	print(i , "=" , str[i])
	
print()
print("using while loop access data")
print()
n=len(str)
i=0
while (i<n):
	print(str[i])
	i+=1
