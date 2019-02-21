#-------------------------------------------------------------------------------
# Name:        The Adventures of Doctor Who
# Purpose:     Class project (Mr. Zimny)
#
# Author:      Ketan Vasudeva and Emma Williams
#
# Created:     12/01/2016
# Submitted:   26/01/2016
#-------------------------------------------------------------------------------
import time
from pygame import mixer

#This code generates the start screen and resets the game the game.
def startScreen (inventory, situations):
    mixer.init()
    mixer.music.load('F:\Python\Summative\Doctor Who Theme Tune 2005-2007 By Murray Gold.mp3')
    mixer.music.play(2, 0)
    print ("THE ADVENTURES OF DOCTOR WHO")
    print ("")
    time.sleep(5)
    print ("")
    print ("You are Doctor Who")
    time.sleep(3)
    print ("")
    print ("He is a 2000 year old time traveller from another planet with a particular fondness")
    print ("for humans. He uses his spaceship known as the Tardis (disguised as a")
    print ("blue police box) in order to travel through time and space. Use your")
    print ("own intelligence to guide the Doctor through his daily adventures.")
    time.sleep (10)
    print ("")
    gameProgress = 0
    return gameProgress

#This function generates the end of game screen and asks the user if they wish to play again.
def death (inventory, situations, gameProgress) :
    import time
    time.sleep(2)
    mixer.init()
    mixer.music.load('F:\Python\Summative\Game Over sound effect.mp3')
    mixer.music.play(10, 0)
    time.sleep (2)
    print ("")
    print ("You are dead. Two thousand years alive and you manage to kill the Doctor in less than one day")
    print ("")
    print ("You have discovered " + str(gameProgress) + "% of the game.")
    print ("")
    time.sleep(2)
    mixer.music.stop()

    playAgain = raw_input ("Do you wish to play again? (yes/no)")
    if playAgain == "yes":
        gameProgress = startScreen (inventory, situations)
        return gameProgress
    else :
        print ("Thank you for playing, have a good day and maybe get a little smarter.")
        quit()

