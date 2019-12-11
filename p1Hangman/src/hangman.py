'''
Created on Nov 23, 2019

@author: ITAUser
'''

#import random library

#define a function called pick_random_word():
    #open word dictionary/list(words.txt)
    #variable called index = selects random word from words.txt
    #create variable called word = strip the randomly selected word
    #return the variable 'word'

#define a function called ask_for_next_letter():
    #variable called letter = input function that asks user to select a letter
    #return the letter selected
    
#define a function called generate_word_string(word, letters_guessed):
    #variable called output = empty list
    #make a for loop that goes through each letter in the variable 'word':
        #if statement that checks if letter is in letters guessed:
            #append letter to output
        #else:
            #append (" ")
        #return output as a string

#create a main module:
    #variable called WORD = pick_random_word()
    
    #variable called letters_to_guess = set of WORD
    #variable called correct_letters_guessed = empty set
    #variable called incorrect_letters_guessed = empty set
    #variable called number_of_guesses = number of guesses you want your user to have
    
    #print statement that welcomes the user to hang man
    
    #while loop that runs until number_of_guesses is less than one or letters-to_guess is grater than zero
        #variable called guess = ask_for_next_letter() and turn it into lower case
        
        #if statement that checks if guess is in correct_letters_guessed or guess is in incorrect_letters_guessed:
            #print statement that says you already guessed that letter
            
        #if statement that checks if guess is in letters_to_guess:
            #remove guess from letters_to_guess
            #add guess to correct_letters_guessed
        #else:
            #add guess to incorrect_letters_guessed
            #number_of_guesses goes down by one
        #variable called word_string = generate_word_string(word, correct_letters_guessed)
        #print statement that prints word string
        #print statement that prints how many guesses you have
        
        #if statement to check if number_of_guesses is grater than
            #print congratulations you guessed the word correctly
        #else:
            #print sorry you lost. the word was WORD
        
    










