from part_I import greedy_coins_game
from part_II import dynamic_coins_game
from part_III import naval_battle_bt, aproximacion
from common_libs import coins_game_output_generator, bt_output_generator, datasets_parser, datasets_parser_partIII
from common_libs import ap_output_generator

import sys

LOCAL_GREEDY = "local_greedy_"  # Datasets locales greedy
EXTERN_GREEDY = "extern_greedy_" # Datasets externos greedy.

LOCAL_PD = "local_pd_"  # Datasets locales programación dinámica
EXTERN_PD = "extern_pd_" # Datasets externos programación dinámica

LOCAL_BT = "local_bt_"  # Datasets locales backtracking
EXTERN_BT = "extern_bt_" # Datasets externos backtracking

LOCAL_APPROX = "local_approx_"  # Datasets locales de aproximación
EXTERN_APPROX = "extern_approx_"  # Datasets externos de aproximación

def main(arguments):

    if len(arguments) < 2:
        raise Exception("[ERROR] No se especificaron los flags necesarios para realizar la ejecución!")

    flag = arguments[1]

    if flag == "-a":
        print("[GREEDY] Reproduciendo casos de uso...")
        datasets_list_g, dataset_names_g = datasets_parser.get_datasets_list("part_I/local_datasets")
        if datasets_list_g is None:
            print("[ERROR] No se pudieron cargar los datasets.")

        for i in range(len(datasets_list_g)):
            dataset = datasets_list_g[i]
            file_name = dataset_names_g[i]
            output = greedy_coins_game.run_use_case(dataset)
            coins_game_output_generator.generate_output_for_greedy(output, file_name, LOCAL_GREEDY)

        print("[GREEDY] Casos reproducidos.")


        print("[PROGRAMACIÓN DINÁMICA] Reproduciendo casos de uso locales...")
        datasets_list_pd, dataset_names_pd = datasets_parser.get_datasets_list("part_II/local_datasets")
        if datasets_list_pd is None:
            print("[ERROR] No se pudieron cargar los datasets.")

        for i in range(len(datasets_list_pd)):
            dataset = datasets_list_pd[i]
            file_name = dataset_names_pd[i]

            output, coins_sophia, coins_mateo = dynamic_coins_game.run_use_case(dataset)
            coins_game_output_generator.generate_output_for_dynamic(output, coins_sophia, coins_mateo, file_name, LOCAL_PD)
        
        print("[PROGRAMACIÓN DINÁMICA] Casos reproducidos.")

        
        print("[BACKTRACKING] Reproduciendo casos de uso locales...")
        datasets_list_bt, dataset_names_bt = datasets_parser_partIII.get_datasets_list("part_III/local_datasets")
        if datasets_list_bt is None:
            print("[ERROR] No se pudieron cargar los datasets.")

        for i in range(len(datasets_list_bt)):
            dataset = datasets_list_bt[i]
            file_name = dataset_names_bt[i]

            output = naval_battle_bt.run_use_case(dataset)
            bt_output_generator.generate_output_for_bt(output, file_name, LOCAL_BT)
        print("[BACKTRACKING] Casos reproducidos.")

        print("[APROXIMACIÓN] Reproduciendo casos de uso locales...")
        datasets_list_bt, dataset_names_bt = datasets_parser_partIII.get_datasets_list("part_III/local_datasets")
        if datasets_list_bt is None:
            print("[ERROR] No se pudieron cargar los datasets.")

        for i in range(len(datasets_list_bt)):
            dataset = datasets_list_bt[i]
            file_name = dataset_names_bt[i]

            output = aproximacion.run_use_case(dataset)
            ap_output_generator.generate_output_for_approx(output, file_name, LOCAL_APPROX)
        print("[APROXIMACIÓN] Casos reproducidos.")


    elif flag == "-g":

        if len(arguments) > 2:
            if arguments[2] == "-e":
                print("[GREEDY] Reproduciendo casos de uso externos...")
                
                datasets_list_g, dataset_names_g = datasets_parser.get_datasets_list("part_I/extern_datasets")
                if datasets_list_g is None:
                    print("[ERROR] No se pudieron cargar los datasets.")

                for i in range(len(datasets_list_g)):
                    dataset = datasets_list_g[i]
                    file_name = dataset_names_g[i]
                    output = greedy_coins_game.run_use_case(dataset)
                    coins_game_output_generator.generate_output_for_greedy(output, file_name, EXTERN_GREEDY)

                print("[GREEDY] Casos reproducidos.")
                return
        else:
            print("[GREEDY] Reproduciendo casos de locales...")
            datasets_list_g, dataset_names_g = datasets_parser.get_datasets_list("part_I/local_datasets")
            if datasets_list_g is None:
                print("[ERROR] No se pudieron cargar los datasets.")

            for i in range(len(datasets_list_g)):
                dataset = datasets_list_g[i]
                file_name = dataset_names_g[i]
                output = greedy_coins_game.run_use_case(dataset)
                coins_game_output_generator.generate_output_for_greedy(output, file_name, LOCAL_GREEDY)
            print("[GREEDY] Casos reproducidos.")

    elif flag == "-d":

        if len(arguments) > 2:
            if arguments[2] == "-e":
                print("[PROGRAMACIÓN DINÁMICA] Reproduciendo casos de uso externos...")
                datasets_list_pd, dataset_names_pd = datasets_parser.get_datasets_list("part_II/extern_datasets")
                if datasets_list_pd is None:
                    print("[ERROR] No se pudieron cargar los datasets.")

                for i in range(len(datasets_list_pd)):
                    dataset = datasets_list_pd[i]
                    file_name = dataset_names_pd[i]

                    output, coins_sophia, coins_mateo = dynamic_coins_game.run_use_case(dataset)
                    coins_game_output_generator.generate_output_for_dynamic(output, coins_sophia, coins_mateo, file_name, EXTERN_PD)

                dynamic_coins_game.run_use_cases("part_I/extern_datasets")
                print("[PROGRAMACIÓN DINÁMICA] Casos reproducidos.")
                return
        else:
            print("[PROGRAMACIÓN DINÁMICA] Reproduciendo casos de uso locales...")
            datasets_list_pd, dataset_names_pd = datasets_parser.get_datasets_list("part_II/local_datasets")
            if datasets_list_pd is None:
                print("[ERROR] No se pudieron cargar los datasets.")

            for i in range(len(datasets_list_pd)):
                dataset = datasets_list_pd[i]
                file_name = dataset_names_pd[i]

                output, coins_sophia, coins_mateo = dynamic_coins_game.run_use_case(dataset)
                coins_game_output_generator.generate_output_for_dynamic(output, coins_sophia, coins_mateo, file_name, LOCAL_PD)
            print("[PROGRAMACIÓN DINÁMICA] Casos reproducidos.")

    elif flag == "-b":

        if len(arguments) > 2:
            if arguments[2] == "-e":
                print("[BACKTRACKING] Reproduciendo casos de uso externos...")
                datasets_list_bt, dataset_names_bt = datasets_parser_partIII.get_datasets_list("part_III/extern_datasets")
                if datasets_list_bt is None:
                    print("[ERROR] No se pudieron cargar los datasets.")

                for i in range(len(datasets_list_bt)):
                    dataset = datasets_list_bt[i]
                    file_name = dataset_names_bt[i]

                    output = naval_battle_bt.run_use_case(dataset)
                    bt_output_generator.generate_output_for_bt(output, file_name, EXTERN_BT)
                print("[BACKTRACKING] Casos reproducidos.")
        else:
            print("[BACKTRACKING] Reproduciendo casos locales...")
            datasets_list_bt, dataset_names_bt = datasets_parser_partIII.get_datasets_list("part_III/local_datasets")
            if datasets_list_bt is None:
                print("[ERROR] No se pudieron cargar los datasets.")

            for i in range(len(datasets_list_bt)):
                dataset = datasets_list_bt[i]
                file_name = dataset_names_bt[i]

                output = naval_battle_bt.run_use_case(dataset)
                bt_output_generator.generate_output_for_bt(output, file_name, LOCAL_BT)
            print("[BACKTRACKING] Casos reproducidos.")
    elif flag == "-ap":

        if len(arguments) > 2:
            if arguments[2] == "-e":
                print("[APROXIMACIÓN] Reproduciendo casos de uso externos...")
                datasets_list_bt, dataset_names_bt = datasets_parser_partIII.get_datasets_list(
                    "part_III/extern_datasets")
                if datasets_list_bt is None:
                    print("[ERROR] No se pudieron cargar los datasets.")

                for i in range(len(datasets_list_bt)):
                    dataset = datasets_list_bt[i]
                    file_name = dataset_names_bt[i]

                    output = aproximacion.run_use_case(dataset)
                    ap_output_generator.generate_output_for_approx(output, file_name, LOCAL_APPROX)
                print("[APROXIMACIÓN] Casos reproducidos.")
        else:
            print("[APROXIMACIÓN] Reproduciendo casos de uso locales...")
            datasets_list_bt, dataset_names_bt = datasets_parser_partIII.get_datasets_list("part_III/local_datasets")
            if datasets_list_bt is None:
                print("[ERROR] No se pudieron cargar los datasets.")

            for i in range(len(datasets_list_bt)):
                dataset = datasets_list_bt[i]
                file_name = dataset_names_bt[i]

                output = aproximacion.run_use_case(dataset)
                ap_output_generator.generate_output_for_approx(output, file_name, LOCAL_APPROX)
            print("[APROXIMACIÓN] Casos reproducidos.")
    else:
        raise Exception("[ERROR] Algoritmo no reconocido!")


'''
    FLAGS DE EJECUCIÓN
    -a para todos los algoritmos con los casos de uso locales
    -g para greedy
    -d para programación dinámica
    -b para backtracking
    -ap para aproximación
    -e después de -g, -d, -b o -ap para los casos de uso externos
'''
if __name__ == "__main__":
    main(sys.argv)
