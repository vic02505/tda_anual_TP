from part_III.libs import ships_operations
from common_libs import datasets_parser_partIII
import copy

HORIZONTAL_DIRECTION = "HORIZONTAL"
VERTICAL_DIRECTION = "VERTICAL"

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def generate_rows_combinations(board, rows_restrictions, rows_occupation,
                               columns_restrictions, columns_occupation, current_ship_len):

    rows_combinations = []
    rows_amount = len(rows_restrictions)
    columns_amount = len(columns_restrictions)
    
    for i, row in enumerate(board):
       
        if (rows_occupation[i] + current_ship_len) > rows_restrictions[i]:
            continue
       
        adjacent_grids = 0
        
        for j in range(columns_amount):
            
            if (board[i][j] == 0) and (columns_occupation[j] < columns_restrictions[j]):
                adjacent_grids += 1
            else: 
                adjacent_grids = 0
                
            if adjacent_grids == current_ship_len:
                ship_begin_position = j - current_ship_len + 1

                if ships_operations.is_valid_position(board, i, ship_begin_position, current_ship_len,HORIZONTAL_DIRECTION):
                    rows_combinations.append((i, ship_begin_position))
                adjacent_grids -= 1

    return rows_combinations


def generate_columns_combinations(board, rows_restrictions, rows_occupation,
                               columns_restrictions, columns_occupation, current_ship_len):
    columns_combinations = []
    rows_amount = len(rows_restrictions)
    columns_amount = len(columns_restrictions)

    for j in range(columns_amount):
        if (columns_occupation[j] + current_ship_len) > columns_restrictions[j]:
            continue

        adjacent_grids = 0

        for i in range(rows_amount):

            if (board[i][j] == 0) and (rows_occupation[i] < rows_restrictions[i]):
                adjacent_grids += 1
            else:
                adjacent_grids = 0

            if adjacent_grids == current_ship_len:
                ship_begin_position = i - current_ship_len + 1

                if ships_operations.is_valid_position(board, ship_begin_position, j, current_ship_len, VERTICAL_DIRECTION):
                    columns_combinations.append((ship_begin_position, j))
                adjacent_grids -= 1

    return columns_combinations


def try_horizontal_combinations(ships, current_ship_index, board, rows_restrictions, columns_restrictions,
                                rows_occupation, columns_occupation, local_solution, global_solution):


    current_ship_len = ships[current_ship_index]
    ship_id = current_ship_index + 1  # IDs para distinguir a los barcos.

    best_board = copy.deepcopy(board)

    rows_combinations = generate_rows_combinations(board=board, rows_restrictions=rows_restrictions,
                                                        rows_occupation=rows_occupation,
                                                        columns_restrictions=columns_restrictions,
                                                   columns_occupation=columns_occupation,
                                                        current_ship_len=current_ship_len)


    for row, ship_begin_position in rows_combinations:

        can_put_ship = ships_operations.put_ship_on_row(game_board=board, current_row=row,
                                                        current_column=ship_begin_position, ship_len=current_ship_len,
                                                        ship_id=ship_id, rows_occupation=rows_occupation,
                                                        columns_occupation=columns_occupation)
        if can_put_ship:

            local_solution_aux = local_solution + (ships[current_ship_index] * 2)

            board_aux, local_solution_aux = build_game_board_bt(ships=ships, current_ship_index=current_ship_index+1,
                                                            game_board=board, rows_restrictions=rows_restrictions,
                                                            columns_restrictions=columns_restrictions,
                                                            rows_occupation=rows_occupation,
                                                            columns_occupation=columns_occupation,
                                                            local_solution=local_solution_aux,
                                                            global_solution=global_solution)

            if local_solution_aux > global_solution:
                global_solution = local_solution_aux
                best_board = copy.deepcopy(board_aux)

            ships_operations.remove_ship_on_row(board, row, ship_begin_position, current_ship_len,
                                                rows_occupation,columns_occupation)

    return best_board, global_solution