#This function runs the part of the game that take place on Doctor Who's home planet.
def homeGallifrey (inventory, situations, gameProgress):
    import time
    mixer.init()
    mixer.music.load('F:\Python\Summative\Doctor Who- The 50th Anniversary - Regeneration Soundtrack.mp3')
    mixer.music.play(3, 0)
    print ("")
    print ("This is your home planet, a war has been raging for centuries between")
    time.sleep (2)
    print ("the warrior race Daleks and your time lords.")
    time.sleep (2)
    print ("The Daleks are an emotionless 'superior race' bent on universal domination.")
    time.sleep (2)
    print ("They were created by a scientist called Davros during the final years")
    time.sleep (2)
    print ("of a thousand-year war. Davros genetically")
    time.sleep (2)
    print ("modified his people and integrated them with a tank-like,")
    time.sleep (2)
    print ("robotic shell, removing their every emotion apart from hate.")
    time.sleep (2)
    print ("Later in history, the Daleks acquired time travel technology")
    time.sleep (2)
    print ("and engaged the Time Lords in a brutal Time War affecting most of the universe,")
    time.sleep (2)
    print ("with battles taking place across all of history.")
    time.sleep (2)
    print ("It is up to you to end the war one way or another...")
    time.sleep (2)
    print ("")
    print ("(options)")
    print ("")

    optionsHome = ["The high council", "Daleks headquarters", "Time Lord's armory"]
    print (optionsHome)
    print ("")
    placeHome = raw_input ("Where to?")
    #This loops through all the different options for this part of the game and ensures that user inputs a correct destination.
    while len(optionsHome) != 0 :
        if placeHome == "The high council":
            optionsHome.remove ("The high council")
            print("")
            print("You arrive in the council chamber. Rassilon, the Lord President of all the Time")
            time.sleep (2)
            print("Lords, awaits you. He has tried to have you killed in the past so you must be")
            time.sleep (2)
            print("cautious. He believes you to be a madman. What do you say?")
            time.sleep (2)
            print("")

            print("(Options)// This war has gone on long enough! or Screw you! or (Other)")
            answerCouncil = raw_input ()
            if answerCouncil == "This war has gone on long enough!":
                time.sleep (2)
                print ("")
                print ("Rassilon : I agree.")
                print ("")
                time.sleep (2)
                print ("You : This war will continue to consume all of time and space unless we act")
                time.sleep (2)
                print ("      immediately and drastically. The need of the many, in this case, the entire")
                time.sleep (2)
                print ("      universe, outweighs the need of the few. This war needs to end one way")
                time.sleep (2)
                print ("      or another.")
                time.sleep (2)
                print("")
                print ("Rassilon : I do not trust you, you are insane. What exactly do you plan?")
                print("")
                time.sleep (2)
                print ("You : " + raw_input ())
                print("")
                time.sleep (2)
                print ("Rassilon : Don't be stupid! Guards! Seize him!")
                decisionCouncil = ""

                while decisionCouncil != "run" and decisionCouncil != "stay":
                    decisionCouncil = raw_input ("What do you do? (run or stay?)")
                if decisionCouncil == "run":
                    print ("You sprint out of the room towards the secret tunnels under the planet's surface.")
                    print ("A door blocks your way. What do you use?")
                    print ("")

                    print ("(options)")
                    print (inventory)
                    inventoryCouncil = raw_input ()
                    if inventoryCouncil == "Sonic screwdriver":
                        print ("")
                        print ("Great choice! The Sonic screwdriver can open almost any door and has many different functions (such as a computer).")
                        print ("You open the door and escape the council's grasp.")
                    else:
                        print ("This does not work. The guards catch up to you with orders to shoot on sight.")
                        mixer.music.fadeout(1000)
                        gameProgress = death (inventory, situations, gameProgress)
                        return gameProgress
                elif decisionCouncil == "stay":
                    print ("")
                    print ("The guards come and take your head.")
                    mixer.music.fadeout(1000)
                    gameProgress = death (inventory, situations, gameProgress)
                    return gameProgress
                else :
                    decisionCouncil = raw_input ("What do you do? (run or stay?)")
            if len(optionsHome) != 0:
                print ("")
                print (optionsHome)
                placeHome = raw_input ("Where do you want to go next?")
        elif placeHome == "Daleks headquarters":
            optionsHome.remove ("Daleks headquarters")
            actionsDalek = ["duck and cover", "run away", "go into the Tardis", "alert civilians"]
            print ("You are on your way to the Dalek's headquarters...")
            print ("")
            time.sleep (3)
            print ("As you look up you see multiple dalek ships flying above you")
            time.sleep(3)
            print (" ")
            print ("dropping bombs and firing at the time lord military force.")
            time.sleep (3)
            print ("")
            print ("You watch as your home is being destroyed.")
            time.sleep(3)
            print (" ")
            print ("SUDDENLY A DALEK SHIP COMES SPIRALING OUT OF CONTROL TOWARDS YOU!!!")
            time.sleep(3)
            print ("")

            print ("(options)")
            print (actionsDalek)
            print("")
            dalekShip = raw_input ("What do you do?")
            while len(actionsDalek) != 0 :
                if dalekShip == "alert civilians":
                    actionsDalek.remove ("alert civilians")
                    print ("")
                    yell = raw_input ("You decide alerting everyone near you is the best option (type what you want to say)")
                    print yell
                    time.sleep (3)
                    print ("")
                    print ("However, that has only created more panic in the streets!")
                    time.sleep(2)
                    print ("")
                    time.sleep (2)

                    print ("(options)")
                    print (actionsDalek)
                    print("")
                    dalekShip = raw_input ("You should try something else.")
                elif dalekShip == "run away":
                    actionsDalek.remove ("run away")
                    print ("")
                    print ("You decide running away is the best option.")
                    time.sleep (2)
                    print ("")
                    print ("Realizing you would wouldn't get very far, you decide to try something else")
                    print ("")

                    print ("(options)")
                    print (actionsDalek)
                    print("")
                    dalekShip = raw_input ("You coward! Once again a dalek ship is about to crash! What do you do? (maybe you should try doing something more practical)")
                elif dalekShip == "duck and cover":
                    actionsDalek.remove ("duck and cover")
                    print ("")
                    time.sleep (2)
                    print ("That's a terrible idea. You should try something else.")
                    print ("")

                    print ("(options)")
                    print (actionsDalek)
                    print("")
                    dalekShip = raw_input ("What do you do?")
                elif dalekShip == "go into the Tardis":
                    print ("")
                    time.sleep (2)
                    print ("The Daleks use an extendable arm resembling a sink plunger to interact with technology.")
                    print ("")
                    time.sleep (2)
                    print ("Once you've entered the Tardis you use your sonic screwdriver to control the Daleks")
                    print ("")
                    time.sleep (2)
                    print ("plunger to control the ship and drive the ship out of your planet and into space. ")
                    print ("")
                    actionsDalek = []

                    print (optionsHome)
                    placeHome = raw_input ("Where to next?")
                else:
                    print ("")
                    print ("That's not an option right now.")
        elif placeHome == "Time Lord's armory":
            optionsHome = []
            actionsArmory = ["weapon of mass destruction", "trap the planet in a single moment in time"]
            print ("")
            time.sleep (3)
            print ("You arrive at the time lord armory.")
            time.sleep (3)
            print ("faced with the two decisions...The weapon called 'the Moment' will wipe out both Time Lords and daleks")
            time.sleep (3)
            print ("or you could attempt to trap the planet in a moment in time which might fail. The war must end.")

            print (actionsArmory)
            armory = raw_input ("what do you do?")
            while armory != "weapon of mass destruction" and armory != "trap the planet in a single moment in time" :
                print ("")
                print ("Sorry that answer is invalid. Please try something else.")
                print (actionsArmory)
                armory = raw_input ("what do you do?")
            if armory == "weapon of mass destruction" :
                print ("")
                print ("The doctors intentions is for the moment to destroy both the Time Lords and the Daleks.")
                time.sleep (3)
                print ("The moment comes with a concequence...")
                time.sleep (3)
                print ("You will die with the rest of your race, ending the Time war and all Daleks from the universe.")
                mixer.music.fadeout(1000)
                gameProgress = death (inventory, situations, gameProgress)
                return gameProgress
            elif armory == "trap the planet in a single moment in time" :
                print ("")
                print ("The plan is to use stasis technology to trap Gallifrey in a single moment in time.")
                time.sleep (3)
                print ("When Gallifrey disappears, the surrounding Dalek war ships would obliterate themselves")
                time.sleep(3)
                print ("In the crossfire")
                time.sleep(3)
                print ("Congratulations!!! You've managed to save your people and end the Time War.")
                mixer.music.fadeout(1000)
                gameProgress = gameProgress + 25
                return gameProgress
        else:
            placeHome = raw_input ("I'm sorry, that is not on this planet. Where to?")

