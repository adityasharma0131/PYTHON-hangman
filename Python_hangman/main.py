import random
import hangman_art
import hangman_words

print(hangman_art.logo)

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# lives = 6bcas there are 7 character in the list to display the hangman
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# creating a list of blank sapces
display = []
for x in range(word_length):
  display += "_"

# loop for the continuation of the algo
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  # check if the guessed letter is aldready in the list
  if guess in display:
    print(f'You have aldready entered {guess} in the list')

  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:  # insert the letter in the blank list if the guessed letter is right

      display[position] = letter

  if guess not in chosen_word:  # if the guessed letter is not the correct-one then reduce  the lives by 1
    print(f'The guessed letter {guess} is not in the word. You loose a life!!')
    lives -= 1
    if lives == 0:  # if the lives  = 0, that means the games is over bcas ther are no more characters left in the list
      end_of_game = True
      print("You lose.")

  print(f"{' '.join(display)}")  # to conver the blank list to a string

  if "_" not in display:  # check if the list is still empty or not
    end_of_game = True
    print("Yaaaay You win.")

  print(hangman_art.stages[lives])