def try_vertical_combinations(ships, current_ship_index, board, rows_restrictions, columns_restrictions,
                                rows_occupation, columns_occupation, local_solution, global_solution):


    current_ship_len = ships[current_ship_index]
    ship_id = current_ship_index + 1  # IDs para distinguir a los barcos.

    best_board = copy.deepcopy(board)

    columns_combination = generate_columns_combinations(board=board, rows_restrictions=rows_restrictions,
                                                        rows_occupation=rows_occupation,
                                                        columns_restrictions=columns_restrictions,
                                                   columns_occupation=columns_occupation,
                                                        current_ship_len=current_ship_len)

    for ship_begin_position, column in columns_combination:

        can_put_ship = ships_operations.put_ship_on_column(game_board=board, current_row=ship_begin_position,
                                                           current_column=column, ship_len=current_ship_len,
                                                        ship_id=ship_id, rows_occupation=rows_occupation,
                                                           columns_occupation=columns_occupation)
        if can_put_ship:

            local_solution_aux = local_solution + (ships[current_ship_index] * 2)

            board_aux, local_solution_aux = build_game_board_bt(ships=ships, current_ship_index=current_ship_index + 1,
                                                            game_board=board, rows_restrictions=rows_restrictions,
                                                            columns_restrictions=columns_restrictions,
                                                            rows_occupation=rows_occupation,
                                                            columns_occupation=columns_occupation,
                                                            local_solution=local_solution_aux,
                                                            global_solution=global_solution)

            if local_solution_aux > global_solution:
                global_solution = local_solution_aux
                best_board = copy.deepcopy(board_aux)

            ships_operations.remove_ship_on_column(board, ship_begin_position, column, current_ship_len,
                                                rows_occupation,columns_occupation)

    return best_board, global_solution



def build_game_board_bt(ships, current_ship_index, game_board, rows_restrictions,
                        columns_restrictions, rows_occupation, columns_occupation,
                        local_solution, global_solution):

    best_game_board = copy.deepcopy(game_board)

    if local_solution > global_solution:
        global_solution = local_solution

    if current_ship_index >= len(ships):
        return best_game_board, global_solution

    if local_solution + sum(ships[current_ship_index:]*2) <= global_solution:
        return best_game_board, global_solution

    best_game_board = copy.deepcopy(game_board)

    game_board_aux, local_solution_aux = try_horizontal_combinations(ships=ships, current_ship_index=current_ship_index,
                                                                 board=game_board, rows_restrictions=rows_restrictions,
                                                                 columns_restrictions=columns_restrictions,
                                                                 rows_occupation=rows_occupation,
                                                                 columns_occupation=columns_occupation,
                                                                 local_solution=local_solution,
                                                                 global_solution=global_solution)
    if local_solution_aux > global_solution:
        global_solution = local_solution_aux
        best_game_board = copy.deepcopy(game_board_aux)

    game_board_aux, local_solution_aux = try_vertical_combinations(ships=ships, current_ship_index=current_ship_index,
                                                               board=game_board, rows_restrictions=rows_restrictions,
                                                               columns_restrictions=columns_restrictions,
                                                               rows_occupation=rows_occupation,
                                                               columns_occupation=columns_occupation,
                                                               local_solution=local_solution,
                                                               global_solution=global_solution)

    if local_solution_aux > global_solution:
        global_solution = local_solution_aux
        best_game_board = copy.deepcopy(game_board_aux)

    game_board_aux, local_solution_aux = build_game_board_bt(ships=ships, current_ship_index=current_ship_index+1,
                                                         game_board=game_board, rows_restrictions=rows_restrictions,
                                                         columns_restrictions=columns_restrictions,
                                                         rows_occupation=rows_occupation,
                                                         columns_occupation=columns_occupation,
                                                         local_solution=local_solution,
                                                         global_solution=global_solution)

    if local_solution_aux > global_solution:
        global_solution = local_solution_aux
        best_game_board = copy.deepcopy(game_board_aux)

    return best_game_board, global_solution


def build_naval_battle_game_board(dataset_name):
    rows_restrictions, columns_restrictions, ships = (datasets_parser_partIII
                                                          .parse_dataset("local_datasets/",dataset_name))

    game_board = [[0 for _ in range(len(columns_restrictions))] for _ in range(len(rows_restrictions))]
    rows_occupation = [0]*len(rows_restrictions)
    columns_occupation = [0]*len(columns_restrictions)
    ships.sort(reverse=True)


    return build_game_board_bt(ships,0, game_board, rows_restrictions, columns_restrictions,
                               rows_occupation, columns_occupation, 0, 0)


files_name = ["3_3_2.txt", "5_5_6.txt", "8_7_10.txt" ,"10_3_3.txt", "10_10_10.txt", "12_12_21.txt",
              "15_10_15.txt", "20_20_20.txt", "20_25_30.txt", "30_25_25.txt"]


_, score = build_naval_battle_game_board("30_25_25.txt")

print(score)