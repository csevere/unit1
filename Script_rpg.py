class Script(object):
    def __init__(self):

        script_dict = {
        	'warrior': """
        You are a Human Warrior. Three weeks after surviving King Iskar's
        battle against the Giants. You travel back home to the village of Quor
        to visit your sister and her family, only to find everyone slaughtered
        in their sleep, even her three children. Enraged and heart-broken,
        you search for the murderer and follow a trail of human footprints to
        the base of a mountain, called the Devil's Teacup, a dark region where
        evil abounds. You enter.\n """,

        	'mage': """
        You are an Elven Mage. Your father Grik, Head Counsel to Arisia Valkruk,
        the Queen of the Northen Elven Realm, has fallen ill from dark magic.
        Rumors are swarming that the Queen's nephew, a powerful mage, is
        responsible and has fled for the Devil's Teacup, mountain known for great
        evil and even greater magic. You take a horse for the region, racing to
        find the cure for your father. And to bring your relative to justice.\n""",

        	'archer': """
        You are a Valkyrie Archer. The Great Withering is coming to the lands
        of Okarun, and without warriors to fight back the endless waves of
        monsters, you cannot hope to save the world from total destruction.
        A mysterious messenger has given you word of a powerful warrior hidden
        in a range of mountains known as The Devil's Teacup. You take your
        horse and make way for the evil region, full of even darker magic.\n"""

        }


        def welcome_WarriorScript(self):
            print script_dict['warrior']

        def welcome_MageScript(self):
            print script_dict['mage']

        def welcome_MageScript(self):
            print script_dict['archer']
