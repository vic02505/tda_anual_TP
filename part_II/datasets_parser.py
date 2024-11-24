import os

def get_coins_list(file_name):
    
    with open(os.path.abspath(".") + file_name, 'r') as dataset_file:
        
        content = dataset_file.read()
        
        coins_list = content.split(';')
        coins_list = [int(str_number) for str_number in coins_list]
        
    return coins_list
