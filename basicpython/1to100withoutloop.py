print("using function method")
i = 1
def rep():
	global i
	if i<101:
		print(i)
		i+=1
		rep()
rep()

print("using recursion function : ")
def rec(n):
	if n>=100:
		return 100
	else:
		return n , rec(n+1)

print(rec(0))
print()

print("using list function : ")
a =list(range(0,100))
print(a)


	
