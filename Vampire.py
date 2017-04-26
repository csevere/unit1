class Vampire(object):
    def __init__(self):
        self.health = 100
        self.attack_power = 25
        self.name = "Vampire"
        self.xp_value = 10
        self.maxhealth = self.health

    def take_damage(self,damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0
