
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

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


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


def put_ship_on_row(board, i, j, columns_len, ship_len, row_restriction, occupied_row_grids):

    ship_index = ship_len
    available_positions = columns_len - j

    if (occupied_row_grids >= row_restriction) or ((occupied_row_grids+ship_len) >= row_restriction):
        return
    if not is_valid_position(board, i, j, ship_len, HORIZONTAL_DIRECTION):
        return

    if ship_len > available_positions:
        return
    
    for k in range(0, ship_len):
        board[i+k][j] = ship_index

def put_ship_on_column(board, i, j, rows_len, ship_len, columns_restriction, occupied_column_grids):

    ship_index = ship_len
    available_positions = rows_len - j

    if (occupied_column_grids >= columns_restriction) or ((occupied_column_grids+ship_len) > columns_restriction):
        return

    if not is_valid_position(board, i, j, ship_len, VERTICAL_DIRECTION):
        return

    if ship_len > available_positions:
        return
    
    for k in range(0, ship_len):
        board[i][j+k] = ship_index
        
        
def remove_ship_on_row(board, i, j, ship_len):
    for k in range(0, ship_len):
        board[i][j+k] = 0


def remove_ship_on_column(board, i, j, ship_len):
    for k in range(0, ship_len):
        board[i+k][j] = 0
        
def move_to_next_position(board, row_index, column_index, rows_restrictions, columns_restrictions,
                          occupied_row_grids, occupied_column_grids, rows_len, columns_len, ship_list, ship_list_index):

    if (column_index + 1) >= columns_len:
        return build_game_board_aux(game_board=board, current_row=row_index+1, current_column=0,
                                    rows_restrictions=rows_restrictions, columns_restrictions=columns_restrictions,
                                    occupied_row_grids=occupied_row_grids, occupied_column_grids=occupied_column_grids,
                                    rows_len=rows_len, columns_len=columns_len, ships=ship_list,
                                    current_ship_index=ship_list_index+1)
    else:        
       return build_game_board_aux(game_board=board, current_row=row_index, current_column=column_index+1,
                                   rows_restrictions=rows_restrictions, columns_restrictions=columns_restrictions,
                                   occupied_row_grids=occupied_row_grids, occupied_column_grids=occupied_column_grids,
                                   rows_len=rows_len, columns_len=columns_len, ships=ship_list,
                                   current_ship_index=ship_list_index+1)


# ACTUALIZACION DE LA FUNCION
def build(game_board, current_row, current_column, rows_restrictions, columns_restrictions, occupied_rows_grids,
          occupied_columns_grids, rows_amount, columns_amount, ships, current_ship_index):

    # Corto la recursión se me salí del tablero.
    if (current_row >= rows_amount) or (current_column >= columns_amount) or (len(ships) == 0):
        return game_board

    occupied_rows_grids_copy = occupied_rows_grids.copy()
    occupied_columns_grids_copy = occupied_columns_grids.copy()

    ships_copy = ships.copy()
    ships_amount = len(ships_copy)
    current_ship_len = ships_copy[current_ship_index]

    game_board_copy = game_board.copy()


    return





def build_game_board_aux(game_board, current_row, current_column, rows_restrictions, occupied_rows_grids,
                         occupied_columns_grids, columns_restrictions, rows_len, columns_len, ships, current_ship_index):

    occupied_rows_grids_copy = occupied_rows_grids.copy()
    occupied_columns_grids_copy = occupied_columns_grids.copy()

    ships_copy = ships.copy()
    ships_amount = len(ships_copy)
    game_board_copy = game_board.copy()
    current_ship_len = ships_copy[current_ship_index]

    if (current_row >= rows_len) or (current_column >= columns_len):
        return game_board_copy

    if ships_amount == 0:
        return game_board_copy

    #Pongo el barco a lo largo.
    if (occupied_rows_grids_copy[current_row] + current_ship_len <= rows_restrictions[current_row]):

        put_ship_on_row(board=game_board_copy, i=current_row, j=current_column, columns_len=columns_len,
                    ship_len=current_ship_len, row_restriction=rows_restrictions[current_ship_index],
                    occupied_row_grids=occupied_rows_grids_copy[current_ship_index])
        move_to_next_position(board=game_board_copy, row_index=current_row, column_index=current_column,
                          rows_restrictions=rows_restrictions, columns_restrictions=columns_restrictions,
                          occupied_row_grids=occupied_row_grids, occupied_column_grids=occupied_column_grids,
                          rows_len=rows_len, columns_len=columns_len, ship_list=ships_copy,
                          ship_list_index=current_ship_index)
        remove_ship_on_row(game_board_copy, current_row, current_column, current_ship_len)

    #Pongo el barco a lo an
    if (occupied_columns_grids_copy[current_column] + current_ship_len <= columns_restrictions[current_column]):
        put_ship_on_column(game_board_copy, current_row, current_column, rows_len, current_ship_len)
        move_to_next_position(board=game_board_copy, row_index=current_row, column_index=current_column,
                              rows_restrictions=rows_restrictions, columns_restrictions=columns_restrictions,
                              occupied_row_grids=occupied_row_grids, occupied_column_grids=occupied_column_grids,
                              rows_len=rows_len, columns_len=columns_len, ship_list=ships_copy,
                              ship_list_index=current_ship_index)
        remove_ship_on_column(game_board_copy, current_row, current_column, current_ship_len)
    
    # Me quedo en el mismo lugar pero considero otro barco.
    build_game_board_aux(game_board=game_board_copy, current_row=current_row, current_column=current_column,
                         rows_restrictions=rows_restrictions, columns_restrictions=columns_restrictions,
                         occupied_row_grids=occupied_row_grids, occupied_column_grids=occupied_column_grids,
                         rows_len=rows_len, columns_len=columns_len, ships=ships_copy,
                         current_ship_index=current_ship_index+ 1)
    
    # Avanzo al siguiente lugar pero con el mismo barco
    move_to_next_position(board=game_board_copy, row_index=current_row, column_index=current_column,
                          rows_restrictions=rows_restrictions, columns_restrictions=columns_restrictions,
                          occupied_row_grids=occupied_row_grids, occupied_column_grids=occupied_column_grids,
                          rows_len=rows_len, columns_len=columns_len, ship_list=ships_copy,
                          ship_list_index=current_ship_index-1)
    
    # Elimino el barco
    ships.pop(current_ship_index)
    return build_game_board_aux(game_board=game_board_copy, current_row=current_row, current_column=current_column,
                                rows_restrictions=rows_restrictions, rows_len=rows_len, columns_len=columns_len,
                                occupied_row_grids=occupied_row_grids, occupied_column_grids=occupied_column_grids,
                                columns_restrictions=columns_restrictions, ships=ships_copy,
                                current_ship_index=current_ship_index)
    

def build_game_board(rows_restrictions, columns_restrictions, ship_list):
    
    game_board = [[0 for _ in range(len(rows_restrictions))] for _ in range(len(columns_restrictions))]

    print_matrix(game_board)

    rows_len = len(rows_restrictions)
    columns_len = len(columns_restrictions)

    occupied_row_grids = [0]*rows_len
    occupied_column_grids = [0]*columns_len

    build_game_board_aux(game_board=game_board, current_row=0, current_column=0, rows_restrictions=rows_restrictions,
                         occupied_row_grids=occupied_row_grids, occupied_column_grids=occupied_column_grids,
                         columns_restrictions=columns_restrictions, rows_len=rows_len, columns_len=columns_len,
                         ships=ship_list, current_ship_index=0)
    return game_board


build_game_board([3,1,2], [3,2,0], [1,1])
