HORIZONTAL_DIRECTION = "HORIZONTAL"
VERTICAL_DIRECTION = "VERTICAL"

LEFT_DOWN_DIAGONAL_INDEX = (-1,-1)
LEFT_INDEX = (-1,0)
LEFT_TOP_DIAGONAL_INDEX =(-1, 1)

DOWN_INDEX = (0, -1)
TOP_INDEX = (0, 1)

RIGHT_DOWN_DIAGONAL_INDEX = (1, -1)
RIGHT_INDEX = (1, 0)
RIGHT_TOP_INDEX = (1,1)


def is_valid_position(board, i, j, ship_len, ship_direction):
    rows_amount = len(board)
    columns_amount = len(board[0])

    neighbors_directions = [
        LEFT_DOWN_DIAGONAL_INDEX, LEFT_INDEX, LEFT_TOP_DIAGONAL_INDEX,
        DOWN_INDEX, TOP_INDEX, RIGHT_DOWN_DIAGONAL_INDEX, RIGHT_INDEX, RIGHT_TOP_INDEX,
    ]

    if ship_direction == HORIZONTAL_DIRECTION:
        if j + ship_len > columns_amount:
            return False

        for k in range(ship_len):
            actual_i, actual_j = i, j + k

            if board[actual_i][actual_j] != 0:
                return False

            for (dx, dy) in neighbors_directions:
                neighbor_i, neighbor_j = actual_i + dx, actual_j + dy
                if (0 <= neighbor_i < rows_amount) and (0 <= neighbor_j < columns_amount):
                    if board[neighbor_i][neighbor_j] != 0:
                        return False

    elif ship_direction == VERTICAL_DIRECTION:
        if i + ship_len > rows_amount:
            return False

        for k in range(ship_len):
            actual_i, actual_j = i + k, j

            if board[actual_i][actual_j] != 0:
                return False

            for (dx, dy) in neighbors_directions:
                neighbor_i, neighbor_j = actual_i + dx, actual_j + dy
                if (0 <= neighbor_i < rows_amount) and (0 <= neighbor_j < columns_amount):
                    if board[neighbor_i][neighbor_j] != 0:
                        return False

    else:
        raise ValueError("The direction must be 'horizontal' or 'vertical'")

    return True


def put_ship_on_row(game_board, current_row, current_column, ship_len, ship_id, rows_occupation,
                    columns_occupation):

    for k in range(0, ship_len):
        game_board[current_row][current_column+k] = ship_id
        columns_occupation[current_column+k] += 1

    rows_occupation[current_row] += ship_len

    return True

def put_ship_on_column(game_board, current_row, current_column, ship_len, ship_id, rows_occupation,
                       columns_occupation):

    for k in range(0, ship_len):
        game_board[current_row + k][current_column] = ship_id
        rows_occupation[current_row+k] += 1

    columns_occupation[current_column] += ship_len

    return True

def remove_ship_on_row(board, current_row, current_column, ship_len, rows_occupation, columns_occupation):
    for k in range(0, ship_len):
        board[current_row][current_column+k] = 0
        columns_occupation[current_column+k] -= 1

    rows_occupation[current_row] -= ship_len


def remove_ship_on_column(board, current_row, current_column, ship_len, rows_occupation, columns_occupation):
    for k in range(0, ship_len):
        board[current_row+k][current_column] = 0
        rows_occupation[current_row+k] -= 1

    columns_occupation[current_column] -= ship_len