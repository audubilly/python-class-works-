import random


def guess_game():
    player_name = input("Enter your Name: ")
    number_0f_guesses = 0

    print(player_name + " guess a number between 1 and 10")

    while number_0f_guesses < 5:
        number = random.randint(1, 10)
        try:
            guess = int(input())
            number_0f_guesses += 1
            print(number)

            if guess < number:
                print("your guess is too low")

            if guess > number:
                print("your guess is too high")

            if guess == number:
                # print("you guessed correctly")
                break

            if guess == number:
                print("you guessed the number in " + str(number_0f_guesses) + " tries")
            else:
                print("you did not guess the number, the number was " + str(number))
        except ValueError:
            print("you must enter a number")


if __name__ == '__main__':
    guess_game()
