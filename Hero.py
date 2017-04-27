import random
import time
import sys
from Monster import Monster
from Script import script_dict

class Hero(object):
    def __init__(self, name):
        self.name = name
        self.health = 300 #they're hardecoded so don't need to mention in def init () / use in goblin game
        self.max_health = self.health
        self.action_points = 30
        self.max_actionpoints = self.action_points
        self.xp = 0
        self.level = 1
        self.potion = 4
        self.attack = 5
        self.special_a = 10
        self.special_b = 15
        self.special_c  = 25
        self.attack_ap = 1
        self.actionp_a = 3
        self.actionp_b = 6
        self.actionp_c = 9


    def print_status(self):
        print "You have %d HP, %d attack power, and %d action points." % (self.health, self.attack, self.action_points)


    def check_level(self):
        if self.xp > 30:
            self.level += 2
            self.level_up()

    def level_up(self):
        print "You have leveled up %s! Your HP is now %d, your attack power is now %d, and you have %d action points!" % (self.name, self.maxhealth, self.power, self.action_points)
        self.max_health += 20
        self.health = self.max_health
        self.attack_power += 20
        self.action_points += 20


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


    def increase_health(self, amount):
        self.health += amount
        if self.health > 280:
            self.health = self.max_health

    def increase_actionpts(self, amount):
        self.action_points += amount
        if self.action_points > 27:
            self.action_points = self.max_actionpoints




    def take_damage(self,damage):
        self.health -= self.attack_power

    def hero_attack(self, attack_monster):

        print "Watch out, %s! You are fighting a %s!\n" % (self.name, attack_monster.name)
        print self.print_status()
        # print monster.print_status()
        print "The %s has %d health points and %d attack power.\n" % (attack_monster.name, attack_monster.health, attack_monster.attack_power)
        user_input = raw_input()

                   #BASIC ATTACK
        if(user_input == "1"):
            if self.action_points <= 0:
                attack_monster.health -= 1
                print "*****You don't have enough AP! You did only 1 Damage!******"

            if self.action_points >= 1:
                attack_monster.health -= self.attack
                self.action_points -= self.attack_ap
                print "You have done %d damage!\n" % (self.attack)

            if attack_monster.health <= 0:
                print "You have defeated the %s!" % attack_monster.name
                self.xp += monster.xp_value
                self.check_level()


                #SPECIAL ATTACK 1
        elif (user_input == "2"):
            if self.action_points <= 2:
                attack_monster.health -= 1
                print "*****You don't have enough AP! You did only 1 Damage!******"


            if self.action_points >= 3:
                attack_monster.health -=  self.special_a
                self.action_points -= self.actionp_a
                print "You have done %d damage!\n" % (self.special_a)

            if attack_monster.health <= 0:
                print "YOU KILLED THE %s!" % attack_monster.name
                self.xp += attack_monster.xp_value
                self.check_level()

                time.sleep(1.5)

                #SPECIAL ATTACK 2
        elif (user_input == "3"):
            if self.action_points <= 5:
                attack_monster.health -= 1
                print "*****You don't have enough AP! You did only 1 Damage!******"

            if self.action_points >= 6:
                attack_monster.health -= self.special_b
                self.action_points -= self.actionp_b
                print "You have done %d damage!\n" % (self.special_b)


            if attack_monster.health <= 0:
                print "YOUR KILLED THE %s!" % attack_monster.name
                self.xp += attack_monster.xp_value
                self.check_level()

                time.sleep(1.5)

                #SPECIAL ATTACK 3
        elif user_input == "4":
            if self.action_points <= 0:
                attack_monster.health -= 1
                print "*****You don't have enough AP! You did only 1 Damage!******"

            if self.action_points >= 9:
                attack_monster.health -= self.special_c
                self.action_points -= self.actionp_c
                print "You have done %d damage!\n" % (self.special_c)


            if attack_monster.health <= 0:
                print "****** YOU KILLED THE %s! *******" % attack_monster.name
                self.xp += attack_monster.xp_value
                self.check_level()

                time.sleep(1.5)


        elif user_input == "5":
            print "You drank a health potion!"
            self.increase_health(20)

        elif user_input == "6":
            print "You gained 3 AP!"
            self.increase_actionpts(3)


        else:
            print "Invalid input %s" % user_input

        if attack_monster.health > 0:
            self.health -= attack_monster.attack_power  #so this will hit hero depending on what arrives in list, calling class methods
            print "The %s hits you for %d damage!\n" % (attack_monster.name, attack_monster.attack_power)


        if self.health <= 0:
                print "You died! GAME OVER!\n"
                sys.exit(0)

        if self.health > 0 and self.health < 5:
            print "You are in RAGE. Your attack power has increased by 10!!"
            self.attack_power += 5






#put store in hero here
#import traveler option
