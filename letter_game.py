print("welcome to DICT !!!!!!!!!!!!!!!")
print("you have FIVE trials to guess the word right")
trial=5
score=0
while trial <=5:
    import random
    with open("text.txt") as word_file:
             value= list(word_file.read().split())
    letter=random.choice(value).lower()
    #print(letter)
    def scramble(word):
        word=list(word)
        #print(word)
        random.shuffle(word)
        string_word=""
        for string in word:
            string_word+=string
        return(string_word) 
    shuffled_word=scramble(letter)
    hint = letter[0:4]
    print("scrambled word : "+ shuffled_word)
    print("Hint is {}...".format(hint))
    user_input=input("DICT ....").lower()
    if user_input==letter:
        print("Dict scholar !!!!")
        score=+10
        print("SCORE = " + str(score) +" points")
    else:
        print("Wrong!!!")
        print(f"The Correct word is {letter}")
        trial = trial - 1
        print(f"you have {trial} left")
       


    
    
    
     
