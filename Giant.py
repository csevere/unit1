

class Giant(object):
    def __init__(self):
        self.health = 300
        self.attack_power = 50
        self.name = "Giant"
        self.xp_value = 10
        self.maxhealth = self.health

    def take_damage(self,damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0
