a = [10 , 20 , 30 ,40.56 , "tejas" , "raj"]
print(a)
print("id = " , id(a))
print()

#.......insert element.....................

#a.insert(3 , 70)
#print(a)
#print()

#.......change element value......................
a[1] = 50
print(a)
print("id = " , id(a))
print()

#....append function...................................
a.append("ravi")
a.append("harsh")
print(a)
print()
#......pop method(delete last element)....................................

a.pop()
print(a)
print()

#......return index number......................

x=a.index(10)
print("return index no. =",x)

#......geting input from user....................

a=[ ]
n = int(input("how many element enter : "))
for i in range(n):
 	a.append(input("enterl element : "))
 	
print(a)
for i in a:
	print(i)
print()


