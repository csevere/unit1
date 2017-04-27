#import the monster class
from Monster import Monster
class Vampire(Monster): #making it a subclass of something else
    def __init__(self):
        super (Vampire, self).__init__("The name you want to use") # pass stuff up to parent, telling parent class about self and object
        #call init to get name
        self.health = 100 #override anything in parent class
        self.attack_power = 25
        self.name = "Vampire"
        self.xp_value = 10
        self.maxhealth = self.health

    def take_damage(self,damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0
