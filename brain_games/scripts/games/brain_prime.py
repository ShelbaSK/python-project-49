#!/usr/bin/env python3
import random
import brain_games.scripts.brain_games as brain_games


promt = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return 'no'

    result = []
    for index in range(1, number + 1):
        if number % index == 0:
            result.append(index)
    if len(result) > 2:
        return 'no'
    else:
        return 'yes'


def get_task():
    question = random.randint(1, 100)
    correct_answer = is_prime(question)

    return [question, correct_answer]


def main():
    brain_games.start_game('prime')


if __name__ == '__main__':
    main()
