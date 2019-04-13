import random
number=random.randint(0,100)
print(number)
while True:
      user_input=input("enter your number>>>")
      if user_input.isdigit():
      	 user_input=int(user_input)
      	 if user_input==number:
      	 	print("you won")
      	 	break
      	 else:
      	 	print("Not correct guess")
      else: 
      	 print("wrong entry")


##with open("biola.txt") as word_file:
##	 value= list(word_file.read().split())
##print(value)
