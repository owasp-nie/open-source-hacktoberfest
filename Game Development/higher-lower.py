import random

def play_game():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number (1-100): "))
        attempts += 1

        if guess == target_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < target_number:
            print("Higher! Try again.")
        else:
            print("Lower! Try again.")

if __name__ == "__main__":
    play_game()
