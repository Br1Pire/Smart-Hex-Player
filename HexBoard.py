class HexBoard:
    def __init__(self, size: int):
        self.size = size  # Tamaño N del tablero (NxN)
        self.board = [[0] * size for _ in range(size)]  # Matriz NxN (0=vacío, 1=Jugador1, 2=Jugador2)
        self.player_positions = {1: set(), 2: set()}  # Registro de fichas por jugador

    def clone(self) -> 'HexBoard':
		#Devuelve una copia del tablero actual
        pass

    def place_piece(self, row: int, col: int, player_id: int) -> bool:
        #Coloca una ficha si la casilla está vacía.
        if(not self.board[row][col]):
            self.board[row][col] = player_id

        return self.board[row][col]
           

    def get_possible_moves(self) -> list:
        #Devuelve todas las casillas vacías como tuplas (fila, columna).
        # ret = []
        # for x in range(self.size):
        #     for y in range(self.size):
        #         if (x,y) not in self.player_positions[1] | self.player_positions[2]:
        #             ret.append((x,y))
        return [(x,y) for x in range(self.size) for y in range(self.size) if (x,y) not in self.player_positions[1] | self.player_positions[2]]
                

    
    def check_connection(self, player_id: int) -> bool:
        #Verifica si el jugador ha conectado sus dos lados
        pass

