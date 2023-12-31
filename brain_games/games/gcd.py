#!/usr/bin/env python3
import random


PROMT = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_operand, second_operand):

    if first_operand == second_operand:
        return first_operand

    while first_operand != 0 and second_operand != 0:
        if first_operand > second_operand:
            first_operand %= second_operand
        else:
            second_operand %= first_operand

    if first_operand == 0:
        return second_operand
    else:
        return first_operand


def get_task():
    first_operand = random.randint(1, 100)
    second_operand = random.randint(1, 100)

    question = f'{first_operand} {second_operand}'
    correct_answer = get_gcd(first_operand, second_operand)

    return [question, str(correct_answer)]
