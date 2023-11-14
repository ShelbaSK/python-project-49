#!/usr/bin/env python3
import random


PROMT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False

    result = []
    for index in range(1, number + 1):
        if number % index == 0:
            result.append(index)
    if len(result) > 2:
        return False
    else:
        return True


def get_task():
    question = random.randint(1, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return [question, correct_answer]
