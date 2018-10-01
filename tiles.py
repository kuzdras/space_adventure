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
class LootRoom(map_tile):
        def __init__(self, x, y, item):
                self.item = item
                super().__init__(x, y)
 
        def add_loot(self, player):
                player.inventory.append(self.item)
 
        def modify_player(self, player):
                self.add_loot(player)
#===============##===============#


#===============# super for room with enemies:
class EnemyRoom(map_tile):
        def __init__(self, x, y, enemy):
                self.enemy = enemy
                super().__init__(x, y)
 
        def modify_player(self, the_player):
                if self.enemy.is_alive():
                        the_player.hp = the_player.hp - self.enemy.damage
                        print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
#===============##===============#

#===============##now some specific rooms:
class first_corridor(LootRoom):
    def __init__(self,x,y):
        super().__init__(x, y, items.Flashlight())
        
    def intro_text(self):"""
    Corridor is devastated. Plasteel walls are full of scratches and burns. Seems like there was a fight here. Now it's empty. Wait...
    There's a flashlight on the floor. Now you'll be able to examine other rooms more closely.
    """
    
class spider_room(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, Enemy.Space_Spider())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You find yourself is devastated room. Shards of plasteel and glass are all over the floor.
            In the corner you see giant Space Spider. It jumps over you!
            """
        else:
            return """
            You find corpse of the Space Spider. You admire your work for a while and move along.
            """
		
class generic_room(map_tile):
	def __init__(self,x,y):
	super().__init__(x,y)
	
	def intro_text(self):"""
	Dirty floor and cracked walls. Lights are flashing. You hear no sound and see nothing special so you decide to proceed to next room.
	"""
        
