#the super class

class Monster(object):
    def __init__(self, name):
        self.name = name
        self.health = 300
        self.attack_power = 50 #you can hard code this for EVERY monter if you choose
        self.xp_value = 10
        self.maxhealth = self.health

    def take_damage(self,damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def monster_status(self):
        "The %s has %d health points and %d power.\n" % (monster.name, monster.health, monster.attack_power)



class Ghoul(Monster):
    def __init__(self):
        super(Ghoul, self).__init__("Ghoul") #need to call super to pass variables, call the init function
        self.name = "GHOUL"
        self.health = 50 # will override parent attributes
        self.attack_power = 10
        self.xp_value = 5
        self.maxhealth = self.health


class Vampire(Monster): #making it a subclass of something else
    def __init__(self):
        super (Vampire, self).__init__("VAMPIRE") # pass stuff up to parent, telling parent class about self and object
        #call init to get name
        self.health = 100 #override anything in parent class
        self.attack_power = 25
        self.name = "VAMPIRE"
        self.xp_value = 10
        self.maxhealth = self.health



class Giant(Monster):
    def __init__(self):
        super (Giant, self).__init__("Giant")
        self.health = 300
        self.attack_power = 50
        self.name = "GIANT"
        self.xp_value = 10
        self.maxhealth = self.health





# class Hobghoul(Ghoul):
#     def __init__ (self):
#         super(hobghoul, self).__init__()
#         self.power = 3
        #   self.name = "Hobghuol"


    # def take_damage(self,damage):
    #     self.health -= damage
    #
    # def is_alive(self):
    #     return self.health > 0
