from libs import datasets_parser

#Agregar parametro que indique si se quiere ordenar la lista o no. Esto no sirve para comparar
#resultados.
def coins_game(coins_list):
    sophia_coins = []
    mateo_coins = []
    
    sophia_is_playing = True

    beginning = 0
    end = len(coins_list) - 1
    
    while beginning <= end:

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

    
coins_list = datasets_parser.get_coins_list('6.txt')
sophia_coins, mateo_coins = coins_game(coins_list)


print(f"Sofia {sum(sophia_coins)}")
print(f"Mateo {sum(mateo_coins)}")

