#tupple is same is list but tupple can't modify the value'
a = (10)
print("a is :", type(a))

b = (10 ,)
print("b is :", type(b))

c = 10 , 20 , 30 , "tejas"
print("c is :", type(c))

d = (10 ,20, 30 ,40, 50, 60, 70)
print(d[0])
print(d[1])
print(d[-1])
print()

print("using without index : ")
for i in d:
	print(i)
	
print("using with index : ")
n = len(d)
for i in range(n):
	print(i ,"=",d[i])
print()

print("using while loop : ")
n= len(d)
i = 0
while (i<n):
	print(i , "=", d[i])
	i+=1
print()


#.........slicing on tuple..................
e = d[1:7:2]
print(e)
print()

e = d[::2]
print(e)
print()

e = d[2:]
print(e)
print()

e = d[:5]
print(e)
print()

e = d[::-1]
print(e)
print()

e = d[-4:]
print(e)
print()

e = d[:-4]
print(e)
print()

e= d[-4: -1] #..e= d[-1: -4] am na lkhi sakay
print(e)
print()

#.......tuple concatenation....................
a = (1 , 2 , 3)
b = (4 , 5 , 6)

print(a)
print(b)
 
print(a + b)
print()

#.....modifying .....................................

#tuple can not modify becuse tuple is immuteble.......
#but
#use concatination
#slicing is better option............
#ex.
a =(10, 20, 30, 40, 50,)
print(a)
b = (60, 70) #add this tuple between 1 and 2 position

s1=a[0:2]
s2=a[2:6]
c=s1+b+s2
print(c)
print()

#..... delete tuple..............
#delete full tuple can possible but delete element can't possible
a = (10 , 20 , 30 , 40 , 50)
#del a
#print(a) #giving error "a" is not defind
print(a)
s1 = a[0:3]
print(s1) #3 and 4 element remove
print()

 #geting input form user
 #that is not possible but 
 #using logic possible
 #inpute take list and typcast in tuple
a = [ ]
n = int(input("enter how many element store : "))
for i in range(n):
	a.append(int(input("enter element : ")))
print(type(a))
 
a = tuple(a)
print(type(a))
print(a)
 