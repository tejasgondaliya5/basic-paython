a = [10 , 20 , 30 ,40.56 , "tejas" , "raj"]
print(a)
print ()

#........................................................................
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print()

#........................................................................
print("access for loop using")
for i in a:
	print(i)
print()

#...........................................................................
print("list access forloop with index :")
n = len(a)
for i in range(n):
	print(i , "=" ,a[i])
print()
	
#..........................................................................
print("list access while loop : ")
n = len(a)
i=0
while (i<n):
	print(i , "=" , a[i]) 
	i+=1
	