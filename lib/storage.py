from typing import Dict
from lib.dungeon_world import Character, Name, Stat

DATAFILE = "./data/characters.txt"

characters: Dict[Name, Character]

def characters_load() -> Dict[Name, Character]:
    print("loading: ", DATAFILE)

    file = open(DATAFILE, "r")
    lines = file.readlines()
    file.close()

    chars = map(lambda line: Character.decode(line), lines)
    return {char.name: char for char in chars}

def characters_save(database, characters: Dict[Name, Character]):
    print("saving: " + DATAFILE)

    # lines = map(lambda char: char.encode(), characters)

    # file = open(DATAFILE, "w")
    # file.writelines(lines)
    # file.close()

def character_find(characters: Dict[Name, Character], name:Name):
    if characters.get(name):
        return characters.get(name)
    
    else:
        characters[name] = Character(name, Stat(10), Stat(10), Stat(10), Stat(10), Stat(10), Stat(10))
        return characters.get(name)
