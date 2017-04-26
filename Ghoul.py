class Ghoul(object):
    def __init__(self):
        self.health = 50
        self.attack_power = 10
        self.name = "Ghoul"
        self.xp_value = 5
        self.maxhealth = self.health


    def take_damage(self,damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0
