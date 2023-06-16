Bonus = int
Name = str

class Stat():
    value: int
    def __init__(self, value:int):
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
        return str(self.value)

    @classmethod
    def decode(cls, input:str):
        return Stat(int(input))

class Character():

    name: str

    STR: Stat
    DEX: Stat
    CON: Stat
    WIS: Stat
    INT: Stat
    CHA: Stat

    def __init__(self, name:str, str: Stat, dex: Stat, con: Stat, wis: Stat, int: Stat, cha: Stat):
        self.name = name
        self.STR = str
        self.DEX = dex
        self.CON = con
        self.WIS = wis
        self.INT = int
        self.CHA = cha

    def encode(self) -> str:
        stats = [self.STR, self.DEX, self.CON, self.WIS, self.INT, self.CHA]
        encoded = map(lambda s: s.encode(), stats)
        return self.name + ":" + "|".join(encoded)

    @classmethod
    def decode(cls, input:str):
        [name, rest] = input.split(":")
        [str, dex, con, wis, int, cha] = map(lambda s: Stat.decode(s),rest.split("|"))
        return Character(name=name, str=str, dex=dex, con=con, wis=wis, int=int, cha=cha)