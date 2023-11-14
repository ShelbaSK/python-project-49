#!/usr/bin/env python3
import brain_games.engine as engine


ROUNDS = 3


def init_game(game=None):
    username = engine.greeting_player()
    if game is not None:
        questions = engine.prepare_game(game, ROUNDS)
        print(game.PROMT)
        result = engine.start_game(questions, ROUNDS)
        message = engine.finish_game(username, *result)
        print(message)


def main():
    init_game()


if __name__ == '__main__':
    main()
