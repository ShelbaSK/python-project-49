#!/usr/bin/env python3
import prompt
import brain_games.cli as cli
import brain_games.games.brain_calc as brain_calc
import brain_games.games.brain_even as brain_even
import brain_games.games.brain_gcd as brain_gcd
import brain_games.games.brain_prime as brain_prime
import brain_games.games.brain_progression as brain_progression


def round(round_data):
    print(f'Question: {round_data[0]}')
    user_answer = prompt.string('Your answer: ')

    if user_answer == round_data[1]:
        return True
    return user_answer


rounds = 3


def start_game(game=None):
    print('Welcome to the Brain Games!')
    username = cli.welcome_user()

    if game is not None:
        question = []
        for element in range(0, rounds):
            question.append(game.get_task())

        print(game.promt)

        score = 0
        while score < 3:
            result = round(question[score])
            if result is True:
                print('Correct!')
                score += 1
            else:
                break

        if score == 3:
            message = f'Congratulations, {username}!'
        else:
            message = (f"'{result}' is wrong answer ;(. "
                       f"Correct answer was '{question[score][1]}'.\n"
                       f"Let's try again, {username}!")

        print(message)


def init_calc():
    start_game(brain_calc)


def init_even():
    start_game(brain_even)


def init_gcd():
    start_game(brain_gcd)


def init_prime():
    start_game(brain_prime)


def init_progression():
    start_game(brain_progression)


def main():
    start_game()


if __name__ == '__main__':
    main()
