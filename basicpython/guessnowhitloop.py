from random import*

print("welcome to guess no. game : ")
while (True):
	y ="y"
	n = "n"
	a = (input("play game : y , exit : n : "))
	lis = list(range(0, 50))
	ran=choice(lis)
	x = ran 
	if (a==y): 
		j = 0
		while (j < 5):
		      
		    b = int(input("enter guess no 0 to 50 : "))
		    if (b>x):
			    print("guess small no : ")
			    j+=1
		    elif (b<x):
			    print("guess big no :")
			    j+=1
		    elif(b==x):
			    print("you win")
			    break
		else:
			print("you loss the game ::) try agin! :")
			print("right guess is  ",x)
	else:
		print("you exit the game : ")
		break