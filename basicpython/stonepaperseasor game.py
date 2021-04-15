import random
print("welcome to stone paper seasor game!"/n)


while(attempt >= 5):
    lis = ["ston" , "paper" , "seasor"]
    ran = random.choice(lis)

    inp = inpute("enter your choice"/n)
    attempt = 1
    your_score = 0
    computer_score = 0
    if inp==ran:
      	print(f"you have select ({inp}) and computer have guess ({ran})")
      	print("tie! = point can not achive anyone") 
    
    elif (inp=="paper" and ran=="stone"):
    	print(f"you have select ({inp}) and computer have guess ({ran})")
    	print("point is your")
    	print("computer is loss")
    	your_score+=1
    	print(your_score)
    
    elif (inp=="seasor" and ran=="paper"):
    	print(f"you have select ({inp}) and computer have guess ({ran})")
    	print("point is your")
    	print("computer is loss")
    	your_score+=1
    	print(your_score)
    	
    elif(inp=="stone" and ran=="seasor"):
    	print(f"you have select ({inp}) and computer have guess ({ran})")
    	print("point is your")
    	print("computer is loss")
    	your_score+=1
    	print(your_score)
    	
    elif(inp=="stone" and ran=="paper"):
    	print(f"you have select ({inp}) and computer have guess ({ran})")
    	print("you are loss the point")
    	print("point is win computer")
    	computer_score+=1
    	print(computer_score)
    	
    elif(inp=="paper" and ran=="seasor"):
    	print(f"you have select ({inp}) and computer have guess ({ran})")
    	print("you are loss the point")
    	print("point is win computer")
    	computer_score+=1
    	print(computer_score)
    
    elif(inp=="seasor" and ran=="stone"):
    	print(f"you have select ({inp}) and computer have guess ({ran})")
    	print("you are loss the point")
    	print("point is win computer")
    	computer_score+=1
    	print(computer_score)
    
    else:	
      	print("not vaild inpute")
          



