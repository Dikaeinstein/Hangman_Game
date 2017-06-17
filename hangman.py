import wordlist
from random import choice
from string import ascii_lowercase

global_word = ""

def select_word():
    words = [word for word in wordlist.make_word_list1() if len(word) < 8]
    return choice(words)
    
       
def start_game():
    global global_word
    global_word = select_word()
    length = len(global_word)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(length))


def splice(word, letter=""):
    if len(letter) == 0:
        return word
    t = list(word)
    t.remove(letter)
    return "".join(t)
  
  
def logic(n=12, ch="", guess=None):
    guess = guess or "_"*len(global_word)
    
    if n == 0:
        end_game(0)
        return
    if all(c in ascii_lowercase for c in guess):
        end_game(1)
        return
        
    print("__________")
    print("You have {} guesses left.".format(n))
    print("Available letters: {}".format(splice(ascii_lowercase, ch)))
    letter = str(input("Please guess a letter: "))
    if letter in global_word:
        t = list(guess)
        for index, l in enumerate(global_word):
            if l == letter:
                t[index] = letter
        guess = "".join(t)
        print("Good guess: {}".format(guess))
        logic(n, letter, guess)
    else:
        print("Oops! That letter is not in my word: {}".format(guess))
        logic(n-1, "", guess)
    

def end_game(n):
    if n == 0:
        print("Sorry, Game over!")
    else:
        print("Congratulations, you won!")

    
if __name__ == "__main__":
    start_game()
    print(global_word)
    logic()
    
