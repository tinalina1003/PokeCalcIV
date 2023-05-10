class pokemon:
    def __init__(self, name, HP, ATK, DEF, SPA, SPD, SPE):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SPA = SPA
        self.SPD = SPD
        self.SPE = SPE

pokemon.HP = input("What is your pokemon's HP IV?: ")

print(pokemon.HP)
