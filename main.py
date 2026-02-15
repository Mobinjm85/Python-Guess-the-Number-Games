import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    score = 100

    print("🎯 Welcome to Guess the Number!")
    print("🔢 I have selected a number between 1 and 100.")
    print("❌ Enter 'q' to quit the game anytime.\n")

    while True:
        user_input = input("Enter your guess: ")

        if user_input.lower() == 'q':
            print("👋 Exiting the game. Better luck next time!")
            break

        if not user_input.isdigit():
            print("⚠️ Please enter a valid number!")
            continue

        user_guess = int(user_input)

        if user_guess == secret_number:
            print(f"✅ Congratulations! You guessed the number.")
            print(f"🏆 Final Score: {score}")
            break
        elif user_guess > secret_number:
            print("⬇️ Too high! Try a lower number.")
        else:
            print("⬆️ Too low! Try a higher number.")

        score -= 1
        if score == 0:
            print("❌ You've run out of points! Game over.")
            print(f"The correct number was: {secret_number}")
            break

if __name__ == "__main__":
    guess_the_number()
    
