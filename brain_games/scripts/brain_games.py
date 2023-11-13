#!/usr/bin/env python3
import prompt
import brain_games.cli as cli


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


def main():
    start_game()


if __name__ == '__main__':
    main()
