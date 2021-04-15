# return function is work to return the value and return value used to declar variable, variable hold the return value and print variable
 
def add (x , y):
	c = x + y
	return c

sum = add(10 , 20)
print(sum)

#new return function
a=int(input("enter value of a : "))
b=int(input("enter value of b : "))
def pluse(x , y):
	c=x+y
	d=x-y
	return c , d , 50
		
sum , sub , a = pluse(a,b)  #sum , sub = 30 , 10                                                      (sum = 30) (sub = 10)
print(sum)
print(sub)
print(a)