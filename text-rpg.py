#This is a procedural approach to a text based rpg game
#The hero is fighting a goblin
#He has the option to: fight, do nothing, run

#procedural way to make a game



def main():
	hero_health = 10
	hero_power = 5
	goblin_health = 6
	goblin_power = 2

	# Run game as long as BOTH cahracters have health
	while goblin_health > 0 and hero_health > 0:
 		print "You have %d health and %d power." % (hero_health, hero_power)
 		print "The goblin has %d health and %d power." % (goblin_health, goblin_power)
 		print "What do you want to do?"
 		print "1. fight goblin"
 		print "2. do nothing"
 		print "3. flee"
 		print "> ",
 		user_input = raw_input()

        if user_input == "1":
            #hero is going to attack
            goblin_health -= hero_power
            print "You have done %d damage to the goblin" % hero_power
            print "You have defeated the goblin!"

        elif user_input == "2":
            #hero is going to do nothing
            pass # tell program not to do anything, allows you to keep going

        elif user_input == "3":
			print "Goodbye, coward."
            break

        else:
            print "Invalid input %s" % user_input

        if goblin_health > 0:
            hero_health =- goblin_power
            print "The %s hits you for %d damage" % monster
            if hero_health <= 0:
                print "You die!"

        if hero_health > 0 and hero_health < 5:
            print "You have gone into a rage. Your power has incraesed!"
            hero_power += 5



main()
