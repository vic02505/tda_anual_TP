
import os
from audioop import error

def get_coins_list(dataset_path):

    with open(dataset_path, 'r') as dataset_file:
        
        content = dataset_file.read()
        
        coins_list = content.split(';')
        coins_list = [int(str_number) for str_number in coins_list]
    dataset_file.close()

    return coins_list

def get_datasets_list(directory_name):
    path = os.path.abspath("") + "/"
    aboslute_path = path + directory_name
    datasets_list = []

    try:
        for dataset in os.listdir(aboslute_path):

            if dataset !=  "resultados_esperados.txt":
                dataset_absolute_path = os.path.join(aboslute_path, dataset)
                datasets_list.append(get_coins_list(dataset_absolute_path))
    except Exception as e:
        print(f"[ERROR] {e}")
        return None

    return datasets_list