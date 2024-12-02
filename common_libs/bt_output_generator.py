
import os

LOCAL_BT = "local_bt_"  # Datasets locales backtracking
EXTERN_BT = "extern_bt_" # Datasets externos backtracking

OUTPUTS_DIRECTORY = "algorithms_output"

def generate_content_for_bt(output):

    content = ""
    game_board = output[0]
    score = output[1]

    game_board_str = "\n".join(",".join(map(str, row)) for row in game_board)

    content += game_board_str + "\n\n"

    score_str = str(score)

    content += "Restricciones cumplidas: " + score_str + "\n"

    return content

def generate_output_for_bt(bt_outputs, output_type):

    try:
        if not os.path.exists(OUTPUTS_DIRECTORY):
            os.makedirs(OUTPUTS_DIRECTORY)

        file_id = 1
        for output in bt_outputs:

            file_name = output_type + str(file_id)
            file_path = os.path.join(OUTPUTS_DIRECTORY, file_name)

            with open(file_path, "w") as output_file:
                content = generate_content_for_bt(output)
                output_file.write(content)
                output_file.close()

            file_id += 1

    except Exception as e:
        print(f"[ERROR] {e}")
        return