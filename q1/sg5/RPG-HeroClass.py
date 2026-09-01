class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        

    def take_damage(self, amount): 
        self.hp = self.hp - amount
        return self.hp

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

print(arthur.take_damage(10))
print(morgana.hp)