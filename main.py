import requests

def get_pokemon_stats(pokemon_name):
    #Base url for pokemon API
    base_url = "https://pokeapi.co/api/v2/"

    #Construct the full URL for the pokemon
    pokemon_url = f"{base_url}pokemon/{pokemon_name.lower()}"

    #Send a GET request to the url
    response = requests.get(pokemon_url)

    #Check if request was succesfull
    if response.status_code == 200:
        #Parse JSON response
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data for {pokemon_name}.")
        return None

def main():
    while True:
        pokemon_name = input("Enter pokemon name: ")
        #Get data
        data = get_pokemon_stats(pokemon_name)
        type = data['types'][0]['type']['name']
        hp = data['stats'][0]['base_stat']
        attack = data['stats'][1]['base_stat']
        defense = data['stats'][2]['base_stat']
        height = data['height']
        weight = data['weight']
        picture = data['sprites']['front_default']
        picture_shiny = data['sprites']['front_shiny']
        #Print data
        print(f"Name: {pokemon_name.capitalize()}")
        print(f"Type: {type}")
        print(f"HP: {hp}")
        print(f"Attack: {attack}")
        print(f"Defense: {defense}")
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print(f"Picture: {picture}")
        print(f"Picture Shiny: {picture_shiny}")

main()
