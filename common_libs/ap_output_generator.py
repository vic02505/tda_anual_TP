import os

LOCAL_APPROX = "local_approx_"  # Prefijo para datasets locales de aproximación
EXTERN_APPROX = "extern_approx_"  # Prefijo para datasets externos de aproximación

OUTPUTS_DIRECTORY = "algorithms_output"


def generate_content_for_approx(output):
    game_board, approx_score = output
    board_str = "\n".join(",".join(map(str, row)) for row in game_board)
    content = board_str + "\n\nPuntaje de Aproximacion: " + str(approx_score) + "\n"
    return content


def generate_output_for_approx(output, file_name, output_type):
    try:
        if not os.path.exists(OUTPUTS_DIRECTORY):
            os.makedirs(OUTPUTS_DIRECTORY)
        full_file_name = output_type + file_name
        file_path = os.path.join(OUTPUTS_DIRECTORY, full_file_name)
        with open(file_path, "w") as output_file:
            content = generate_content_for_approx(output)
            output_file.write(content)
    except Exception as e:
        print(f"[ERROR] {e}")
