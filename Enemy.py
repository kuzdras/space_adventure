#The liar of whole band of bad guys

#super class
class Enemy:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
   
  def is_alive(self):
    return self.hp > 0

#time for some sub-classes
  
class SpaceSpider(Enemy):
  def __init__(self):
    super().__init__(name = "Space Spider", hp = 6, damage = 1)
