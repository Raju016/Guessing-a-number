from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
"""
print(logo)

def set_difficulty():
  level = input("Select difficulty Type 'easy' or 'hard':")
  if level == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS



def check_answer(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
      print("Too High")
      return turns - 1
    elif user_guess < actual_answer:
      print("Too low")
      return turns - 1
    else:
        print("You got it")

def game():
  print("Welcome to Guessing Number game")
  print("I'm Thinking a number between 1 to 100")
  answer = randint(1,100)
  
  turns = set_difficulty()
  
  
  guess = 0
  while guess != answer:
    print(f"you have {turns} remaining chanses!")
    guess = int(input("Make a guess :"))
  
    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("You hav run out of guesses")
      return 
    elif guess != answer:
      print("Guess again")


game()