#This function runs the code pertinent to the part of the game that is in Berlin, Germany.
def berlinGermany (inventory, situations, gameProgress):
    mixer.init()
    mixer.music.load('F:\Python\Summative\Doctor Who Unreleased Music - Lets Kill Hitler - Previously on Doctor Who.mp3')
    mixer.music.play (4,0)
    import time
    time.sleep (2)
    print ("")
    print ("You enter the Tardis deciding that it's time to visit Berlin, Germany. Ahhhh, Berlin, the heart")
    time.sleep (2)
    print ("of modern day Europe. No better place to take a relaxing break but amidst the innovation of the")
    time.sleep (2)
    print ("german folk. Such a progressive people.")
    time.sleep (2)
    print ("You arrive in an expensively orned room with a massive desk at the other side. Giant bookcases")
    time.sleep (2)
    print ("overflow with shelves upon shelves of books. A fancy furncace broods darkly in the corner.")
    print ("")
    time.sleep (2)
    optionsBerlin = ["Look around", "Go into hallway", "Go over to the desk"]
    print ("")

    print ("(options)")
    print (optionsBerlin)
    placeBerlin = raw_input("What do you want to do?")
    #This code checks if the user has inputed a valid option and loops through this section of the game.
    while len(optionsBerlin) != 0:
        if placeBerlin == "Look around":
            optionsBerlin.remove ("Look around")
            print ("")
            print ("You decide to take a look around the room.")
            time.sleep (2)
            print ("You go over to the furnace and notice a pile of burnt books inside.")
            time.sleep (2)
            print ("You find a lighter next to the furncace. *object aquired: lighter*")
            inventory.append("lighter")
            time.sleep (2)
            print ("You continue to look around the room. The books on the shelves appear to")
            time.sleep (2)
            print ("written in German. Looking towards the wall behind the massive desk, you notice")
            time.sleep (2)
            print ("a giant swastika flag...")
            print ("")

            print (optionsBerlin)
            placeBerlin = raw_input ("What do you want to do next?")
        elif placeBerlin == "Go over to the desk":
            optionsBerlin.remove ("Go over to the desk")
            print ("")
            print ("You walk over to the massive desk. It seems to be strewn with loose papers and maps.")
            time.sleep (2)
            print ("You notice a book on the side of the desk, it's name is 'Mein Kampf'. Other papers")
            time.sleep (2)
            print ("seem to indicate troop locations all over Europe. Strange, didn't think there was a")
            time.sleep (2)
            print ("war in Europe nowadays.")

            print (optionsBerlin)
            placeBerlin = raw_input ("What do you want to do next?")
        elif placeBerlin == "Go into hallway":
            optionsBerlin = []
            print ("You walk over to the giant oak door and push it open into the hallway.")
            time.sleep (2)
            print ("The walls are littered with swastikas. You begin to think that this is")
            time.sleep (2)
            print ("not the Germany you were looking for. As you keep walking, a guard rounds")
            time.sleep (2)
            print ("the corner.")
            time.sleep (2)
            print ("")

            print ("(options)")
            inventory.append ("run")
            print (inventory)
            decisionGuard = raw_input ("What do you do?")
            guardCount = 0
            #This code checks to see if the user has selected the correct option.
            while guardCount != 1:
                if decisionGuard == "run":
                    time.sleep (2)
                    print ("You turn and run")
                    time.sleep (2)
                    print ("The guard shoots you in the back.")
                    inventory.remove ("run")
                    mixer.music.fadeout(1000)
                    gameProgress = death (inventory, situations, gameProgress)
                    return gameProgress
                elif decisionGuard == "Sonic screwdriver":
                    time.sleep (2)
                    print ("What are you going to do with a screwdriver? Build yourself a cabinet to hide in?")
                    print ("Be more reasonable.")
                    time.sleep (2)
                    print ("The guard is facing you.")
                    time.sleep (2)
                    print ("")
                    print (inventory)
                    decisionGuard =("What do you want to do?")
                elif decisionGuard == "lighter":
                    inventory.remove ("lighter")
                    print ("")
                    print ("Um... That's arson. You sure you're not secretly a psychopath?")
                    time.sleep (2)
                    print ("")
                    print (optionsGuard)
                    inventory.append ("lighter")
                    decisionGuard =("What do you want to do?")
                elif decisionGuard == "psychic paper":
                    guardCount = 1
                    inventory.remove("run")
                    time.sleep (2)
                    print ("Great choice, the psychic paper shows people what they want to see. It can often")
                    time.sleep (2)
                    print ("be used to fake an identity.")
                    time.sleep (2)
                    ministry = raw_input("You : Hey there, I'm from the ministry of ???")
                    time.sleep (2)
                    print ("")
                    print ("The guard does not appear to understand english, however he no longer seems hostile.")
                    time.sleep (2)
                    print ("Whatver the psychic paper showed him, it worked. The guards asks you to come with him")
                    time.sleep (2)
                    print ("in rough english.")
                    time.sleep (2)
                    print ("")
                    print ("The guard leads you to the basement of what seems to be a military compound. You notice")
                    time.sleep (2)
                    print ("some cans of gasoline leaking in the corner of the room. Explosives lie on the ground like toys.")
                    time.sleep (2)
                    print ("The guard calls to what seems to be his commanding officer standing at a table. The officer turns and")
                    time.sleep (2)
                    print ("you come face to face with Adolf Hitler.")
                    print ("")
                    mixer.music.fadeout(1000)
                    mixer.init()
                    mixer.music.load('F:\Python\Summative\DUN-DUN-DUUUUN!!! Sound Effect.mp3')
                    mixer.music.play (2,0)
                    time.sleep (4)
                    mixer.music.stop()
                    mixer.init()
                    mixer.music.load('F:\Python\Summative\Doctor Who Unreleased Music - Lets Kill Hitler - Previously on Doctor Who.mp3')
                    mixer.music.play (2,0)
                    time.sleep (2)
                    print ("** I think that it's time to mention something...")
                    time.sleep (2)
                    print ("You have a british accent... And it seems you're stuck in World War Two Germany...")
                    time.sleep (2)
                    print ("Oops...**")
                    print ("")
                    time.sleep (5)
                    print ("The guard seems to tell Hitler something about finding you in his office.")
                    time.sleep (2)
                    print ("Hitler asks you for your name.")
                    time.sleep (2)
                    name = raw_input ("What do you say?")
                    time.sleep (2)
                    print ("You say your name is " + name)
                    time.sleep (2)
                    print ("Hitler picks up on your british accent and starts yelling obsceneties. His quivering")
                    time.sleep (2)
                    print ("moustache seems about to fall of his face. Hitler has been known to give terrible deaths")
                    time.sleep (2)
                    print ("to english spies. You must think fast.")
                    print ("")

                    print ("(options)")
                    print (inventory)
                    choiceHitler = raw_input("What do you do?")
                    while choiceHitler !="Sonic screwdriver" and choiceHitler != "psychic paper" and choiceHitler != "lighter":
                        choiceHitler = raw_input ("Seriously, what do you do?")
                    if choiceHitler =="Sonic screwdriver":
                        print ("")
                        print ("You throw the Sonic screwdriver at Hitler's head.")
                        time.sleep (2)
                        print ("He picks up his gun and throws a bullet at yours...")
                        time.sleep (2)
                        mixer.music.fadeout(1000)
                        gameProgress = death (inventory, situations, gameProgress)
                        return gameProgress
                    elif choiceHitler == "psychic paper":
                        print ("")
                        print ("The psychic paper shows people what they want to see.")
                        time.sleep (2)
                        print ("You show Hitler the psychic paper and he lets out a startled grunt.")
                        time.sleep (2)
                        print ("You look at the paper and see that it showed him a star of David.")
                        time.sleep (2)
                        print ("So now Hitler not only thinks you are British, but a British jew.")
                        time.sleep (2)
                        print ("Doctor Who part two coming soon... Escaping Auschwitz.")
                        mixer.music.fadeout(1000)
                        gameProgress = death (inventory, situations, gameProgress)
                        return gameProgress
                    elif choiceHitler =="lighter":
                        print ("")
                        print ("You throw the lighter on the ground right where the gas has leaked.")
                        time.sleep (2)
                        print ("The whole building goes up in smoke as you run for your life back to the")
                        time.sleep (2)
                        print ("the Tardis. You get in and fly far far away.")
                        mixer.music.fadeout(1000)
                        inventory.remove ("lighter")
                        gameProgress = gameProgress + 25
                        return gameProgress
                else :
                    decisionGuard = raw_input("Come on, this is a serious situation, what do you do?")
            else :
                print ("")
                print (optionsBerlin)
                placeBerlin = raw_input ("That's not an option right now, what do you do?")

