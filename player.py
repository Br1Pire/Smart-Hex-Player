import random
import HexBoard

class Player:
    def __init__(self, player_id: int):
        self.player_id = player_id  # Tu identificador (1 o 2)

    def play(self, board: HexBoard) -> tuple:
        raise NotImplementedError("¡Implementa este método!")

class SmartPlayer(Player):
    def __init__(self, player_id: int):
        super().__init__(player_id)

    def play(self, board: HexBoard) -> tuple:
        possible_moves = board.get_possible_moves()

        best_score = float('-inf')
        best_move = []

        for move in possible_moves:
            aux_board = board.clone()
            aux_board.place_piece(move[0], move[1], self.player_id)

            score = self.minimax(aux_board,3, float('-inf'), float('inf'), False)

            if score > best_score:
                best_score = score
                best_move = move
            elif score == best_score:
                best_move.append(move)

            return random.choice(best_move)

    def minimax(self, board, depth, alpha, beta, maximizing):
        if depth == 0 or board.check_connection(self.player_id) :
            return self.evaluate_board(board)

        possible_moves = board.get_possible_moves()
        current_player = self.player_id if maximizing else 3 - self.player_id

        if maximizing:
            max_eval = float("-inf")
            for move in possible_moves:
                aux = board.clone()
                aux.place_piece(move[0], move[1], current_player)
                eval = self.minimax(aux, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float("inf")
            for move in possible_moves:
                aux = board.clone()
                aux.place_piece(move[0], move[1], current_player)
                eval = self.minimax(aux, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval   
        
    def evaluate_board(self, board):
        
        return random.randint(1, 100)