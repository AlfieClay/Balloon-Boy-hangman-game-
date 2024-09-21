#imports.
import os
import case_conversion
from case_conversion import upper_to_lower, lower_to_upper, upper_to_lower_list, lower_to_upper_list
import PIL
from PIL import Image
import csv_list
from csv_list import csv_list
import random as ran

#initial variables and constants.
difficulty_level=input("Welcome to Balloon Boy. What level of difficulty would you like? Type 'e' (easy- 15 balloons), 'm' (medium- 10 balloons) or 'h' (5 balloons).\n")
allowed_answers=['e','m','h']
if difficulty_level not in allowed_answers:
    print("Error. Please type in lower case. Try again:\n")
    difficulty_level=input("What level of difficulty would you like? Type 'e' (easy- 15 balloons), 'm' (medium- 10 balloons) or 'h' (5 balloons).\n")
balloon_number=int() #how many balloons the user is allowed to pop.
if difficulty_level=='e':
    balloon_number=15
elif difficulty_level=='m':
    balloon_number=10
elif difficulty_level=='h':
    balloon_number=5
upper_words=csv_list(file="dictionary.csv") #the group of words used in the game. a list has been made from a string of upper case starting words.
lower_words=upper_to_lower_list(upper_words) #convert upper case beginnings to loewr case begginings.
random_index=ran.randint(0,int(len(lower_words)-1)) #the index is chosen from numbers from 0 to len(words)-1.
mystery_word=lower_words[random_index] #the word used in the game.
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

#user guessing game
blanked_word="_ "*len(mystery_word) #the word as it appears to the user throughout the game.
print(blanked_word)
os.chdir("./images")
img_name_I=str(balloon_number)+"_balloons.png" #the name of the first image to appear for each initial balloon number setting.
Image.open(img_name_I).show() #print the image of max balloons.
solved_indices=[] #the indices of letter_guess within mystery_word.
letter_guesses=[] #letters guessed by the player.
while balloon_number>0 and "_" in blanked_word:
    letter_guess=input("Guess a letter: ")
    if letter_guess not in letter_guesses:
        letter_guesses.append(letter_guess)
    else:
        pass
    if letter_guess in mystery_word:
        for i in range(int(len(mystery_word)-1)):
            char=mystery_word[i]
            if char==letter_guess:
                solved_indices.append(i) #if the chracter in mystery word equals the letter guess, add the corresponding index.
        blanked_word=str() #reset blanked_word as may change over the round.
        for j in range(int(len(mystery_word)-1)):
            if j in solved_indices:
                blanked_word=blanked_word+mystery_word[j]+" " #add a 'char ' to reveal part of the blanked word.
            else:
                blanked_word=blanked_word+"_ " #if the index is not a match, add a blank '_ ' to the new blanked word.
        print("You were successful! Keep going.")
    else:
        balloon_number-=1
        if balloon_number==0:
            break
        else:
            #Image.close() #reset the cv2 window.
            img_name=str(balloon_number)+"_balloons.png"
            Image.open(img_name).show()
            print(f"You were unsuccessful. You now have {balloon_number} balloons. Try again.\n")
    remaining_letters=[] #letters not yet guessed
    for letter in alphabet:
        if letter not in letter_guesses:
            remaining_letters.append(letter)
    print(f"Remaining letters: {remaining_letters}.\n{blanked_word}\n")

if "_" not in blanked_word:
    print(f"You win! You guessed the correct word: {mystery_word}.")
    Image.open("you_win.png").show()
else:
    print(f"Game over! The mystery word was {mystery_word}. Better luck next time.")
    Image.open("game_over.png").show()

            



    
