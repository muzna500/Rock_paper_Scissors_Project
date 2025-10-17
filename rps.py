#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    """A player that chooose a move at random"""
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    """A player that takes input from a human"""
    def move(self):
        while True:
            move = input("Enter your move (rock, paper, scissors): ").lower()
            if move in moves:
                return move
            else:
                print("Invalid move! Try Again.")


class ReflectPlayer(Player):
    """A player that mimics the opponent's last move"""
    def __init__(self):
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    """A player that cycles through the moves in order"""
    def __init__(self):
        self.last_move = None

    def move(self):
        if self.last_move is None:
            self.last_move = random.choice(moves)
        else:
            index = moves.index(self.last_move)
            self.last_move = moves[(index + 1) % len(moves)]
        return self.last_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            self.p1_score += 1
            print("Player 1 wins this round!")
        elif beats(move2, move1):
            self.p2_score += 1
            print("Player 2 wins this round!")
        else:
            print("It's a tie!")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"\nRound {round + 1}:")
            self.play_round()
            print(f"Scores: Player 1: {self.p1_score}, "
                  f"Player 2: {self.p2_score}")
        print("\nGame over!")
        if self.p1_score > self.p2_score:
            print("Player 1 wins the game!")
        elif self.p2_score > self.p1_score:
            print("Player 2 wins the game!")
        else:
            print("The game is a tie!")


if __name__ == '__main__':
    print("Welcome to Rock, Paper, Scissors!")
    # Change player here to test different combinations
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
