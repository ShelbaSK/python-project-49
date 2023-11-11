#!/usr/bin/env python3
import prompt
import brain_games.cli as cli
import brain_games.scripts.games.brain_even as brain_even
import brain_games.scripts.games.brain_calc as brain_calc
import brain_games.scripts.games.brain_gcd as brain_gcd
import brain_games.scripts.games.brain_progression as brain_progression
import brain_games.scripts.games.brain_prime as brain_prime


def round(round_data):
    print(f'Question: {round_data[0]}')
    user_answer = prompt.string('Your answer: ')

    if user_answer == round_data[1]:
        return True
    return user_answer


rounds = 3


def start_game(game_name=None):
    print('Welcome to the Brain Games!')
    username = cli.welcome_user()

    question = []
    match game_name:
        case 'even':
            for element in range(0, rounds):
                question.append(brain_even.get_task())
                promt = brain_even.promt
        case 'calc':
            for element in range(0, rounds):
                question.append(brain_calc.get_task())
                promt = brain_calc.promt
        case 'gcd':
            for element in range(0, rounds):
                question.append(brain_gcd.get_task())
                promt = brain_gcd.promt
        case 'progression':
            for element in range(0, rounds):
                question.append(brain_progression.get_task())
                promt = brain_progression.promt
        case 'prime':
            for element in range(0, rounds):
                question.append(brain_prime.get_task())
                promt = brain_prime.promt
        case _:
            return None

    print(promt)

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


def main():
    start_game()


if __name__ == '__main__':
    main()
