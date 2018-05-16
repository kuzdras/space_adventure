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
  
class Space_Spider(Enemy):
  def __init__(self):
    super().__init__(name = "Space Spider", hp = 6, damage = 1,
                    description = "Green, dog-size spider. It has a eight red eyes and radioactive glow. It usualy lives on the planet surface")
    
    
class Hopper(Enemy):
  def __init__(self):
    super.__init__(name = "Hopper",
                  hp = 10,
                  damage = 3,
                  description = "Giant insect. It's has massive back legs and razor-sharp front ones.")
    
class Broken_Droid(Enemy):
  def __init__(self):
     super.__init__(name = "Malfunctioned Security Droid",
                  hp = 20,
                  damage = 7,
                  description = "Bulky Security Droid. It seems that it's malfunctioned because he perceives you as a threat.")
    
