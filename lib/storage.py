from typing import Dict
from lib.dungeon_world import Character, Name, Stat, Dict

DATAFILE = "./data/characters.txt"

characters: Dict[Name, Character]

def characters_load(self) -> Dict[Name, Character]:
    print("loading: ", DATAFILE)

    file = open(DATAFILE, "r")
    lines = file.readlines()
    file.close()

    chars = map(lambda line: Character.decode(line), lines)
    return {char.name: char for char in chars}

def characters_save(self, database, characters: Dict[Name, Character]):
    print("saving: " + DATAFILE)

    lines = map(lambda char: char.encode(), characters)

    file = open(DATAFILE, "w")
    file.writelines(lines)
    file.close()

