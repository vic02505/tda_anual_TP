from part_I.libs import datasets_parser

#Agregar parametro que indique si se quiere ordenar la lista o no. Esto no sirve para comparar
#resultados.
def play_game(coins_list):
    sophia_coins = []
    mateo_coins = []
    
    sophia_is_playing = True

    beginning = 0
    end = len(coins_list) - 1
    
    while beginning <= end:

        selected_coin = -1
        
        if sophia_is_playing:
            if coins_list[beginning] <= coins_list[end]:
                selected_coin = coins_list[end]
                end -=1
            else:
                selected_coin = coins_list[beginning]
                beginning +=1
                
            sophia_coins.append(selected_coin)
            sophia_is_playing = False
        else:
            if coins_list[beginning] >= coins_list[end]:
                selected_coin = coins_list[end]
                end -=1
            else:
                selected_coin = coins_list[beginning]
                beginning +=1
                
            mateo_coins.append(selected_coin)
            sophia_is_playing = True      
    
    return sophia_coins, mateo_coins


def coins_game(coins_list_name):
    coins_list = datasets_parser.get_coins_list(coins_list_name)
    sophia_coins, mateo_coins = play_game(coins_list)
    return sophia_coins

