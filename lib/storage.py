from typing import Dict, List
from lib.dungeon_world import Character, Name, Stat

DATAFILE = "./data/characters.txt"

characters: Dict[Name, Character]

def characters_load() -> Dict[Name, Character]:
    print("loading: ", DATAFILE)

    with open(DATAFILE, "r") as file:
        lines = file.readlines()

    chars = map(lambda line: Character.decode(line), lines)
    return {char.name: char for char in chars}

def characters_save(characters: Dict[Name, Character]):
    print("saving: " + DATAFILE)

    lines = map(lambda char: char.encode(), characters.values())
    with open(DATAFILE, "w") as file:
        file.write("\n".join(lines))

def character_find(characters: Dict[Name, Character], name:Name):
    if characters.get(name):
        return characters.get(name)
    
    else:
        characters[name] = Character(name)
        return characters.get(name)
