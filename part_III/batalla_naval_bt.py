from wsgiref.util import shift_path_info
from part_III.libs import ships_operations
from common_libs import datasets_parser_partIII

import copy

HORIZONTAL_DIRECTION = "HORIZONTAL"
VERTICAL_DIRECTION = "VERTICAL"

GAME_BOARD = 0
PENDING_DEMAND = 1
LAST_USED_SHIP = 2

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def get_most_demanded_indexes(restrictions):
    return sorted(range(len(restrictions)), key=lambda i: restrictions[i], reverse=True)


def horizontal_combination(ships, current_ship_index, game_board, rows_restrictions, columns_restrictions,
                        best_local_solution, best_global_solution, current_row, current_column):

    current_ship_len = ships[current_ship_index]
    ship_id = current_ship_index + 1  # IDs para distinguir a los barcos.

    # Se pone el barco actual a lo largo.
    can_put_ship = ships_operations.put_ship_on_row(game_board, current_row, current_column, current_ship_len,
                                                    ship_id, rows_restrictions,columns_restrictions)

    if can_put_ship:

        best_local_solution[PENDING_DEMAND] = sum(rows_restrictions) + sum(columns_restrictions)
        best_local_solution[GAME_BOARD] = copy.deepcopy(game_board)
        best_local_solution[LAST_USED_SHIP] = current_ship_len

        if best_local_solution[PENDING_DEMAND] < best_global_solution[PENDING_DEMAND]:
            build_best_solution(ships, current_ship_index+1, game_board, rows_restrictions, columns_restrictions,
                                best_local_solution, best_global_solution, current_row, current_column)

        # Se elimina el barco.
        ships_operations.remove_ship_on_row(game_board, current_row, current_column,current_ship_len, rows_restrictions,
                                            columns_restrictions)


def vertical_combination(ships, current_ship_index, game_board, rows_restrictions, columns_restrictions,
                           best_local_solution, best_global_solution, current_row, current_column):

    current_ship_len = ships[current_ship_index]
    ship_id = current_ship_index + 1  # IDs para distinguir a los barcos.

    # Se pone el barco actual a lo ancho.
    can_put_ship = ships_operations.put_ship_on_column(game_board=game_board, current_row=current_row,
                                                       current_column=current_column, ship_len=current_ship_len, ship_id=ship_id,
                                                       rows_occupation=rows_restrictions, columns_occupation=columns_restrictions)

    if can_put_ship:

        best_local_solution[PENDING_DEMAND] = sum(rows_restrictions) + sum(columns_restrictions)
        best_local_solution[GAME_BOARD] = copy.deepcopy(game_board)
        best_local_solution[LAST_USED_SHIP] = current_ship_len

        if best_local_solution[PENDING_DEMAND] < best_global_solution[PENDING_DEMAND]:
            build_best_solution(ships=ships, current_ship_index=current_ship_index + 1, game_board=game_board,
                                rows_restrictions=rows_restrictions, columns_restrictions=columns_restrictions,
                                best_local_solution=best_local_solution, best_global_solution=best_global_solution,
                                current_row=current_row, current_column=current_column)

        # Se elimina el barco.
        ships_operations.remove_ship_on_column(board=game_board, current_row=current_row, current_column=current_column,
                                               ship_len=current_ship_len, rows_occupation=rows_restrictions,
                                               columns=columns_restrictions)

def build_best_solution(ships, current_ship_index, game_board, rows_restrictions, columns_restrictions,
                        best_local_solution, best_global_solution, current_row, current_column):

    # Actualizo el óptimo global si el óptimo local es mejor.
    if best_local_solution[PENDING_DEMAND] < best_global_solution[PENDING_DEMAND]:
        best_global_solution[GAME_BOARD] = copy.deepcopy(best_local_solution[GAME_BOARD])
        best_global_solution[PENDING_DEMAND] = best_local_solution[PENDING_DEMAND]
        best_global_solution[LAST_USED_SHIP] = best_local_solution[LAST_USED_SHIP]

    if current_ship_index >= len(ships):
        return

    current_ship_len = ships[current_ship_index]

    if (best_local_solution[PENDING_DEMAND] - sum(ships[current_ship_index:])*2) >= best_global_solution[PENDING_DEMAND]:
        return

    if ((best_local_solution[LAST_USED_SHIP] == current_ship_len) and
        ((current_ship_len > rows_restrictions[current_row]) or
        (current_ship_len > columns_restrictions[current_column]))):

        build_best_solution(ships, current_ship_index+1, game_board, rows_restrictions, columns_restrictions,
                            best_local_solution, best_global_solution, current_row, current_column)
        return

    most_demanded_rows = get_most_demanded_indexes(rows_restrictions)
    most_demanded_columns = get_most_demanded_indexes(columns_restrictions)

    for i in most_demanded_rows:
        for j in most_demanded_columns:

            # Pongo el barco actual a lo largo.
            horizontal_combination(ships, current_ship_index, game_board, rows_restrictions, columns_restrictions,
                                       best_local_solution, best_global_solution, i, j)
            # Pongo el barco actual a lo ancho.
            vertical_combination(ships, current_ship_index, game_board, rows_restrictions, columns_restrictions,
                                       best_local_solution, best_global_solution, i, j)

    # No pongo el barco actual en ningún lado.
    build_best_solution(ships, current_ship_index+1, game_board, rows_restrictions, columns_restrictions,
                               best_local_solution, best_global_solution, current_row, current_column)
    return


def build_best_game_board(rows_restrictions, columns_restrictions, ships):

    game_board = [[0 for _ in range(len(rows_restrictions))] for _ in range(len(columns_restrictions))]

    total_demand = sum(rows_restrictions) + sum(columns_restrictions)
    last_used_ship = -1 # Al principio no se uso ningun barco

    best_local_solution = [copy.deepcopy(game_board), total_demand, last_used_ship]
    best_global_solution = [copy.deepcopy(game_board), total_demand, last_used_ship]

    build_best_solution(ships, 0, game_board, rows_restrictions, columns_restrictions,
                        best_local_solution, best_global_solution, 0, 0)

    return best_global_solution


def build_game_board(dataset_name):
    rows_restrictions, columns_restrictions, ships_list = (datasets_parser_partIII
                                                          .parse_dataset("datasets_partIII/",dataset_name))

    return build_best_game_board(rows_restrictions, columns_restrictions, ships_list)

best_solution = build_game_board("5_5_6.txt")

print_matrix(best_solution[GAME_BOARD])
print(f"Demanda pendiente: {best_solution[PENDING_DEMAND]}")