from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, pokemons=list()):
        self.name = name
        self.pokemons = pokemons

    def add_pokemon(self, pokemon_new: Pokemon):

        if pokemon_new not in self.pokemons:
            self.pokemons.append(pokemon_new)
            return f"Caught {pokemon_new.name} with health {pokemon_new.health}"

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


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
