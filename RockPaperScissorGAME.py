import random
Computer_choice=random.randint(0, 2)
user_choice=int(input("Enter Your Choice in numbers\nrock=0 \npaper=1 \nscissor=2 :"))
print(f"Computer chose {Computer_choice}")
if(Computer_choice==user_choice):
  print("The game is Draw")
elif(Computer_choice==0 and user_choice==1):
  print("You won the game.. ")
elif(Computer_choice==0 and user_choice==2):
  print(" Computer won the game")
elif(Computer_choice==1 and user_choice==0):
  print("computer won the game")
elif(Computer_choice==1 and user_choice==2):
  print("You won the game")
elif(Computer_choice==2 and user_choice==0):
  print("You won the game")
elif(Computer_choice==2 and user_choice==1):
  print("Computer Won the game")
else:
  print("Enter the valid number")