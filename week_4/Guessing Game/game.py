import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                print()
            else:
                return level
        except ValueError:
            print("Please enter a valid integer.")

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                print("Please enter a positive integer.")
            else:
                return guess
        except ValueError:
            print("Please enter a valid integer.")

def main():
    level = get_level()
    answer = random.randint(1, level)

    while True:
        guess = get_guess()
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
