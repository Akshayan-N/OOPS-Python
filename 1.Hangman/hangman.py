from random  import choice
from time import sleep
from string import ascii_letters
from os import system, name

class Hangman:
    def __init__(self):
        pass


    @classmethod
    def loadgamefile(cls):
        wordfile = "./wordlist/file.txt"
        hangman = "./wordlist/hangman.txt"

        with open(wordfile, "r") as wordlist :
            wordlist = wordlist.read().split('\n')
        
        
        Hangman.word = choice(wordlist)
        
        with open(hangman, 'r') as hangman:
            Hangman.pic = hangman.readlines()
        
    def print_hangman(numerator = 1, denomerator = 1):
        line = int(numerator / denomerator * 10)
        
        for index in range(0,line) :
            print(Hangman.pic[index], end="")
        print()
        
    @classmethod
    def play(cls):
        Hangman.loadgamefile()
        Hangman.banner()
        Hangman.countdown_timer()
        
        start = ['_'] * len(cls.word)
        end = list(cls.word)
        existing_letter = []
        
        attempts = 0
        total_attempts = len(cls.word) + 2  
        
        while (attempts != total_attempts):
            Hangman.clear()
            if start == list(cls.word) :
                print("You won, You saved hangman")
                print(f"The Word : {cls.word}")
                break

            
            Hangman.print_hangman(attempts, total_attempts)
            print(start)

            letter = input("Enter you letter : ").lower()
            if len(letter) == 1 and letter in ascii_letters :
                if letter in existing_letter :
                    print("The letter is already")
                elif letter in end:
                    while letter in end:
                        index = end.index(letter)
                        start[index] = letter 
                        end[index] = None
                        existing_letter.append(letter)

                        print("You guessed the letter correctly wow !!! ")
                else:
                    print("Wrong guess \n Letter not in the word")
                    attempts += 1
                
                
            else:
                print("Please enter a single character [a-z and A-Z]")

            sleep(2)

            
        else:
            Hangman.clear()
            Hangman.print_hangman()
            print("Hangman Died")
            print(f"The Word : {cls.word}")

    @staticmethod
    def countdown_timer():
        seconds = 3
        for i in range(seconds, 0, -1):
            print(f"Game starting in {i}...", end='\r')
            sleep(1)
        print("---------Game started!-------------")
        sleep(1)

    @staticmethod
    def banner():
        print("""
 _   _    _    _   _  ____ __  __    _    _   _ 
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  | 
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|
              
""")
    
    @staticmethod
    def clear():
        if name == 'nt':
            system('cls')
        else:
            system('clear')
