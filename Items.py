#super-class for my all items
class Item():
	#Base class for all my items
	def __init__(self, name, description):
		self.name = name
		self.description = description
	def __str__(self):
	  return "{}\n=====\n{}\n".format(self.name, self.description)

#sub-class of Iteam but super-class for other weapons
class Weapon(Item):
	self.damage = damage
	super().__init__(name, description, damage)
	def __str__(self):
	  return "{}\n=====\nDamage: {}\n".format(self.name, self.description, self.damage)

#let's make some weapons:

class Pipe(Weapon):
	def __init__(self):
		super.__init__(name = "Pipe",
		               description = "Fragment of rusted water-pipe. Can be used as weapon.",
		               damage = 2)

class ShockPistol(Weapon):
	def __init__(self):
		super().__init__(name = "Shock pistol",
		               description = "Handgun for self-defence use. It shots a bolt of electricity which deals minor damage to the body."
		               damage = 8)

class StunBaton(Weapon):
	def __init__(self):
		super().__init__(name = "Stun Baton",
		               description = "A stick charged with electricity. It strikes the nerve system. Commonly used by security officers."
		               damage = 5)
# Some utility items		
class Flashlight(Item):
	def __init__(self):
		super().__init__(name = "Flashlight"
				 description = "An average flashlight, lights up your path")
