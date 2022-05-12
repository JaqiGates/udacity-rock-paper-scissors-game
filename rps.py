import random
moves = ['rock', 'paper', 'scissors']


def valid_input(prompt, op1, op2, op3):
    while True:
        response = input(prompt).lower()
        if op1 == response:
            break
        elif op2 == response:
            break
        elif op3 == response:
            break
        else:
            print("Sorry, I don't understand.\n")
    return response


def player_type():
    players = [Player(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    return random.choice(players)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:

    def __init__(self):
        self.my_move = None
        self.their_move = None

    def move(self):
        # Always returns 'rock'.
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class HumanPlayer(Player):
    def move(self):
        response = valid_input("Rock, paper, or scissors?\n~ ",
                               "rock", "paper", "scissors")
        return response


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        elif self.their_move in moves:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            index = moves.index(self.my_move) + 1
            if index == len(moves):
                index = 0
            return moves[index]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        while True:
            if move1 == move2:
                print("**It's a tie!**\n")
            elif beats(move1, move2) is True:
                print("**Player 1 wins!**\n")
                self.p1.count += 1
            else:
                print("**Player 2 wins!**\n")
                self.p2.count += 1
            return self.p1.count and self.p2.count

    def play_game(self):
        self.p1.count = 0
        self.p2.count = 0
        print("\nRock, paper, scissors, GO!\n")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!\n")
        print(f"SCOREBOARD:\n"
              f"Player 1: {self.p1.count}\n"
              f"Player 2: {self.p2.count}\n")

    def play_again(self):
        response = valid_input("Would you like to play again? "
                               "(yes, no, maybe)\n~ ", "yes", "no", "maybe")
        if "yes" in response:
            print("\nGreat!")
            self.play_game()
        elif "no" in response:
            print("\nThanks for playing!\n")
            exit()
        elif "maybe" in response:
            print("\nLet's just play again...")
            self.play_game()


if __name__ == '__main__':

    game = Game(HumanPlayer(), player_type())
    game.play_game()

    while True:
        game = Game(HumanPlayer(), player_type())
        game.play_again()
