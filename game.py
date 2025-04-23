import socket
import threading
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
            return False
        return True

    def board_state(self):
        return f"""
{self.a1 or X} | {self.b1 or X} | {self.c1 or X}
{self.a2 or X} | {self.b2 or X} | {self.c2 or X}
{self.a3 or X} | {self.b3 or X} | {self.c3 or X}
"""


class GameServer:
    def __init__(self, host="0.0.0.0", port=12345):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(2)
        print(f"Server started on {host}:{port}")
        self.clients = []
        self.game = Game()

    def handle_client(self, client, player):
        client.sendall(f"Welcome Player {player}!\n".encode())
        if len(self.clients) < 2:
            client.sendall("Waiting for another player to join...\n".encode())

        while len(self.clients) < 2:
            pass  # Wait for the second player to connect

        for current_player in itertools.cycle([1, 2]):
            if current_player != player:
                continue

            client.sendall("Your turn! Enter your move (e.g., a1, b2):\n".encode())
            move = client.recv(1024).decode().strip()

            if not self.game.make_move(player, move):
                client.sendall("Invalid move. Try again.\n".encode())
                continue

            # Broadcast the board state to all players
            board = self.game.board_state()
            for c in self.clients:
                c.sendall(f"Player {player} made a move: {move}\n{board}\n".encode())

            # Check for a winner or draw
            if self.game.winner(player):
                for c in self.clients:
                    c.sendall(f"Player {player} wins!\n".encode())
                break
            elif all(
                [
                    self.game.a1,
                    self.game.a2,
                    self.game.a3,
                    self.game.b1,
                    self.game.b2,
                    self.game.b3,
                    self.game.c1,
                    self.game.c2,
                    self.game.c3,
                ]
            ):
                for c in self.clients:
                    c.sendall("It's a draw!\n".encode())
                break

        client.close()

    def start(self):
        print("Waiting for players to connect...")
        while len(self.clients) < 2:
            client, addr = self.server.accept()
            self.clients.append(client)
            player = len(self.clients)
            print(f"Player {player} connected from {addr}")
            threading.Thread(target=self.handle_client, args=(client, player)).start()


if __name__ == "__main__":
    server = GameServer()
    server.start()
