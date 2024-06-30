import itertools

X = "X"


class Game:
    def __init__(self):
        self.a1 = self.a2 = self.a3 = None
        self.b1 = self.b2 = self.b3 = None
        self.c1 = self.c2 = self.c3 = None

    def winner(self, player):
        if self.a1 == self.a2 == self.a3 == player:
            return player
        if self.b1 == self.b2 == self.b3 == player:
            return player
        if self.c1 == self.c2 == self.c3 == player:
            return player
        if self.a1 == self.b1 == self.c1 == player:
            return player
        if self.a2 == self.b2 == self.c2 == player:
            return player
        if self.a3 == self.b3 == self.c3 == player:
            return player
        if self.a1 == self.b2 == self.c3 == player:
            return player
        if self.c1 == self.b2 == self.a3 == player:
            return player

    def make_move(self, player, move):
        if self.a1 is None and move == "a1":
            self.a1 = player
        elif self.a2 is None and move == "a2":
            self.a2 = player
        elif self.a3 is None and move == "a3":
            self.a3 = player
        elif self.b1 is None and move == "b1":
            self.b1 = player
        elif self.b2 is None and move == "b2":
            self.b2 = player
        elif self.b3 is None and move == "b3":
            self.b3 = player
        elif self.c1 is None and move == "c1":
            self.c1 = player
        elif self.c2 is None and move == "c2":
            self.c2 = player
        elif self.c3 is None and move == "c3":
            self.c3 = player
        else:
            print("invalid move")
            return False
        return True

    def play(self):

        for player in itertools.cycle([1, 2]):
            while True:
                move = input(f"player {player}? ")
                if self.make_move(player, move):
                    break
            if self.winner(player):
                print(f"player {player} wins!")
                break
            elif all(
                [
                    self.a1,
                    self.a2,
                    self.a3,
                    self.b1,
                    self.b2,
                    self.b3,
                    self.c1,
                    self.c2,
                    self.c3,
                ]
            ):
                print("It's a draw")
                break

        print(
            f"""
{self.a1 or X} | {self.b1 or X} | {self.c1 or X}
{self.a2 or X} | {self.b2 or X} | {self.c2 or X}
{self.a3 or X} | {self.b3 or X} | {self.c3 or X}
"""
        )


if __name__ == "__main__":
    game = Game()
    game.play()
