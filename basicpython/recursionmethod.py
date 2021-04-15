a = int(input("enter the number of fac : "))
def fac(n):
		if n ==1:
			return 1
			
		else :
			return n*fac(n-1)
			
print(fac(a))
