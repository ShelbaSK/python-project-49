import prompt
import brain_games.cli as cli


def round(round_data):
    print(f'Question: {round_data[0]}')
    user_answer = prompt.string('Your answer: ')

    if user_answer == round_data[1]:
        return True
    return user_answer


def greeting_player():
    print('Welcome to the Brain Games!')
    username = cli.welcome_user()
    return username


def prepare_game(game, rounds):
    questions = []
    for _ in range(0, rounds):
        questions.append(game.get_task())
    return questions


def start_game(questions, rounds):
    game_result = True
    user_answer = None
    correct_answer = None
    score = 0
    while score < rounds:
        result = round(questions[score])
        if result is True:
            print('Correct!')
            score += 1
        else:
            game_result = False
            user_answer = result
            correct_answer = questions[score][1]
            break
    return [game_result, user_answer, correct_answer]


def finish_game(username, result, user_answer=None, correct_answer=None):
    if result:
        message = f'Congratulations, {username}!'
    else:
        message = (f"'{user_answer}' is wrong answer ;(. "
                   f"Correct answer was '{correct_answer}'.\n"
                   f"Let's try again, {username}!")
    return message


ROUNDS = 3


def init_game(game=None):
    username = greeting_player()
    if game is not None:
        questions = prepare_game(game, ROUNDS)
        print(game.PROMT)
        result = start_game(questions, ROUNDS)
        message = finish_game(username, *result)
        print(message)
