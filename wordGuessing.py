import random
fruits=["apple","mango","banana","cherry","pineapple"]
#welcoming the user
name = input("What is your name? ")

print("Hello, " + name, "Time to play hangman!")


word = random.choice(fruits) #apple

guesses = '' #empty string


turns = 5

while turns > 0: #5>0 t            
    
    for char in word:#apple a p p l
        if char in guesses: #ban
            print(char,end=" ")    

        else:
            print("_",end=" ")                  

    print()
    guess = input("guess a character:") #a l

    guesses += guess #al
    if guess not in word:
        turns =turn- 1
        print("Wrong") 
        print("You have", + turns, 'more guesses') 
 
    # if the turns are equal to zero
        if turns == 0:
            print("You Lose and the word was",word)