from array import*
a=array('i' , [])
inp = int(input("enter howmany element : "))
for i in range(inp):
	a.append(int(input("enter element : ")))
n = len(a)
print(f"lenght of array a[{n}]")
for j in a:
	print(j)