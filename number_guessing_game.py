import random


def number_guessing_game():
    """
    A simple number guessing game.
    The computer picks a random number between 1 and 100.
    The player has 7 attempts to guess it.
    """
    # Step 2: Generate random number between 1 and 100
    random_number = random.randint(1, 100)

    # Fixed secret number = 5 (no longer random)
    random_number = 5
    
    # Step 3: Set maximum number of attempts
    max_attempts = 7
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    # Step 4: Use a for loop to give limited attempts
    for attempt in range(1, max_attempts + 1):
        # Step 5: Get player's guess
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer number.")
            continue
        
        # Step 6: Compare guess with random number
        if guess == random_number:
            print(f"\nCongratulations! You guessed the number {random_number} correctly!")
            print(f"You got it in {attempt} attempt(s). 🎉")
            return  # End the game early when correct
        
        elif guess < random_number:
            print("Too low!")
        
        else:
            print("Too high!")
        
        # Optional: show remaining attempts
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"{remaining} attempt(s) remaining.\n")
        else:
            print()  # just a blank line before final message
    
    # Step 7: If we get here → player used all attempts without success
    print(f"Game over! You've used all {max_attempts} attempts.")
    print(f"The correct number was {random_number}.")


# ────────────────────────────────────────────────
#           Run the game
# ────────────────────────────────────────────────

if __name__ == "__main__":
    number_guessing_game()