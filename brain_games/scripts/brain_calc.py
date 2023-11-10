#!/usr/bin/env python3
import random
import brain_games.scripts.brain_games as brain_games


def get_operation():
    operation = ('+', '-', '*')
    element = random.randint(0, 2)
    return operation[element]


def get_task():
    operation = get_operation()
    fitst_operand = random.randint(1, 100)
    second_operand = random.randint(1, 100)

    question = f'{fitst_operand} {operation} {second_operand}'

    match operation:
        case '+':
            correct_answer = fitst_operand + second_operand
        case '-':
            correct_answer = fitst_operand - second_operand
        case '*':
            correct_answer = fitst_operand * second_operand
        case _:
            return None

    return [question, str(correct_answer)]


def main():
    brain_games.start_game('calc')


if __name__ == '__main__':
    main()
