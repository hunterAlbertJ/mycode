#!/usr/bin/python3
"""Alta3 Research | hjalbert@amazon.com
 """  

# python3 -m pip install flask
from flask import Flask
from flask import redirect
from flask import url_for
import requests
# create flask app instance    
app = Flask(__name__)
api_url = "http://pokeapi.co/api/v2/pokemon/"


@app.route("/poke/<name>")
def poke_return(name):
    pokemon = requests.get(f"{api_url}?limit=1000")
    pokemon = pokemon.json()

    # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        # Display the value associated with 'name'
        #print(poke["name"])
        if poke.get("name") == name:
            pokemon = requests.get(f"{api_url}/{name}")
            pokemon = pokemon.json()
            poke_list = []
            for poke in pokemon:
                poke_list.append(poke);
            return poke_list
@app.route("/poke/<name>/abilities")
def poke_abilities(name):
    pokemon = requests.get(f"{api_url}/{name}")
    pokemon = pokemon.json()
    ability_list = []
    for ability in pokemon.get("abilities"):
        print(ability.get("ability").get("name"))
        ability_list.append(ability.get("ability").get("name"))

    return ability_list

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

