import random
import requests
from pprint import pprint

def random_pokemon_id():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    #print(response)
    pokemon = response.json()
    #pprint(pokemon)

    return {"name":pokemon["name"],
            "id":pokemon["id"],
            "height":pokemon["height"],
            "weight":pokemon["weight"]
            }

def players():
    player_one = random_pokemon_id()
    print("Name of player one's pokemon is:{}".format(player_one["name"]))
    print("Weight:{}, Height:{}., id:{}.\n".format(player_one["weight"], player_one["height"], player_one["id"]))
    user_stat_choice = input("What is your chosen stat?")


    more_players = random_pokemon_id()
    print("Name of player two pokemon:{}".format(more_players["name"]))
    print("Weight:{}, Height:{}., id:{}.\n".format(more_players["weight"], more_players["height"], more_players["id"]))

    player_one_stat = player_one[user_stat_choice]
    more_players_stat = more_players[user_stat_choice]

    if player_one_stat > more_players_stat:
        print("PLAYER ONE WINS")
    elif player_one_stat < more_players_stat:
        print("PLAYER TWO WINS")
    else:
        print("It's a draw, play again")
players()