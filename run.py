from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

class Pokemon:
    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url

@app.route('/')
def index():
    pokemon = None
    search_query = request.args.get('search')

    if search_query:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{search_query.lower()}")
        if response.status_code == 200:
            data = response.json()
            pokemon = {
                "name": data["name"].capitalize(),
                "description": "Descrição do Pokémon",
                "image_url": data["sprites"]["front_default"],
                "type": data["types"][0]["type"]["name"].capitalize(),
                "abilities": [ability["ability"]["name"].capitalize() for ability in data["abilities"]],
                "hp": data["stats"][0]["base_stat"],
                "attack": data["stats"][1]["base_stat"],
                "defense": data["stats"][2]["base_stat"],
                "special_attack": data["stats"][3]["base_stat"],
                "special_defense": data["stats"][4]["base_stat"],
                "speed": data["stats"][5]["base_stat"]
            }

    return render_template('index.html', pokemon=pokemon, search_query=search_query)

def search():
    search_query = request.args.get('search')
    pokemon = None
    if search_query:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{search_query.lower()}')
        if response.status_code == 200:
            data = response.json()
            pokemon = Pokemon(data['name'].capitalize(), data['sprites']['front_default'])
    return pokemon
class Pokemon:
    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url
        self.description = ''
        self.types = []
        self.abilities = []
        self.stats = {}

    def get_details(self):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name.lower()}')
        if response.status_code == 200:
            data = response.json()
            self.description = self._get_description(data)
            self.types = self._get_types(data)
            self.abilities = self._get_abilities(data)
            self.stats = self._get_stats(data)

    def _get_description(self, data):
        for entry in data['species']['flavor_text_entries']:
            if entry['language']['name'] == 'en':
                return entry['flavor_text']
        return ''

    def _get_types(self, data):
        types = []
        for entry in data['types']:
            types.append(entry['type']['name'])
        return types

    def _get_abilities(self, data):
        abilities = []
        for entry in data['abilities']:
            abilities.append(entry['ability']['name'])
        return abilities

    def _get_stats(self, data):
        stats = {}
        for entry in data['stats']:
            stats[entry['stat']['name']] = entry['base_stat']
        return stats



if __name__ == '__main__':
    app.run(debug=True)

