from wsgiref.util import shift_path_info

HORIZONTAL_DIRECTION = "HORIZONTAL"
VERTICAL_DIRECTION = "VERTICAL"

GAME_BOARD = 0
PENDING_DEMAND = 1
LAST_USED_SHIP = 2

from part_III.libs import ships_operations
from common_libs import datasets_parser_partIII

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def horizontal_combination(ships, current_ship_index, game_board, rows_restrictions, columns_restrictions,
                        best_local_solution, best_global_solution, current_row, current_column):

    current_ship_len = ships[current_ship_index]
    ship_id = current_ship_index + 1  # IDs para distinguir a los barcos.

    # Se pone el barco actual a lo largo.
    ships_operations.put_ship_on_row(game_board=game_board, current_row=current_row, current_column=current_column,
                                     ship_len=current_ship_len, ship_id=ship_id, rows_restrictions=rows_restrictions,
                                     columns_restrictions=columns_restrictions)

    best_local_solution[PENDING_DEMAND] = sum(rows_restrictions) + sum(columns_restrictions)
    best_local_solution[GAME_BOARD] = game_board.copy()
    best_local_solution[LAST_USED_SHIP] = current_ship_len

    if best_local_solution[PENDING_DEMAND] < best_global_solution[PENDING_DEMAND]:
        build_best_solution(ships, current_ship_index+1, game_board, rows_restrictions, columns_restrictions,
                            best_local_solution, best_global_solution, current_row, current_column)

    # Se elimina el barco.
    ships_operations.remove_ship_on_row(board=game_board, current_row=current_row, current_column=current_column,
                                        ship_len=current_ship_len, rows_restrictions=rows_restrictions,
                                        columns_restrictions=columns_restrictions)


def vertical_combination(ships, current_ship_index, game_board, rows_restrictions, columns_restrictions,
                           best_local_solution, best_global_solution, current_row, current_column):

    current_ship_len = ships[current_ship_index]
    ship_id = current_ship_index + 1  # IDs para distinguir a los barcos.

    # Se pone el barco actual a lo ancho.
    ships_operations.put_ship_on_column(game_board=game_board, current_row=current_row, current_column=current_column,
                                     ship_len=current_ship_len, ship_id=ship_id, rows_restrictions=rows_restrictions,
                                     columns_restrictions=columns_restrictions)

    best_local_solution[PENDING_DEMAND] = sum(rows_restrictions) + sum(columns_restrictions)
    best_local_solution[GAME_BOARD] = game_board.copy()
    best_local_solution[LAST_USED_SHIP] = current_ship_len

    if best_local_solution[PENDING_DEMAND] < best_global_solution[PENDING_DEMAND]:
        build_best_solution(ships=ships, current_ship_index=current_ship_index + 1, game_board=game_board,
                            rows_restrictions=rows_restrictions, columns_restrictions=columns_restrictions,
                            best_local_solution=best_local_solution, best_global_solution=best_global_solution,
                            current_row=current_row, current_column=current_column)

    # Se elimina el barco.
    ships_operations.remove_ship_on_column(board=game_board, current_row=current_row, current_column=current_column,
                                        ship_len=current_ship_len, rows_restrictions=rows_restrictions,
                                        columns_restrictions=columns_restrictions)


def build_best_solution(ships, current_ship_index, game_board, rows_restrictions, columns_restrictions,
                        best_local_solution, best_global_solution, current_row, current_column):

    # Actualizo el óptimo global si el óptimo local es mejor.
    if best_local_solution[PENDING_DEMAND] < best_global_solution[PENDING_DEMAND]:
        best_global_solution[GAME_BOARD] = best_local_solution[GAME_BOARD].copy()
        best_global_solution[PENDING_DEMAND] = best_local_solution[PENDING_DEMAND]
        best_global_solution[LAST_USED_SHIP] = best_local_solution[LAST_USED_SHIP]

    if current_ship_index >= len(ships):
        return

    current_ship_len = ships[current_ship_index]

    if best_local_solution[LAST_USED_SHIP] == current_ship_len :
          build_best_solution(ships, current_ship_index+1, game_board, rows_restrictions, columns_restrictions,
                            best_local_solution, best_global_solution, current_row, current_column)

    for i in range(len(rows_restrictions)):
        for j in range(len(columns_restrictions)):

            # Pongo el barco actual a lo largo.
            horizontal_combination(ships, current_ship_index, game_board, rows_restrictions, columns_restrictions,
                                       best_local_solution, best_global_solution, i, j)
            # Pongo el barco actual a lo ancho.
            vertical_combination(ships, current_ship_index, game_board, rows_restrictions, columns_restrictions,
                                       best_local_solution, best_global_solution, i, j)

    # No pongo el barco actual en ningún lado.
    return build_best_solution(ships, current_ship_index+1, game_board, rows_restrictions, columns_restrictions,
                               best_local_solution, best_global_solution, current_row, current_column)

def build_best_game_board(rows_restrictions, columns_restrictions, ships):

    game_board = [[0 for _ in range(len(rows_restrictions))] for _ in range(len(columns_restrictions))]

    total_demand = sum(rows_restrictions) + sum(columns_restrictions)
    last_used_ship = -1 # Al principio no se uso ningun barco

    best_local_solution = [game_board.copy(), total_demand, last_used_ship]
    best_global_solution = [game_board.copy(), total_demand, last_used_ship]

    build_best_solution(ships, 0, game_board, rows_restrictions, columns_restrictions,
                        best_local_solution, best_global_solution, 0, 0)

    return best_global_solution[GAME_BOARD]


def build_game_board(dataset_name):
    rows_restrictions, columns_restrictions, ships_list = (datasets_parser_partIII
                                                          .parse_dataset("datasets_partIII/",dataset_name))
    return build_best_game_board(rows_restrictions, columns_restrictions, ships_list)


game_board = build_game_board("3_3_2.txt")

print_matrix(game_board)