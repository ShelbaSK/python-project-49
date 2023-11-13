#!/usr/bin/env python3
import random


promt = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    result = number % 2

    if not result:
        return 'yes'
    return 'no'


def get_task():
    question = random.randint(1, 100)
    correct_answer = is_even(question)
    return [question, correct_answer]
