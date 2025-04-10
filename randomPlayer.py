import HexBoard
import player

class RandomPlayer(player):
    def __init__(self, player_id: int):
        self.player_id = player_id  

    def play(self, board: HexBoard) -> tuple:
        