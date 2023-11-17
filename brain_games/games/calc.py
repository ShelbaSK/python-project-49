#!/usr/bin/env python3
import random


PROMT = 'What is the result of the expression?'


def get_operation():
    operation = ('+', '-', '*')
    element = random.randint(0, len(operation) - 1)
    return operation[element]


def get_result(operation, first_operand, second_operand):
    match operation:
        case '+':
            result = first_operand + second_operand
        case '-':
            result = first_operand - second_operand
        case '*':
            result = first_operand * second_operand
        case _:
            return None
    return result


def get_task():
    operation = get_operation()
    first_operand = random.randint(1, 100)
    second_operand = random.randint(1, 100)

    question = f'{first_operand} {operation} {second_operand}'
    correct_answer = get_result(operation, first_operand, second_operand)

    return [question, str(correct_answer)]
