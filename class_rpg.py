import sys
from Hero import Hero
from Monster import Monster
from Monster import Vampire
from Monster import Giant
from Monster import Ghoul
from Script import script_dict
# import pyglet
# song = pyglet.media.load('thesong.ogg')
# song.play()
# pyglet.app.run()


monsters = [] #make an empty list with variables monsters
monsters.append(Ghoul())
monsters.append(Vampire())
monsters.append(Giant())
#

print ("***** WELCOME TO WARRIOR DOGMA! *****")
print """

 __      ___   ___ ___ ___ ___  ___   ___   ___   ___ __  __   _
 \ \    / /_\ | _ \ _ \_ _/ _ \| _ \ |   \ / _ \ / __|  \/  | /_
  \ \/\/ / _ \|   /   /| | (_) |   / | |) | (_) | (_ | |\/| |/ _
   \_/\_/_/ \_\_|_\_|_\___\___/|_|_\ |___/ \___/ \___|_|  |_/_/ \_



"""


print("What is the name of your hero?: ")
hero_name = raw_input(">")
the_hero = Hero(hero_name) #call the class hero from Hero module



while the_hero.is_alive(): #run game as long as hero is alive

	def start_Warrior():
		for monster in monsters:
			while monster.is_alive():
				print script_dict["fightop_warrior"]
				print script_dict['dosomething_else']
				the_hero.hero_attack(monster)





	def start_Mage():
		for monster in monsters:
			while monster.is_alive():
				print script_dict['fightop_mage']
				print script_dict['dosomething_else']
				the_hero.hero_attack(monster)



	def start_Archer():
		for monster in monsters:
			while monster.is_alive():
				print script_dict['fightop_archer']
				print script_dict['dosomething_else']
				the_hero.hero_attack(monster)



	print("""
		Greetings, %s
		Are you the:
		1. Human Warrior?
		2. Elven Mage?
		3. Valkyrie Archer? """) % the_hero.name

	user_input = raw_input()

	if(user_input == "1"):
		print "%s,\n" % the_hero.name
		print script_dict["warrior"]
		start_Warrior()

	elif(user_input == "2"):
		print "%s,\n" % the_hero.name
		print script_dict["mage"]
		start_Mage()

	elif(user_input == "3"):
		print "%s,\n" % the_hero.name
		print script_dict["archer"]
		start_Archer()

	else:
		print "Invalid input:!"
