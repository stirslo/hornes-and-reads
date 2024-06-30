from game import Game

game = input("What is your favorite game? ")

if game == "Hornes and Reads":
    print("I made that game you know!")
    game = Game()
    game.play()

elif game == "LEGO Harry Potter":
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
