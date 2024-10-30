from libs import datasets_parser

#Agregar parametro que indique si se quiere ordenar la lista o no. Esto no sirve para comparar
#resultados.
def coins_game(coins_list):
    
    
    #coins_list.sort(reverse=True)
    
    sophia_coins = []
    mateo_coins = []
    
    sophia_is_playing = True

    beginning = 0
    end = len(coins_list) - 1
    
    while beginning < end:
        
        selected_coin = -1
        
        if sophia_is_playing:
            if coins_list[beginning] < coins_list[end]:
                selected_coin = coins_list[end]
                end -=1
            else:
                selected_coin = coins_list[beginning]
                beginning +=1
                
            sophia_coins.append(selected_coin)
            sophia_is_playing = False
        else:
            if coins_list[beginning] > coins_list[end]:
                selected_coin = coins_list[end]
                end -=1
            else:
                selected_coin = coins_list[beginning]
                beginning +=1
                
            mateo_coins.append(selected_coin)
            sophia_is_playing = True      
    
    return (sophia_coins, mateo_coins)


def coins_game_v2(coins_list):
    sophia_coins = []
    mateo_coins = []
    
    
    sophia_is_playing = True
    while len(coins_list) > 0:
        if sophia_is_playing:
            # Tomo la moneda de mayor valor. De ser iguales tomo la del principio.
            if coins_list[0] > coins_list[-1]:
                selected_coin = coins_list.pop(0)
            else:
                selected_coin = coins_list.pop()
                
            sophia_coins.append(selected_coin)
            sophia_is_playing = False
        else:
            # Tomo la moneda de menor valor. De ser iguales tomo la del principio.
            if coins_list[0] > coins_list[-1]:
                selected_coin = coins_list.pop()
            else:
                selected_coin = coins_list.pop(0)
                
            mateo_coins.append(selected_coin)
            sophia_is_playing = True
    
    return (sophia_coins, mateo_coins)

    
coins_list = datasets_parser.get_coins_list('6.txt')
sophia_coins, mateo_coins = coins_game_v2(coins_list)


print(f"Sofia {sum(sophia_coins)}")
print(f"Mateo {sum(mateo_coins)}")

