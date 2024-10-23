import random

def guess_the_number(level=1, max_level=50):
    if level > max_level:
        print("You've completed all levels! Great job!")
        return
    
    range_limit = 100 * level
    number_to_guess = random.randint(1, range_limit)
    print(f"Level {level}: Guess a number between 1 and {range_limit}.")
    
    attempts = 0
    
    while True:
        guess = int(input("Take a guess: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Higher!")
        elif guess > number_to_guess:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    print(f"\nGreat job! Now onto Level {level + 1}.")
    guess_the_number(level=level + 1, max_level=max_level)

print("Welcome to 'Guess the Number'!")
guess_the_number()
