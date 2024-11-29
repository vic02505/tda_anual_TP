import os

def parse_dataset(directory_name, file_name):
    relative_path = directory_name + file_name
    path = os.path.abspath("") + "/"

    with open(path + relative_path, 'r') as dataset_file:
        content = dataset_file.readlines()[2:]  # Ignore the first 2 lines
        content = ''.join(content).strip().split('\n\n')
        
        rows_restrictions = [int(x) for x in content[0].split('\n')]
        columns_restrictions = [int(x) for x in content[1].split('\n')]
        ship_list = [int(x) for x in content[2].split('\n')]
        
    return rows_restrictions, columns_restrictions, ship_list
