#!/usr/bin/env python3
import random


PROMT = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    result = number % 2

    if not result:
        return True
    return False


def get_task():
    question = random.randint(1, 100)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return [question, correct_answer]
