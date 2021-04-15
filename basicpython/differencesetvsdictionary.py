#set and dictionary can not mention index no 
#so can not access to use index no. ex= a[0]
#diffrence between set and dictionary
#set is collection of str , int , float
#dictionary is collection of key , value pair
#creat empty set                a = set()
#cerat empty dictionary    a ={ }

print("this is set : ")
a = {10, 20, 30, 40, "tejas"}
print(a)
print()
 
print("this is dictionary : ")
b = {10 : "tejas" , 20 : "raj" , 30 : "ravi" , 40 : "harsh"}
print(b)
print()

print("set access element : ")
for i in a:
	print(i)
print()

print("dictionary access element : ")
print(b[10])
print(b[20])
print(b[30])
print(b[40])
print()
print(b.setdefault(10 , "python"))
print(b.setdefault(70 , "python")) # 70 does not exist so return python
print()

for i in b:
	print(i, b[i])
print()

c = b.keys()
print(c)
d= b.values()
print(d)
print()

c = list(b.keys())
print(c)
d= list(b.values())
print(d)
print()

	
for i in c:
	print(i)
print()

print("add value in set : ")
print(a.add(100))
print(a)
print()

print("add value in dictionary : ")
b.update({101: "jay"})
print(b)
print()

print("empty set to value give : ")
x = set()
print(x)
x.add(100)
x.add(200)
print(x)
print()

print("empty dictionary to value give : ")
z ={}
print(z)
z.update({101:"tejas"})
print(z)
p={102:"raj" , 103:"ravi"}
z.update(p)
print(z)
print()

print("delete set function : ")
x.remove(100)
print(x)
print()

print("delet dictionary function : ")
del z[101]
print(z)
print()
z.pop(103)
print(z)

z.clear()
print(z)