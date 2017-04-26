#Import the hero Class from Hero.py
import sys
from Hero import Hero
#Import the goblin class from Goblin.py
from Vampire import Vampire
from Ghoul import Ghoul
from Giant import Giant


#
# print ("WELCOME TO WARRIOR DOGMA")
# print("What is the name of your hero?: ")
# hero_name = raw_input(">")
# the_hero = Hero(hero_name) #call the class hero from Hero module


# print("""
# 	Greetings, %s
# 	Are you a:
#   	1. Human Warrior?
# 	2. Elven Mage?
# 	3. Valkyrie Archer?
# """) % the_hero.name
#
# if user_input == "1":
# 	print ("""You are the Human Warrior %s,
# 	Three weeks after surviving King Iskar's battle against the Giants,
# 	You travel back home to visit your sister and her family, only
# 	to find everyone slaughtered in their sleep, even her three children.
# 	Enraged and heart-broken, you search for the murderer
# 	and follow a trail of prints to the base of the mountain
# 	called the Devil's teacup""") % the_hero.name

script_dict = {
	'warrior': """
You are a Human Warrior. Three weeks after surviving King Iskar's and
battle against the Giants. You travel back home to the village of Quor
to visit your sister and her family, only to find everyone slaughtered
in their sleep, even her three children. Enraged and heart-broken,
you search for the murderer and follow a trail of human footprints to
the base of mountains, called the Devil's Teacup, a dark region where
evil abounds. You enter. """,

	'mage': """
You are an Elven Mage. Your father Grik, Head Counsel to Arisia Valkruk,
the Queen of the Northen Elven Realm, has fallen ill from dark magic.
Rumors are swarming that the Queen's nephew, a powerful mage, is
responsible and has fled for the Devil's Teacup, a range of mountains
known for great evil and even greater magic. You take a horse for the
region, racing to find the cure for your father. And to bring your
relative to justice.""",

	'archer': """
You are a Valkyrie Archer. The Great Withering is coming to the lands
of Okarun, and without warriors to fight back the endless waves of
monsters, you cannot hope to save the world from total destruction.
A mysterious messenger has given you word of a powerful warrior hidden
in a range of mountains known as The Devil's Teacup. You take your
horse and make way for the evil region, full of even darker magic."""

}


# the_hero.cheer_hero()

monsters = [] #make an empty list with variables monsters
monsters.append(Ghoul())
monsters.append(Vampire())
monsters.append(Giant())

#adding ghoul, vampire, and giants to list


# for i in range(0,len(monster)-1):
# monsters[i]

# for monster in monsters:
#

print ("***** WELCOME TO WARRIOR DOGMA! *****")
print("What is the name of your hero?: ")
hero_name = raw_input(">")
the_hero = Hero(hero_name) #call the class hero from Hero module


