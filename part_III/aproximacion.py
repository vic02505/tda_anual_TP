from common_libs.datasets_parser_partIII import parse_dataset

HORIZONTAL = "horizontal"
VERTICAL = "vertical"

def horizontal_pos_available(board, row, col, ship_len):
    if col + ship_len > len(board[0]):
        return False
    for c in range(col, col + ship_len):
        if board[row][c] != 0:
            return False
    return True

def vertical_pos_available(board, row, col, ship_len):
    if row + ship_len > len(board):
        return False
    for r in range(row, row + ship_len):
        if board[r][col] != 0:
            return False
    return True

def position_horizontal(board, row, col, ship_len, ship_id, row_demand, col_demand):
    for c in range(col, col + ship_len):
        board[row][c] = ship_id
        col_demand[c] -= 1
    row_demand[row] -= ship_len

def position_vertical(board, row, col, ship_len, ship_id, row_demand, col_demand):
    for r in range(row, row + ship_len):
        board[r][col] = ship_id
        row_demand[r] -= 1
    col_demand[col] -= ship_len

def battleship_approximation(n, m, row_demand, col_demand, ships):
    game_board = [[0 for _ in range(m)] for _ in range(n)]
    row_demand_available = row_demand[:]
    col_demand_available = col_demand[:]
    ships_in_game = []

    ship_id = 1

    for ship in ships:
        in_game = False

        possible_positions = []
        for i in range(n):
            if row_demand_available[i] >= ship:
                possible_positions.append((i, HORIZONTAL, row_demand_available[i]))
        for j in range(m):
            if col_demand_available[j] >= ship:
                possible_positions.append((j, VERTICAL, col_demand_available[j]))

        possible_positions.sort(key=lambda x: x[2], reverse=True)

        for position, orientation, _ in possible_positions:
            if orientation == HORIZONTAL:
                for col in range(m - ship + 1):
                    if horizontal_pos_available(game_board, position, col, ship):
                        position_horizontal(game_board, position, col, ship, ship_id, row_demand_available, col_demand_available)
                        ships_in_game.append(ship)
                        in_game = True
                        break
            elif orientation == VERTICAL:
                for row in range(n - ship + 1):
                    if vertical_pos_available(game_board, row, position, ship):
                        position_vertical(game_board, row, position, ship, ship_id, row_demand_available, col_demand_available)
                        ships_in_game.append(ship)
                        in_game = True
                        break
            if in_game:
                break

        if not in_game:
            continue

        ship_id += 1

    aproximation = sum(ships_in_game)
    return game_board, aproximation

def build_game_board(dataset_name):
    row_demand, col_demand, ships = parse_dataset("datasets_partIII/", dataset_name)
    n = len(row_demand)
    m = len(col_demand)
    return battleship_approximation(n, m, row_demand, col_demand, ships)

datasets = ["3_3_2.txt", "5_5_6.txt", "8_7_10.txt" ,"10_3_3.txt", "10_10_10.txt", "12_12_21.txt",
              "15_10_15.txt", "20_20_20.txt", "20_25_30.txt", "30_25_25.txt"]

for dataset in datasets:
    print(f"\ninstancia: {dataset}")
    game_board, aproximation = build_game_board(dataset)

    # for row in game_board:
    #     print(" ".join(map(str, row)))

    print(f"Aproximación: {aproximation}")