#This function run the code for entering the house that is mentioned to be across the street.
def darkHouse (inventory, situations, gameProgress):
    mixer.init()
    mixer.music.load('F:\Python\Summative\Doctor Who Soundtrack - Blink.mp3')
    mixer.music.play (3,0)
    actionsDarkHouse = ["Look around","Continue walking past the courtyard"]
    import time
    print ("")
    print ("You decide to pay a visit to the dark house across the street that has been raising the hairs on")
    time.sleep (3)
    print ("the back of your neck.")
    print ("")
    time.sleep (3)
    print ("You go up to the front door and find it locked, what do you use?")
    print ("")

    time.sleep (3)
    print ("(options)")
    print (inventory)
    options = raw_input ("You use the")
    while len(actionsDarkHouse) != 0:
        if options == "psychic paper":
            time.sleep (2)
            print ("")
            print ("Great idea, try to hypnotize the door, now go and get a degree in common sense.")
            time.sleep (2)
            options = raw_input ("Now what do you really use?")
        elif options == "Sonic screwdriver":
            mixer.music.fadeout(1000)
            mixer.init()
            mixer.music.load('F:\Python\Summative\Horror Sound Effect - Creaking Door Open - Copy.mp3')
            mixer.music.play (2,0)
            time.sleep(5)
            mixer.music.fadeout(1000)
            mixer.init()
            mixer.music.load('F:\Python\Summative\Doctor Who Soundtrack - Blink.mp3')
            mixer.music.play (10,0)
            time.sleep (2)
            print ("The Sonic screwdriver can open almost any door. This one is no different.")
            time.sleep (3)
            print ("Once inside your spidey senses tell you that you are not alone, and whatevers in ")
            time.sleep (3)
            print ("here is not human. You walk towards the creaking, into the darkness.")
            time.sleep (3)
            print ("With every step, a creaking sound follows")
            time.sleep (3)
            print ("closer and closer, until you find yourself in a small outdoor court yard.")
            time.sleep (2)
            print ("Overgrown vines and weeds crowd most of the space.")
            time.sleep (3)
            print ("")

            print (actionsDarkHouse)
            options = raw_input("What do you want to do?")
        elif options == "Look around" :
            time.sleep(2)
            print ("")
            print ("You decide to take a look around the courtyard.")
            time.sleep(3)
            print ("In the middle of the courtyard you see a circular shaped waterfall.")
            time.sleep(3)
            print ("Multiplpe plants crowd the waterfall covering most of it's surface.")
            time.sleep(3)
            print ("At the base of the structure you see baby angles statues.")
            time.sleep (3)
            print ("In that moment you knew what species had invaded this house.")
            time.sleep(3)
            print ("")
            actionsDarkHouse.remove ("Look around")

            print (actionsDarkHouse)
            print ("")
            options = raw_input ("Where to next?")
        elif options == "Continue walking past the courtyard" :
            actionsDarkHouse =[]
            time.sleep (2)
            print ("")
            print ("As you continue walking past the house, you find a stone pathway.")
            time.sleep (3)
            print ("The path seems to be leading to a large open field.")
            time.sleep(3)
            actionsDarkHouse.append ("Follow the pathway")
            actionsDarkHouse.append ("Go back to the house")
            print ("")

            print (actionsDarkHouse)
            options = raw_input ("Go on! Live a little. What's the worst that could happen?")
        elif options == "Follow the pathway" :
            actionsDarkHouse =[]
            print ("")
            time.sleep (2)
            print ("Continuing along the path you reach a huge open field.")
            time.sleep(3)
            print ("Out in the distance you see a car...As you approach the car.")
            time.sleep(3)
            print ("You notice the keys are still in the ignition.")
            actionsDarkHouse.append ("Turn the keys in the ignition")
            actionsDarkHouse.append ("Look inside the car")
            print ("")

            print (actionsDarkHouse)
            options = raw_input ("Hmm...You decide to.")
        elif options == "Turn the keys in the ignition" :
            time.sleep (2)
            print ("")
            print ("Hmm...The car still works, but where are the owners?")
            time.sleep (3)
            print ("They couldn't have gotten very far.")
            time.sleep (2)
            print ("In the distance you see another abandoned car.")
            actionsDarkHouse =[]
            actionsDarkHouse.append ("Walk towards the car")
            actionsDarkHouse.append ("Go back to the house")
            print ("")

            print (actionsDarkHouse)
            options = raw_input ("")
        elif options == "Walk towards the car" :
            time.sleep(2)
            print ("")
            print ("Same case for this car, the keys are still in the ignition and the owners are nowhere is sight.")
            time.sleep (3)
            print ("The sun is starting to set")
            time.sleep (2)
            print ("and I don't want to be out here with whatever took those people.")
            time.sleep (3)
            actionsDarkHouse =[]
            actionsDarkHouse.append ("Go back to the house")
            actionsDarkHouse.append ("Spend the night in the car")
            print ("")

            print (actionsDarkHouse)
            options = raw_input ("It's getting cold outside maybe we should go inside")
        elif options == "Look inside the car" :
            time.sleep(2)
            print ("")
            print ("Hmm..that's strange")
            time.sleep (2)
            print ("In the back seat of the car you find two backpacks, sleeping bags, pillows, and food and water.")
            time.sleep(3)
            print ("The food and water haven't been opended yet.")
            time.sleep (3)
            print ("You poor the water onto your hand..the waters still cold.")
            actionsDarkHouse =[]
            actionsDarkHouse.append ("Go back to the house")
            actionsDarkHouse.append ("Turn the keys in the ignition")
            print ("")

            print (actionsDarkHouse)
            options = raw_input ("Where to next?")
        elif options == "Spend the night in the car" :
            time.sleep (2)
            print ("")
            mixer.music.fadeout(1000)
            gameProgress = death (inventory, situations, gameProgress)
            return gameProgress
        elif options == "Go back to the house" :
            time.sleep(2)
            print ("")
            print ("You have returned to the courtyard")
            actionsDarkHouse =[]
            actionsDarkHouse.append ("Look around")
            actionsDarkHouse.append ("Go inside")
            print ("")

            print (actionsDarkHouse)
            options = raw_input ("What do you want to do?")
        elif options == ("Go inside") :
            time.sleep (2)
            print ("")
            print ("Once inside the house you deicde to take a look around")
            time.sleep (2)
            print ("You walk into a room with a human sized stone statues.")
            time.sleep (2)
            print ("In the form of winged angels in drapped clothing")
            time.sleep (2)
            print ("Her hands appear to be covering her face")
            time.sleep (2)
            print ("The Weeping Angels can send a person into the past to a point before his/her own birth.")
            time.sleep (3)
            print ("They feed off the potential energy of the years which that victim would have lived in the present.")
            time.sleep (3)
            print ("However, when they are being observed they become quantum-locked.")
            time.sleep (3)
            print ("occupying a single position and becoming stone.")
            actionsDarkHouse =[]
            actionsDarkHouse.append ("Run away")
            actionsDarkHouse.append ("Keep looking at the angel")
            print ("")

            print (actionsDarkHouse)
            options = raw_input ("Chose wisely")
        elif options == "Run away" :
            time.sleep (2)
            print ("")
            print ("You're stupid, I just told you they can't move if you look at them")
            mixer.music.fadeout(1000)
            gameProgress = death (inventory, situations, gameProgress)
            return gameProgress
        elif options == "Keep looking at the angel" :
            time.sleep (2)
            print ("Okay good, now the angel can't move.")
            time.sleep (2)
            print ("Keep looking at it. don't take your eyes off it. Don't even blink not for a second.")
            time.sleep(3)
            print ("Behind the angel you see a shovel")
            actionsDarkHouse =[]
            actionsDarkHouse.append ("Use the shovel to hit the angel")
            actionsDarkHouse.append ("Kick the angel")
            print ("")

            print (actionsDarkHouse)
            options = raw_input ("To shovel or not to shovel?")
        elif options == "Use the shovel to hit the angel" :
            time.sleep (2)
            print ("")
            print ("You grab the shovel and throw it at the angel")
            time.sleep(2)
            print ("Little did you know the angels are quantum locked")
            time.sleep (2)
            print ("meaning they are practically indestructible.")
            time.sleep (3)
            print ("This situation seems impossible. You decide to leave the house and never return")
            time.sleep(3)
            print ("Walking backwards out of the house and down the front steps.")
            actionsDarkHouse =[]
            note = raw_input ("You leave a note on the door saying..")
            print (note)
            mixer.music.fadeout(1000)
            gameProgress = gameProgress + 25
            return gameProgress
        elif options == "Kick the angel" :
            time.sleep (2)
            print ("")
            print ("You break your foot while kicking the angel resulting in your immediate death")
            mixer.music.fadeout(1000)
            gameProgress = death (inventory, situations, gameProgress)
            return gameProgress
        else :
            print("")
            options = raw_input ("Something isn't right, maybe you made a spelling mistake.")



