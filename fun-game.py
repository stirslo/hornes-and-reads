game = input("What is your favorite game? ")

if game == "Hornes and Reads":
    print("I made that game you know!")
    import itertools

    X = "X"

    a1 = a2 = a3 = None
    b1 = b2 = b3 = None
    c1 = c2 = c3 = None

    def winner():
        for player in [1, 2]:
            if a1 == a2 == a3 == player:
                return player
            if b1 == b2 == b3 == player:
                return player
            if c1 == c2 == c3 == player:
                return player
            if a1 == b1 == c1 == player:
                return player
            if a2 == b2 == c2 == player:
                return player
            if a3 == b3 == c3 == player:
                return player
            if a1 == b2 == c3 == player:
                return player
            if c1 == b2 == a3 == player:
                return player

    def make_move(player, move):
        global a1, a2, a3, b1, b2, b3, c1, c2, c3
        if a1 is None and move == "a1":
            a1 = player
        elif a2 is None and move == "a2":
            a2 = player
        elif a3 is None and move == "a3":
            a3 = player
        elif b1 is None and move == "b1":
            b1 = player
        elif b2 is None and move == "b2":
            b2 = player
        elif b3 is None and move == "b3":
            b3 = player
        elif c1 is None and move == "c1":
            c1 = player
        elif c2 is None and move == "c2":
            c2 = player
        elif c3 is None and move == "c3":
            c3 = player
        else:
            print("invalid move")
            return False
        return True

    for player in itertools.cycle([1, 2]):
        while True:
            move = input(f"player {player}? ")
            if make_move(player, move):
                break
        if winner():
            print(f"player {player} wins!")
            break
        elif all([a1, a2, a3, b1, b2, b3, c1, c2, c3]):
            print("It's a draw")
            break


print(
    f"""
{a1 or X} | {b1 or X} | {c1 or X}
{a2 or X} | {b2 or X} | {c2 or X}
{a3 or X} | {b3 or X} | {c3 or X}
"""
)

if game == "LEGO Harry Potter":
    print(
        """
AVADA KADAVRA, you are dead!
I am secretly Voldemort! Mwahahaha!"""
    )

else:
    print(
        """
I do not know of that game?
But it does sound quite fun.
Mayde I'll try it one day?
Who knows?"""
    )
