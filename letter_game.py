print("welcome to DICT !!!!!!!!!!!!!!!")
print("you have FIVE trials to guess the word right")
import random
with open("text.txt") as word_file:
	 value= list(word_file.read().split())
letter=random.choice(value).lower()
hint = letter[0:4]
#print(letter)
trial=1
score=0
def scramble(word):
    word=list(word)
    #print(word)
    random.shuffle(word)
    string_word=""
    for string in word:
        string_word+=string
    return(string_word) 
shuffled_word=scramble(letter)
print("scrambled word : "+ shuffled_word)
print("Hint is {}...".format(hint))
while True:
    user_input=input("DICT ....").lower()
    if user_input==letter:
        print("Dict scholar !!!!")
        score=+1
        print("SCORE = " + str(score) +" points")
        break
    else:
        print("ERROR")
        if (trial)==5:
            print("you have "+str(score)+" points")
            print("GAME OVER  >>>>")
            restart=input("Do you want to start again...Type Enter ").lower()
            if restart=="enter":
               trial=1
               score=0
               continue
            else:
                break
        trial+=1
        print("trial = " + str(trial))
        continue
        
     
