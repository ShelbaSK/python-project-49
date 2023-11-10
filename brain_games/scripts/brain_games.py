#!/usr/bin/env python3
import prompt
import brain_games.cli as cli
import brain_games.scripts.brain_even as brain_even
import brain_games.scripts.brain_calc as brain_calc


def greetings():
    print('Welcome to the Brain Games!')


def round(round_data):
    print(f'Question: {round_data[0]}')
    user_answer = prompt.string('Your answer: ')

    if user_answer == round_data[1]:
        return True
    return user_answer


def start_game(game_name=None):
    greetings()
    username = cli.welcome_user()

    question = []
    match game_name:
        case 'even':
            for element in range(0, 3):
                question.append(brain_even.get_task())
                promt = ('Answer "yes" if the number is even, '
                         'otherwise answer "no".')
        case 'calc':
            for element in range(0, 3):
                question.append(brain_calc.get_task())
                promt = 'What is the result of the expression?'
        case _:
            return None

    print(promt)

    score = 0
    while score < 3:
        result = round(question[score])
        if isinstance(result, bool):
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
