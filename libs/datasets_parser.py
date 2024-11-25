
import os

def get_coins_list(directory_name, file_name):

    relative_path = directory_name + file_name
    path = os.path.abspath("") + "/"

    with open(path + relative_path, 'r') as dataset_file:
        
        content = dataset_file.read()
        
        coins_list = content.split(';')
        coins_list = [int(str_number) for str_number in coins_list]
    dataset_file.close()

    return coins_list
