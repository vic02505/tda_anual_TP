import os

OUTPUTS_DIRECTORY = "algorithms_output"

LOCAL_GREEDY = "local_greedy_"  # Datasets locales greedy
EXTERN_GREEDY = "extern_greedy_" # Datasets externos greedy.

LOCAL_PD = "local_pd_"  # Datasets locales programación dinámica
EXTERN_PD = "extern_pd_" # Datasets externos programación dinámica

def generate_content_for_greedy(output):

    content = ""

    mateo_coins = output[1]
    mateo_gains = sum(output[1])
    sophia_coins = output[0]
    sophia_gains = sum(output[0])

    mateo_coins_str =  "[" + (",".join(map(str, mateo_coins))) + "]"
    mateo_gains_str = str(mateo_gains)
    sophia_coins_str = "[" + (",".join(map(str, sophia_coins))) + "]"
    sophia_gains_str = str(sophia_gains)

    content += "Monedas obtenidas por Mateo: " + mateo_coins_str + "\n"
    content += "Ganancia total de Mateo: " + mateo_gains_str + "\n"
    content += "Monedas obtenidas por Sophia: " + sophia_coins_str + "\n"
    content += "Ganancia total de Sophia: " + sophia_gains_str + "\n"

    return content

def generate_output_for_greedy(coins_game_outputs, output_type):

    try:
        if not os.path.exists(OUTPUTS_DIRECTORY):
            os.makedirs(OUTPUTS_DIRECTORY)

        file_id = 1
        for output in coins_game_outputs:

            file_name = output_type + str(file_id)
            file_path = os.path.join(OUTPUTS_DIRECTORY, file_name)

            with open(file_path, "w") as output_file:
                content = generate_content_for_greedy(output)
                output_file.write(content)
                output_file.close()

            file_id += 1

    except Exception as e:
        print(f"[ERROR] {e}")
        return


def generate_content_for_dynamic(output):

    content = ""

    sophia_gains = sum(output)
    sophia_gains_str = str(sophia_gains)

    content += "Ganancia total de Sophia: " + sophia_gains_str + "\n"

    return content

def generate_output_for_dynamic(coins_game_outputs, output_type):

    try:
        if not os.path.exists(OUTPUTS_DIRECTORY):
            os.makedirs(OUTPUTS_DIRECTORY)

        file_id = 1
        for output in coins_game_outputs:

            file_name = output_type + str(file_id)
            file_path = os.path.join(OUTPUTS_DIRECTORY, file_name)

            with open(file_path, "w") as output_file:
                content = generate_content_for_dynamic(output)
                output_file.write(content)
                output_file.close()

            file_id += 1

    except Exception as e:
        print(f"[ERROR] {e}")
        return