#This function runs the code for the situation in the library.
def library (inventory, situations, gameProgress):
    mixer.init()
    mixer.music.load('F:\Python\Summative\Doctor Who Series 4 Soundtrack - 16 Silence In The Library.mp3')
    mixer.music.play (10,0)
    actionslibrary = ["Go into the next room"]
    import time
    print ("")
    time.sleep(3)
    print ("Upon arrival at the library planet you notice you are surrounded by rows upon rows of books.")
    time.sleep(4)
    print ("It's a world. The library goes on forever. The whole core of the planet is the index computer.")
    time.sleep (4)
    print ("Biggest hard drive ever.")
    time.sleep (4)
    print ("Biggest library in the universe, so where is everyone?")
    time.sleep(4)
    print ("Using the computer next to you, you decide to scan for life forms")
    time.sleep(4)
    print ("Hmmm...that's strange, when you scanned for your basic human life forms the screen goes blank.")
    time.sleep(4)
    print ("But if you widen the parameters to any kind of life the screen says")
    time.sleep (4)
    print ("A million, million lifeforms found")
    time.sleep (4)
    print ("")

    print ("options")
    print (actionslibrary)
    library = raw_input ("where do you want to go")
    #This code loops through all the possibilites for this part of the game and checks to see if the user has inputed a correct option.
    while len(actionslibrary) != 0 :
        if library == "Go into the next room" :
            print ("")
            time.sleep (2)
            print ("You enter a mostly empty room")
            time.sleep (3)
            print ("A vaguely humanoid sculpture by a curved desk turns its head and speaks")
            time.sleep (4)
            print ("")
            print ("NODE: I am Courtesy Node seven one zero slash aqua.")
            time.sleep(4)
            print ("")
            print ("NODE: Additional. There follows a brief message from the Head Librarian.")
            time.sleep(4)
            print ("Message follows. Run. For God's sake, run. Nowhere is safe.")
            time.sleep(4)
            print ("The library has sealed itself, we can't. Oh, they're here. Argh. Slarg. Snick. Message ends.")
            time.sleep (4)
            print ("")
            actionslibrary.append ("Explore the hallways")
            actionslibrary.remove ("Go into the next room")

            print (actionslibrary)
            library = raw_input ("What do you want to do next?")
        elif library == "Explore the hallways" :
            print ("")
            time.sleep (3)
            print ("Once you've entered the dimly lit hallway, lined with endless shelves of books.")
            print ("Most of the books lie on the ground. leading you to believe.")
            print ("No ones been here in a while.")
            time.sleep (6)
            print ("You notice the lights start going out one by one.")
            time.sleep (3)
            actionslibrary = []
            actionslibrary.append ("Run!")
            actionslibrary.append ("Run towards the darkness")
            actionslibrary.append ("Duck and cover")
            print ("")

            print (actionslibrary)
            library = raw_input ("What do you do?")
        elif library == "Run!" :
            print ("")
            print ("You get to the nearest door. It's locked.")
            print ("")
            print (inventory)
            actionslibrary =[]
            actionslibrary.append ("Head for the nearest exit")
            actionslibrary.append ("Go back the way you came")
            library = raw_input ("What do you do you use?")
        elif library == "Run towards the darkness" :
            time.sleep(3)
            print ("")
            mixer.music.fadeout(1000)
            gameProgress = death (inventory, situations, gameProgress)
            return gameProgress
        elif library == "Duck and cover" :
            time.sleep(3)
            print ("")
            mixer.music.fadeout(1000)
            gameProgress = death (inventory, situations, gameProgress)
            return gameProgress
        elif library == "Sonic screwdriver" :
            print ("")
            print ("The sonic has many functions including the ability to open any door.")
            time.sleep(3)
            print ("You open the door and enter a large room, before taking a look around you quickly relock the door.")
            time.sleep(4)
            print ("Taking a look around you notice the ceiling is a huge glass dome allowing the sun light to shine through.")
            time.sleep (4)
            print ("When you look around you notice something strange.")
            time.sleep(3)
            print ("To your left is your shadow")
            time.sleep (3)
            print ("To your right is a triangular shaped shadow.")
            time.sleep (4)
            print ("Taking another glance at the glass dome, you realize nothings casting the second shadow.")
            time.sleep (4)
            print ("Suddenly a woman in a astronaut suit bursts through the doors!!!")
            time.sleep (4)
            print ("")
            print ("You: You need to leave. It's not safe here.")
            print ("")
            time.sleep(4)
            print ("Woman: Professor River Song archaeologist.")
            print ("")
            time.sleep(4)
            print ("You look back at the spot where you saw the second shadow. It's gone the shadow's moved!")
            print ("")
            time.sleep(4)
            print ("You: Almost every species in the Universe has an irrational fear of the dark.")
            print ("But they're wrong. Cause it's not irrational. It's Vashta Nerada.")
            time.sleep(4)
            print("")
            print ("River: What's Vashta Nerada?")
            time.sleep(4)
            print("")
            print ("You: It's what's in the dark. It's what's always in the dark.")
            time.sleep (4)
            print ("")
            print ("You: River did you pack a lunch? I need your lunch.")
            time.sleep (4)
            print ("")
            print ("You: That's not darkness down those hallways. This is not a shadow. It's a swarm.")
            time.sleep (5)
            print ("")
            print ("River hands you a grey container. You take out a piece of chicken and throw it into the shadows.")
            time.sleep (5)
            print ("Within seconds the chicken is devoured.")
            time.sleep (5)
            print ("")
            print ("You: The piranhas of the air. Literally (The shadows that melt the flesh)")
            time.sleep (5)
            print ("")
            print ("River: So what do we do?")
            time.sleep (4)
            print ("")
            print ("You: Run just run.")
            time.sleep (4)
            print ("")
            print ("Suddenly a shadow from the corner of the room starts growing towards the two of you!!!")
            time.sleep (4)
            print ("")
            print ("River: What's going on Doctor?")
            print ("")
            print ("As you look around the room. You see two possible options")
            time.sleep (3)
            print ("")

            print (actionslibrary)
            library = raw_input ("What do you do?")
        elif library == "Head for the nearest exit" :
            time.sleep (3)
            print ("")
            print ("You enter another room similar to the last same roof, except it's evening")
            time.sleep(3)
            print("")
            print ("and soon the Sun won't provide any light for the both of you.")
            time.sleep(3)
            print ("")
            print ("You: Right! We need to figure out where they came from.")
            print ("")
            time.sleep (3)
            print ("You: The Vashta Nerada hatch from spores in trees, but we're nowhere near a forest.")
            print ("")
            actionslibrary = []
            actionslibrary.append ("No! We're surrounded by books")
            actionslibrary.append ("I don't see any trees.")
            print ("")

            print (actionslibrary)
            library = raw_input ("We're nowhere near a forest? Is that true?")
        elif library == "I don't see any trees" :
            time.sleep (3)
            print ("")
            print ("Are you sure? Try again")
            actionslibrary = []
            actionslibrary.append ("No! We're surrounded by books")
            actionslibrary.append ("I don't see any trees")
            print ("")

            print (actionslibrary)
            library = raw_input ("What next?")
        elif library == "No! We're surrounded by books" :
            print ("")
            time.sleep (3)
            print ("You: Books, they came in the books.")
            print ("Microspores in a million million books.")
            print ("A million million books hatching shadows!")
            time.sleep(5)
            print ("")
            actionslibrary = []
            actionslibrary.append ("Question River")
            actionslibrary.append ("Eat Rivers lunch")

            print (actionslibrary)
            library = raw_input ("What do you want to do next?")
        elif library == "Question River" :
            time.sleep (3)
            print("")
            print ("You: River how did you get here and why?")
            time.sleep (3)
            print ("")
            print ("River : I got a message, it said the library had sealed it self.")
            print ("the data fragment said 4,022 people saved no survivors.")
            time.sleep(3)
            print ("")
            print ("You: River the data fragment you recieved what if it acctually meant saved?")
            time.sleep (3)
            print ("")
            print ("You: So a hundred years ago, massive power surge.")
            print ("All the teleports going at once soon as the Vashta Nerada hit thier hatching cycle")
            print ("they attack and someone hits the alarm.")
            time.sleep (4)
            print ("")
            print ("You: 4,022 people about to be teleported, but nowhere to go. They're stuck in the system.")
            time.sleep (4)
            print ("")
            print ("You: All waiting to be sent like emails.")
            time.sleep (3)
            print ("")
            print ("You: The computer saved 4,022 people the only way it can. It saved them to the hard drive.")
            time.sleep (5)
            print ("")
            actionslibrary =[]
            actionslibrary.append ("Go to the hard drive")
            actionslibrary.append ("Read a book")
            print ("")

            print (actionslibrary)
            library = raw_input ("What do you do?")
        elif library == "Eat Rivers lunch" :
            time.sleep(3)
            print ("")
            print ("You grab the rest of Rivers chicken and start eating her lunch. Yummy!")
            time.sleep(3)
            print ("")
            print ("River: Doctor! What are you doing? Shouldn't we be trying to get out of this mess?")
            time.sleep(3)
            print ("")
            print ("You: Yes! Right!")
            actionslibrary = []
            actionslibrary.append ("Go to the hard drive")
            actionslibrary.append ("Read a book")
            print (actionslibrary)
            library = raw_input ("What next?")
        elif library == "Go to the hard drive" :
            print ("")
            time.sleep (3)
            print ("Once you've entered to core of the planet (hard drive).")
            time.sleep(3)
            print ("You beam all the people out of the data core.")
            time.sleep (3)
            print ("4,022 are brought back into the library!!!")
            mixer.music.fadeout(1000)
            gameProgress = gameProgress + 25
            return gameProgress
        elif library == "Read a book" :
            time.sleep (3)
            print ("")
            print ("Reading isn't the greatest option right now!")
            actionslibrary.remove ("Read a book")

            print (actionslibrary)
            library = raw_input ("Where do you want to go?")
        elif library == "Go back the way you came" :
            print ("")
            time.sleep(3)
            print ("You decide to run to the door you just came through")
            time.sleep (3)
            print ("As you reopen the door, you forgot you'd been running from the shadows.")
            time.sleep (3)
            print ("The hallway you entered 20 minutes ago is now pitch black.")
            time.sleep (3)
            print ("Unfortunately both of you were corned by the Vashta Nerada and died.")
            mixer.music.fadeout(1000)
            gameProgress = death (inventory, situations, gameProgress)
            return gameProgress
        elif library == "phychic paper" :
            print ("Phychic paper doesn't open doors. Idiot")
            mixer.music.fadeout(1000)
            gameProgress = death (inventory, situations, gameProgress)
            return gameProgress
        else :
            print ("")
            print ("Sorry that's invalid")
            library= raw_input ("Maybe you made a spelling mistake.")


