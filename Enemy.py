#The liar of whole band of bad guys

#super class
class Enemy:
  def __init__(self, name, hp, damage, description):
    self.name = name
    self.hp = hp
    self.damage = damage
    self.description = description
    
   def desc(self):
    self.name = name
    self.description = description
    return "{}\n {}\n".format(self.name, self.description) 
   
  def is_alive(self):
    return self.hp > 0

#time for some sub-classes
  
class SpaceSpider(Enemy):
  def __init__(self):
    super().__init__(name = "Space Spider", hp = 6, damage = 1,
                    description = "Green, dog-size spider. It has a eight red eyes and radioactive glow. It usualy lives on the planet surface")
    
    
class Hopper
