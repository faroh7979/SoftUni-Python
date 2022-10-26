from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, pokemons=list()):
        self.name = name
        self.pokemons = pokemons

    def add_pokemon(self, pokemon: Pokemon):

        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"

        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):

        for pokemon_element in self.pokemons:

            if pokemon_name == pokemon_element.name:
                self.pokemons.remove(pokemon_element)
                return f"You have released {pokemon_name}"

        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        list_for_returning = [f'Pokemon Trainer {self.name}\n', f'Pokemon count {len(self.pokemons)}\n']

        for element in self.pokemons:
            list_for_returning.append(f'- {element.name} with health {element.health}\n')

        return f'{"".join(list_for_returning)}'

