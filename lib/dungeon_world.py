Bonus = int
Name = str

class Stat():
    value: int
    name: str
    def __init__(self, name:str, value:int):
        self.name = name
        self.value = value

    def to_bonus(self) -> Bonus:
        if self.value >= 18:
            return 3
        elif self.value >= 16:
            return 2
        elif self.value >= 13:
            return 1
        elif self.value >= 9:
            return 0
        elif self.value >= 6:
            return -1
        elif self.value >= 4:
            return -2
        elif self.value >= 1:
            return -3
        else:
            return -4

    def encode(self) -> str:
        return self.name+"="+str(self.value)

    @classmethod
    def decode(cls, input:str):
        name, rest = input.split("=")
        return Stat(name, int(rest))

class Character():

    name: str

    STR: Stat
    DEX: Stat
    CON: Stat
    WIS: Stat
    INT: Stat
    CHA: Stat

    def __init__(self, name:str):
        self.name = name
        self.STR = Stat("STR", 10)
        self.DEX = Stat("DEX", 10)
        self.CON = Stat("CON", 10)
        self.WIS = Stat("WIS", 10)
        self.INT = Stat("INT", 10)
        self.CHA = Stat("CHA", 10)

    def encode(self) -> str:
        stats = [self.STR, self.DEX, self.CON, self.WIS, self.INT, self.CHA]
        encoded = map(lambda s: s.encode(), stats)
        return self.name + ":" + "|".join(encoded)

    @classmethod
    def decode(cls, input:str):
        [name, rest] = input.split(":")
        [str, dex, con, wis, int, cha] = map(lambda s: Stat.decode(s),rest.split("|"))
        char = Character(name=name)
        char.STR = str
        char.DEX = dex
        char.CON = con
        char.WIS = wis
        char.INT = int
        char.CHA = cha
        return char