#!/usr/bin/env python3
import random
import prompt
import brain_games.cli as cli
import brain_games.scripts.brain_games as brain_games


def is_even(number):
    result = number % 2

    if not result:
        return 'yes'
    return 'no'


def round():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    user_answer = prompt.string('Your answer: ')

    correct_answer = is_even(number)

    if user_answer == correct_answer:
        return [True, None, None]
    return [False, user_answer, correct_answer]


def even_game(username):
    score = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while score < 3:
        result = round()
        if result[0]:
            print('Correct!')
            score += 1
        else:
            break

    if score == 3:
        message = f'Congratulations, {username}!'
    else:
        message = (f"'{result[1]}' is wrong answer ;(. "
                   f"Correct answer was '{result[2]}'.\n"
                   f"Let's try again, {username}!")

    print(message)


def main():
    brain_games.greetings()
    username = cli.welcome_user()
    even_game(username)


if __name__ == '__main__':
    main()
