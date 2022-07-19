import random
fruits=["apple","mango","banana"]
stages=[#0
        """

        --------
        |    |
        |    o
        |   \|/
        |    |
        |   / \\
        -

        """,
        #1
        """

        --------
        |    |
        |    o
        |   \|/
        |    |
        |   /    
        -

        """,
        #2
        """

        --------
        |    |
        |    o
        |   \|/
        |    |
        |   
        -

        """,
         #3
        """

        --------
        |    |
        |    o
        |   \|
        |    |
        |   
        -

        """,
        #4
        """

        --------
        |    |
        |    o
        |    |
        |    |
        |   
        -

        """,
        #5
        """

        --------
        |    |
        |    o
        |  
        |    
        |   
        -

        """,
        #6
        """

        --------
        |    |
        |    
        |  
        |    
        |   
        -

        """


]
#welcoming the user
def game():
    name = input("What is your name? ")
    print("Hello, " + name, "Time to play hangman!")
    word = random.choice(fruits) #apple
    guesses = '' #empty string
    turns = 6
    while turns > 0 and guesses!=word:
        print(stages[turns])
        for char in word:#apple a p p l
            if char in guesses: #ban
                print(char,end=" ")    
            else:
                print("_",end=" ")                  
        print()
       
        guess = input("guess a character:")
        guesses += guess #al
        if guess not in word:
            turns =turns- 1
            print("Wrong") 
            print("You have", + turns, 'more guesses') 
 
            if turns == 0:
                print(stages[turns])
                print("You Lose and the word was",word)
        if guesses==word:
            print("you guessed it")
            return 5
    return 5


c=game()