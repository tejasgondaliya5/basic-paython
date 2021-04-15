def hcf(a,b):
	if(b == 0):
		return a
	else:
		return hcf(b,a%b)
a  = 60
b = 48
print(hcf(60,48))