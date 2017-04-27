from Hero import Hero
from Monster import Monster

class hero_Attack():
    def __init__ (self, hero_name):
        self.hero_name = hero_name
        self.attack = 5
        self.special_a = 10
        self.special_b = 15
        self.special_c  = 25
        self.attack_ap = 1
        self.actionp_a = 3
        self.actionp_b = 6
        self.actionp_C = 9

    def hero_attack(self):

        print "Watch out, %s! You are fighting a %s!\n" % (the_hero.name, monster.name)
        print the_hero.print_status()
        # print monster.print_status()
        print "The %s has %d health points and %d attack power.\n" % (monster.name, monster.health, monster.attack_power)

        user_input = raw_input()

        if(user_input == "1"):

            self.attack_power += self.attack
            print "%! You have done %d damage!\n" % (self.attack_power)
            monster.health -= self.attack
            self.action_pts -= self.attackap

            if monster.health <= 0:
                print "You have defeated the %s!" % monster.name
                the_hero.xp += monster.xp_value
                the_hero.check_level()


        if (user_input == "2"):
            self.attack_power += self.special_a
            print "%! You have done %d damage!\n" % (self.attack_power)
            monster.health -=  self.special_a
            self.action_pts -= self.actionp_a

            if monster.health <= 0:
                print "You have defeated the %s!" % monster.name
                the_hero.xp += monster.xp_value
                the_hero.check_level()


        elif user_input == "3":
            self.attack_power + self.special_b
            print "%! You have done %d damage!\n" % (self.attack_power)
            monster.health -= self.special_b
            self.action_pts -= self.actionp_b

            if monster.health <= 0:
                print "You have defeated the %s!" % monster.name
                the_hero.xp += monster.xp_value
                the_hero.check_level()


        elif user_input == "4":
            self.attack_power + self.special_c
            print "%! You have done %d damage!\n" % (self.attack_power)
            monster.health -= self.special_c
            self.action_pts -= self.actionp_c

            if monster.health <= 0:
                print "You have defeated the %s!" % monster.name
                the_hero.xp += monster.xp_value
                the_hero.check_level()


        elif user_input == "5":
            print "You drank a health potion!"
            the_hero.increase_health(20)


        else:
            print "Invalid input %s" % user_input

        if monster.health > 0:
            the_hero.health -= monster.attack_power  #so this will hit hero depending on what arrives in list, calling class methods
            print "The %s hits you for %d damage!\n" % (monster.name, monster.attack_power)


        if the_hero.health <= 0:
                print "You died! GAME OVER!\n"
                sys.exit(0)

        if the_hero.health > 0 and the_hero.health < 5:
            print "You are in RAGE. Your attack power has increased by 10!!"
            the_hero.attack_power += 5
