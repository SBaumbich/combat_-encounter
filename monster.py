import random
from combat import Combat

COLORS = ["red","blue","green","orange","yellow"]


class Monster(Combat):
  min_hitpoints = 1
  max_hitpoints = 1
  min_exp = 1
  max_exp = 1
  weapon = "sword"
  sound = "roar"
  
  def __init__(self, **kwargs):
    self.hit_points = random.randint(self.min_hitpoints, self.max_hitpoints)
    self.exp = random.randint(self.min_exp, self.max_exp)
    self.color = random.choice(COLORS)
    
    for key, value in kwargs.items():
      setattr(self, key, value)
      
      
  def __str__(self):
    return "{} {}, HP: {}, XP: {}".format(self.color.title(),
                                           self.__class__.__name__,
                                           self.hit_points,
                                           self.exp)
      
    
    
  def battlecry(self):
    return self.sound.upper()
  
  
class Goblin(Monster):
  max_hitpoints = 3
  max_exp = 2
  sound = "squeek"
  

class Troll(Monster):
  min_hitpoints =3
  max_hitpoints = 5
  min_exp = 2
  max_exp = 6
  sound = "growl"
  
  
  
class Dragon(Monster):
  min_hitpoints = 5
  max_hitpoints = 10
  min_exp = 6
  max_exp = 10
  sound = "rahhhh"
  
  