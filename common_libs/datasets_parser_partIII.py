import os

def parse_dataset(dataset_absolute_path):

    with open(dataset_absolute_path, 'r') as dataset_file:
        content = dataset_file.readlines()[2:]  # Ignore the first 2 lines
        content = ''.join(content).strip().split('\n\n')
        
        rows_restrictions = [int(x) for x in content[0].split('\n')]
        columns_restrictions = [int(x) for x in content[1].split('\n')]
        ship_list = [int(x) for x in content[2].split('\n')]

    dataset_file.close()
        
    return (rows_restrictions, columns_restrictions, ship_list)

def get_datasets_list(directory_name):
    path = os.path.abspath("") + "/"
    absolute_path = path + directory_name
    datasets_list = []

    try:
        for dataset in os.listdir(absolute_path):

            if ((dataset !=  "resultados_esperados.txt") and (dataset != "resultados_esperados_tablero.txt")
                    and (dataset != "leeme.txt")):
                dataset_absolute_path = os.path.join(absolute_path, dataset)
                datasets_list.append(parse_dataset(dataset_absolute_path))

    except Exception as e:
        print(f"[ERROR] {e}")
        return None

    return datasets_list