while the_hero.is_alive(): #run game as long as hero is alive

	def start_Warrior():
		for monster in monsters:
			print "Watch out, %s! You have encountered a %s!\n" % (the_hero.name, monster.name)
			print "You have %d health points and %d attack power.\n" % (the_hero.health, the_hero.attack_power)
			print "The %s has %d health points and %d power.\n" % (monster.name, monster.health, monster.attack_power)
			print "What do you want to do?"
			print "1. Pommel Strike!"
			print "2. Shattering Blow!"
			print "3. Mighty Blow!"
			print "4. Drink health potion"
			print "5. Use Your Magic Stop Crystal and Go to Shop" #make a class for shop
			print "6. Quit"
			print ">",
			user_input = raw_input()
			if(user_input == "1"):
				#hero is going to attack
				the_hero.attack(monster)
				# monster.take_damage(the_hero.power) #another option to attack the goblin; use one or the other
				print "POMMEL STRIKE! You have done %d damage to the %s!\n" % (the_hero.attack_power, monster.name)
				if monster.health <= 0:
					print "You have defeated the %s!" % monster.name

			elif user_input == "2":
				monster.take_damage(the_hero.attack_power) #another option to attack the goblin; use one or the other
				print "SHATTERING BLOW! You have done %d damage to the %s!\n" % (the_hero.attack_power, monster.name)
				if monster.health <= 0:
					print "You have defeated the %s!" % monster.name


			elif user_input == "3":
				monster.take_damage(the_hero.attack_power) #another option to attack the goblin; use one or the other
				print "SHATTERING BLOW! You have done %d damage to the %s!\n" % (the_hero.attack_power, monster.name)
				if monster.health <= 0:
					print "You have defeated the %s!\n" % monster.name


			elif user_input == "4":
				print "You drank a health potion!"
				the_hero.increase_health(20)

			elif user_input == "6":
				sys.exit(0)
				break

			else:
				print "Invalid input %s" % user_input

			if monster.health > 0:
				the_hero.health -= monster.attack_power  #so this will hit hero depending on what arrives in list, calling class methods
				print "The %s hits you for %d damage!\n" % (monster.name, monster.attack_power)


			if the_hero.health <= 0:
		            print "You died! GAME OVER!\n"


			if the_hero.health > 0 and the_hero.health < 5:
				print "You have gone into a rage. Your power has increased!"
		        the_hero.attack_power += 5

	def start_Mage():
		for monster in monsters:
			print "Watch out, %s! You have encountered a %s!\n" % (the_hero.name, monster.name)
					#run game as long as Both Characters ahve health

			print "You have %d health points and %d attack power.\n" % (the_hero.health, the_hero.attack_power)
			print "The %s has %d health points and %d power.\n" % (monster.name, monster.health, monster.attack_power)
			print "What do you want to do?"
			print "1. Fire Ball!"
			print "2. Winter's Blast!"
			print "3. Lightening Strike!"
			print "4. Drink health potion"
			print "5. Use Your Magic Stop Crystal and Go to Shop" #make a class for shop
			print "6. Quit"
			print "> ",
			user_input = raw_input()

			if(user_input == "1"):
				#hero is going to attack
				the_hero.attack(monster)
				# monster.take_damage(the_hero.power) #another option to attack the goblin; use one or the other
				print "FIRE BALL! You have done %d damage to the %s!\n" % (the_hero.attack_power, monster.name)
				if monster.health <= 0:
					print "You have defeated the %s!" % monster.name

			elif user_input == "2":
				monster.take_damage(the_hero.attack_power) #another option to attack the goblin; use one or the other
				print "WINTER'S BLAST! You have done %d damage to the %s!\n" % (the_hero.attack_power, monster.name)
				if monster.health <= 0:
					print "You have defeated the %s!" % monster.name


			elif user_input == "3":
				monster.take_damage(the_hero.attack_power) #another option to attack the goblin; use one or the other
				print "LIGHTENING STRIKE! You have done %d damage to the %s!\n" % (the_hero.attack_power, monster.name)
				if monster.health <= 0:
					print "You have defeated the %s!\n" % monster.name


			elif user_input == "4":
				print "You drank a health potion!"
				the_hero.increase_health(20)

			else:
				print "Invalid input %s" % user_input

			if monster.health > 0:
				the_hero.health -= monster.attack_power  #so this will hit hero depending on what arrives in list, calling class methods
				print "The %s hits you for %d damage!\n" % (monster.name, monster.attack_power)


			if the_hero.health <= 0:
		            print "You died! GAME OVER!\n"


			if the_hero.health > 0 and the_hero.health < 5:
				print "You have gone into a rage. Your power has increased!"
	        the_hero.attack_power += 5


	def start_Archer():
		for monster in monsters:
			print "Watch out, %s! You have encountered a %s!\n" % (the_hero.name, monster.name)
				#run game as long as Both Characters ahve health

			print "You have %d health points and %d attack power.\n" % (the_hero.health, the_hero.attack_power)
			print "The %s has %d health points and %d power.\n" % (monster.name, monster.health, monster.attack_power)
			print "What do you want to do?"
			print "1. Pinning Shot!"
			print "2. Rapid Shot!"
			print "3. Shattering Shot!"
			print "4. Drink health potion"
			print "5. Use Your Magic Stop Crystal and Go to Shop" #make a class for shop
			print "6. Quit"
			print "> ",
			user_input = raw_input()
			if (user_input == "1"):
				#hero is going to attack
				the_hero.attack(monster)
				# monster.take_damage(the_hero.power) #another option to attack the goblin; use one or the other
				print "PINNING SHOT! You have done %d damage to the %s!\n" % (the_hero.attack_power, monster.name)
				if monster.health <= 0:
					print "You have defeated the %s!" % monster.name

			elif user_input == "2":
				monster.take_damage(the_hero.attack_power) #another option to attack the goblin; use one or the other
				print "RAPID SHOT! You have done %d damage to the %s!\n" % (the_hero.attack_power, monster.name)
				if monster.health <= 0:
					print "You have defeated the %s!" % monster.name


			elif user_input == "3":
				monster.take_damage(the_hero.attack_power) #another option to attack the goblin; use one or the other
				print "SHATTERING SHOT! You have done %d damage to the %s!\n" % (the_hero.attack_power, monster.name)
				if monster.health <= 0:
					print "You have defeated the %s!\n" % monster.name


			elif user_input == "4":
				print "You drank a health potion!"
				the_hero.increase_health(20)

			else:
				print "Invalid input %s" % user_input

			if monster.health > 0:
				the_hero.health -= monster.attack_power  #so this will hit hero depending on what arrives in list, calling class methods
				print "The %s hits you for %d damage!\n" % (monster.name, monster.attack_power)


			if the_hero.health <= 0:
		            print "You died! GAME OVER!\n"



			if the_hero.health > 0 and the_hero.health < 5:
				print "You have gone into a rage. Your power has increased!"
		        the_hero.attack_power += 5


	print("""
		Greetings, %s
		Are you a:
		1. Human Warrior?
		2. Elven Mage?
		3. Valkyrie Archer? """) % the_hero.name
	user_input = raw_input()

	if(user_input == "1"):
		print "%s,\n" % the_hero.name, script_dict['warrior']
		start_Warrior()

	elif(user_input == "2"):
		print "%s,\n" % the_hero.name, script_dict['mage']
		start_Mage()

	elif(user_input == "3"):
		print "%s,\n" % the_hero.name, script_dict['archer']
		start_Archer()

	else:
		print "Invalid input:!"
