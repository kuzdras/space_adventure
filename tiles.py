#The whole world in one place

import Enemy, Items

class map_tile:
  def __init__(self, x, y):
    self.x = x
    self.y = y
#=====to not create blank world
  def intro_text(self):
    raise NotImplementedError()
  def modify_player(self, player):
    raise NotImplementedError()
#=====
  
#Starting tile:
#===============#
class Start(map_tile):
  def intro_text(self):"""
  You wake up in empty room. Doors to your stasis chamber slided open with a little crack. 
  When you try to move a powerful headache strikes you. You slowly move to the door. Corridor leads you only in one way. 
  All lights are off are you have a bad feeling about this.
  What do you do?
  """
  def modify_player(self, player):
    pass
  
#===============# super class for rooms with items:
class loot_room(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)
#===============##===============#


#===============# super for room with enemies:
lass EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
class one_way_corridor(map_tile):
  def __init__(x,y,self,item):
    self.item = item
    super().__init__(x,y)
#===============##===============#

#===============##now some specific rooms:
class first_corridor:
  def __init__(self,x,y):
    super().__init__(x, y, items.Flashlight())
  def intro_text(self):"""
  Corridor is devastated. Plasteel walls are full of scratches and burns. Seems like there was a fight here. Now it's empty. Wait...
  There's a flashlight on the floor. Now you'll be able to examine other rooms more closely.
  """
  def modify_player(self, player):
    pass
  

class 
    
    
