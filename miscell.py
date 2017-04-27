# elif user_input == "6":
    #
    # elif user_input == "7"

    elif user_input == "8":
        sys.exit(0)
        break

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
