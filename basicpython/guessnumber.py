print("welcome to gusse no. game : ")
n=5
i=0
while(i<3):
	a=int(input("guess the number : "))
	if (a<5):
		print("guess big number then :")
	elif(a>5):
		print("guess small number then :")
	elif(a>=5):
		print("you won this game ::)")
		break
	else:
		print("invail input :")
	i+=1
else:
  print("you loss game : ")
  print("right ans is 5")
  
	