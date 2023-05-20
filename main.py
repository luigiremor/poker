
from model.game import Game
from model.player import Player


def main():

    game = Game()

    player_1 = Player("Player 1", 100)
    player_2 = Player("Player 2", 100)
    player_3 = Player("Player 3", 100)
    player_4 = Player("Player 4", 100)
    player_5 = Player("Player 5", 100)

    game.add_player(player_1)
    game.add_player(player_2)
    game.add_player(player_3)
    game.add_player(player_4)
    game.add_player(player_5)

    game.run()


if __name__ == "__main__":
    main()
