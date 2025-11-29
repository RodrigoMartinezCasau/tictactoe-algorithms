def row_winner(board):
    for row in board.grid:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    return None


def column_winner(board):
    for col in range(board.size):
        if (board.grid[0][col] == board.grid[1][col] ==
            board.grid[2][col] != " "):
            return board.grid[0][col]
    return None


def diagonal_winner(board):
    # Diagonal principal
    if (board.grid[0][0] == board.grid[1][1] ==
        board.grid[2][2] != " "):
        return board.grid[0][0]

    # Diagonal secundaria
    if (board.grid[0][2] == board.grid[1][1] ==
        board.grid[2][0] != " "):
        return board.grid[0][2]

    return None


def check_winner(board):
    """
    Devuelve 'X' o 'O' si hay ganador, None si no.
    Complejidad: O(1).
    """
    return (
        row_winner(board) or
        column_winner(board) or
        diagonal_winner(board)
    )
