# Udacity Rock Paper Scissors Game
This project was submitted to Udacity during their Intro to Programming Nanodegree course. It is a text-based rock, paper, scissors game in Python, in which a human player can play against a computer player, best two out of three. You can play as many times as you like before ending the program. 

### Try it out!
[![Run on Repl.it](https://repl.it/badge/github/JaqiGates/udacity-rock-paper-scissors-game)](https://replit.com/@JaqiGates/udacity-rock-paper-scissors-game#rps.py)


## Project Instructions
Udacity learners were given starter code and instructions on what the final code should consist of. The `Player` class in the starter code always makes the same move.

Every game looks like this:
```
Game start!
Round 0:
Player 1: rock  Player 2: rock
Round 1:
Player 1: rock  Player 2: rock
Round 2:
Player 1: rock  Player 2: rock
Game over!
```

- Create player subclasses which all choose their moves (rock, paper, scissors) differently. 
  - `HumanPlayer` allows a human player to input their moves into the game.
  - `RandomPlayer` creates a computer player which chooses its moves at random.
  - `ReflectPlayer` creates a computer player which remembers and reflects the `HumanPlayer`'s last move. Its first move is chosen at random.
  - `CyclePlayer` creates a computer player which remembers its last move and cycles through the remaining moves. Its first move is chosen at random.
- Announce the winner of each round.
- Keep score of each round won.
- Show the scoreboard at the end of the game.
- Allow the human player to input their moves without crashing the program. I created a `valid_input` function so players can enter their response in uppercase or lowercase. If the input is not vaild the program will display `'Sorry, I don't understand.'` and ask for input again.
- Ask if the player wants to play again.

### [Udacity's Starter Code](https://video.udacity-data.com/topher/2021/August/6128db63_rps-starter-code/rps-starter-code.py)
```
#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
    ```
