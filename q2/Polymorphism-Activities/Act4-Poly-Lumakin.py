class HealthPotion:
  def use(self):
    print("You regain 50 HP!")

class ManaPotion:
  def use(self):
    print("You restore 30 MP!")

class SpeedBoost:
  def use(self):
    print("Your speed increase for 10 secomds!")

def apply_item(item):
  item.use()

healthpotion = HealthPotion()
manapotion = ManaPotion()
speedboost = SpeedBoost()

potions = [healthpotion, manapotion, speedboost]
for item in potions:
  apply_item(item)
    
