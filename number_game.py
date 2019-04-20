print("welcome to MATH GUESS !!!!!!!!!!!!!!")
import random
number=random.randint(0,100)
#print(number)
while True:
      user_input=input("enter your number>>>")
      if user_input.isalpha():
          print("you  entered an alphabet")
          continue
      try:
          user_input=int(user_input)
      except:
           print("invalid input")
           continue
      if user_input==number:
         print("you won")
         break
              
      else:
          print("Not correct guess")
          
