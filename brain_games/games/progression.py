#!/usr/bin/env python3
import random


PROMT = 'What number is missing in the progression?'


def get_sequence():
    number = random.randint(1, 10)
    step = random.randint(1, 10)

    index = 10
    sequence = []
    while index > 0:
        sequence.append(str(number))
        number += step
        index -= 1

    return sequence


def get_task():
    sequence = get_sequence()
    position = random.randint(1, len(sequence))
    correct_answer = sequence.pop(position - 1)
    sequence.insert(position - 1, '..')
    question = ' '.join(sequence)

    return [question, correct_answer]
