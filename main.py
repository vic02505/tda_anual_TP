from part_I import greedy_coins_game
from part_II import dynamic_coins_game
from part_III import naval_battle_bt
from common_libs import coins_game_output_generator, bt_output_generator

import sys

LOCAL_GREEDY = "local_greedy_"  # Datasets locales greedy
EXTERN_GREEDY = "extern_greedy_" # Datasets externos greedy.

LOCAL_PD = "local_pd_"  # Datasets locales programación dinámica
EXTERN_PD = "extern_pd_" # Datasets externos programación dinámica

LOCAL_BT = "local_bt_"  # Datasets locales backtracking
EXTERN_BT = "extern_bt_" # Datasets externos backtracking

def main(arguments):

    if len(arguments) < 2:
        raise Exception("[ERROR] No se especificaron los flags necesarios para realizar la ejecución!")

    flag = arguments[1]

    if flag == "-a":
        print("[GREEDY] Reproduciendo casos de uso...")
        outputs = greedy_coins_game.run_use_cases("part_I/local_datasets")
        coins_game_output_generator.generate_output_for_greedy(outputs, LOCAL_GREEDY)
        print("[GREEDY] Casos reproducidos.")

        print("[PROGRAMACIÓN DINÁMICA] Reproduciendo casos de uso locales...")
        outputs = dynamic_coins_game.run_use_cases("part_II/local_datasets")
        coins_game_output_generator.generate_output_for_dynamic(outputs, LOCAL_PD)
        print("[PROGRAMACIÓN DINÁMICA] Casos reproducidos.")

        print("[BACKTRACKING] Reproduciendo casos de uso locales...")
        outputs = naval_battle_bt.run_use_cases("part_III/local_datasets")
        bt_output_generator.generate_output_for_bt(outputs, LOCAL_BT)
        print("[BACKTRACKING] Casos reproducidos.")

    elif flag == "-g":

        if len(arguments) > 2:
            if arguments[2] == "-e":
                print("[GREEDY] Reproduciendo casos de uso externos...")
                outputs = greedy_coins_game.run_use_cases("part_I/extern_datasets")
                coins_game_output_generator.generate_output_for_greedy(outputs, EXTERN_GREEDY)
                print("[GREEDY] Casos reproducidos.")
                return
        else:
            print("[GREEDY] Reproduciendo casos de locales...")
            outputs = greedy_coins_game.run_use_cases("part_I/local_datasets")
            coins_game_output_generator.generate_output_for_greedy(outputs, LOCAL_GREEDY)
            print("[GREEDY] Casos reproducidos.")

    elif flag == "-d":

        if len(arguments) > 2:
            if arguments[2] == "-e":
                print("[PROGRAMACIÓN DINÁMICA] Reproduciendo casos de uso externos...")
                dynamic_coins_game.run_use_cases("part_I/extern_datasets")
                print("[PROGRAMACIÓN DINÁMICA] Casos reproducidos.")
                return
        else:
            print("[PROGRAMACIÓN DINÁMICA] Reproduciendo casos de uso locales...")
            outputs = dynamic_coins_game.run_use_cases("part_II/local_datasets")
            coins_game_output_generator.generate_output_for_dynamic(outputs, LOCAL_PD)
            print("[PROGRAMACIÓN DINÁMICA] Casos reproducidos.")

    elif flag == "-b":

        if len(arguments) > 2:
            if arguments[2] == "-e":
                print("[BACKTRACKING] Reproduciendo casos de uso externos...")
                outputs = naval_battle_bt.run_use_cases("part_III/extern_datasets")
                bt_output_generator.generate_output_for_bt(outputs, EXTERN_BT)
                print("[BACKTRACKING] Casos reproducidos.")
        else:
            print("[BACKTRACKING] Reproduciendo casos locales...")
            outputs = naval_battle_bt.run_use_cases("part_III/local_datasets")
            bt_output_generator.generate_output_for_bt(outputs, LOCAL_BT)
            print("[BACKTRACKING] Casos reproducidos.")
    else:
        raise Exception("[ERROR] Algoritmo no reconocido!")


'''
    FLAGS DE EJECUCIÓN
    -a para todos los algoritmos con los casos de uso locales
    -g para greedy
    -d para programación dinámica
    -b para backtracking
    -e después de -g, -d o -b para los casos de uso externos
'''
if __name__ == "__main__":
    main(sys.argv)
