gameOn = True

while(gameOn == True):

    print("Welcome to Bill Nye Trivia Night: Night Two!")
    print("Five Questions, all EXTREME difficulty")
    print("Are you up to the challenge???")

    questions = ["Here's your first question: Who was Bill Nye's astronomy professor?", "Here's your next question: What illness runs in Bill Nye's family?", "Third question: What is Bill Nye the CEO of?", "Almost Done, you're killing this!: What was the focus of Bill Nye's documentary Bill Nye: Science Guy?", "Last Question: What wine did Bill Nye and Neil deGrasse Tyson drink in Bill Nye: Science Guy?"]


    print(questions [0])
    print("a. Robert Pattinson")
    print("b. Aurora Sinistra")
    print("c. Carl Sagan")
    print("d. William Killinger")
    playerGuess = input("Your guess: ")
    if (playerGuess != "Carl Sagan"):  
        gameOn = False
    else:
        print(questions [1])
        print("a. Amyotrophic lateral sclerosis")
        print("b. Ataxia")
        print("c. Diabetes")
        print("d. Multiple sclerosis")
        playerGuess = input("Your guess: ")
        if (playerGuess != "Ataxia"):
            gameOn = False
        else:
            print(questions [2])
            print("a. National Aeronautics and Space Administration")
            print("b. National Space Society")
            print("c. The Bill Nye Foundation")
            print("d. The Planetary Society")
            playerGuess = input("Your guess: ")
            if (playerGuess != "The Planetary Society"):
                gameOn = False
            else:
                print(questions [3])
                print("a. The importance of developing critical thinking skills in young people")
                print("b. The climate crisis")
                print("c. Space exploration")
                print("d. Bill Nye's life after Bill Nye the Science Guy")
                playerGuess = input("Your guess: ")
                if (playerGuess != "The importance of developing critical thinking skills in young people"):
                    gameOn = False
                else:
                    print(questions [4])
                    print("")
                    playerGuess = input("Your guess: ")
                    if (playerGuess != "") and print(questions [4]):
                        gameOn = False
  
print("Wow, you really don't know Bill. Game Over")

