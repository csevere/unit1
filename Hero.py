class Hero(object):
    def __init__(self, name = "Incognito"):
        self.name = name
        self.health = 300 #they're hardecoded so don't need to mention in def init () / use in goblin game
        self.attack_power = 5
        self.max_health = self.health
        self.xp = 0
        self.level = 1
        self.potion = 4


    def check_level(self):
        if self.xp > 3:
            self.level = 2
            self.level_up()

    def level_up(self):
        print "You have leveled up %s! Your HP is now %d and your power is now %d" % (self.name, self.maxhealth, self.power)
        self.max_health += 20
        self.health = self.max_health
        self.attack_power += 10


#this method return a boolean. True if the hero is alive, false if the hero is dead
    def is_alive(self):
        return self.health > 0
        # if(self.health > 0):
        #     return True
        # else:
        #     return False and
        #

    def make_name(self, user_input):
        user_input = raw_input("What is your hero's name?: ")


    def attack(self, who_to_attack):
        who_to_attack.health -= self.attack_power

    def increase_health(self, amount):
        self.health += amount
        if self.health > 280:
            self.health = self.max_health


    def take_damage(self,damage):
            self.health -= damage