#This code initiates the start screen.
inventory = ["Sonic screwdriver", "psychic paper"]
situations = ["Go Home (planet Gallifrey)", "Go to Berlin, Germany", "Dark house across the street", "Visit the library, 5123 (Library planet)"]
gameProgress = startScreen (inventory, situations)
print ("")
print ("(options)")
print (situations)
place = raw_input ("Where do you want to go?")

#This loop loops through the different game scenarios until the program is ended or the user completes the game.
while (gameProgress != 100) :
    mixer.music.fadeout(1000)
    if place == ("Go Home (planet Gallifrey)") :
        situations.remove ("Go Home (planet Gallifrey)")
        gameProgress = homeGallifrey (inventory, situations, gameProgress)
        if gameProgress == 0:
            situations.append ("Go Home (planet Gallifrey)")
        if gameProgress != 100:
            print ("")
            print (situations)
            place = raw_input ("Where to?")
    elif place == ("Go to Berlin, Germany") :
        situations.remove ("Go to Berlin, Germany")
        gameProgress = berlinGermany (inventory, situations, gameProgress)
        if gameProgress == 0:
            situations.append ("Go to Berlin, Germany")
        if gameProgress != 100:
            print ("")
            print (situations)
            place = raw_input ("Where to?")
    elif place == ("Dark house across the street") :
        situations.remove ("Dark house across the street")
        gameProgress = darkHouse (inventory, situations, gameProgress)
        if gameProgress == 0:
            situations.append ("Dark house across the street")
        if gameProgress != 100:
            print ("")
            print (situations)
            place = raw_input ("Where to?")
    elif place == ("Visit the library, 5123 (Library planet)") :
        situations.remove ("Visit the library, 5123 (Library planet)")
        gameProgress = library (inventory, situations, gameProgress)
        if gameProgress == 0:
            situations.append ("Visit the library, 5123 (Library planet)")
        print ("")
        if gameProgress != 100:
            print (situations)
            place = raw_input ("Where to?")
    else:
        place = raw_input ("I don't quite know that place, sorry, maybe somewhere else?")
#The user reaches this point if they have completed the game.
time.sleep (2)
print ("")
print ("Congratulations, you have discovered 100% of the game! You're not a COMPLETE idiot after all.")
time.sleep (2)
print ("...just a slight one")
time.sleep (2)
print ("")
print ("Come play again sometime soon and prove your worth! Now for some words of inspiration from Shia LaBeouf.")
mixer.init()
mixer.music.load('F:\Python\Summative\Shia LaBeouf Just Do It Motivational Speech ? Original Video.mp3')
mixer.music.play (2,0)
time.sleep(60)
mixer.music.fadeout(1000)







