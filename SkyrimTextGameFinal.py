import random

#
# Kent Kober and Helen Meng
#
# Skyrim Text Game
#

class Player:
    def __init__(self,name):
        """initializes a player object that simulates a warrior in Skyrim

    name - the name of the player"""

        #initializing the instance variables
        self.name = name
        self.health = 100
        self.gold = 100
        self.inventory = []

    def reset(self):
        """resets the player's stats for a new game"""

        #reseting all of the instance variables
        self.health = 100
        self.gold = 100
        self.inventory = []

    def getHealth(self):
        """returns the integer value that represents the player's health"""

        #returing the health variable
        return self.health

    def getName(self):
        """returns the player's input name in string format"""

        #returing the name variable 
        return self.name

    def getInventory(self):
        """returns a list of all of the objects in the player's inventory"""

        #returning the inventory list
        return self.inventory

    def changeHealth(self, change):
        """change's the player's overall health by a specfic amount

    change - the amount the health is changed. Positive values increase the
             player's health and negative values decrease it"""

        #changing the health variable
        self.health = self.health + change

    def addItem(self,item):
        """adds an item to the player's inventory. If it's a potion, it also
adds the effect to the player.

    item - the item object to be added to the player's inventory."""

        #adding the item to the inventory variable
        self.inventory.append(item)

        #getting the item effect
        x = item.getEffect()

        #seeing if the item has an effect
        if x != None:

            #going through all of the possibilities and changing the player's
            #stats accordingly
            if x == "inchealth": self.changeHealth(5)
            elif x == "dechealth": self.changeHealth(-5)
            elif x == "incpower": self.changeHealth(5)
            elif x == "decpower": self.changeHealth(-5)
            elif x == "FrostIncPower": self.changeHealth(5)
        
    def getGold(self):
        """returns the current amount of gold in the player's pocket"""

        #returing the gold variable
        return self.gold

    def changeGold(self,change):
        """changes the amount of gold the player has by a specfic amount

    change - the amount of gold to be changed. A positive amount will increase
             the amount of gold and a negative number will decrease it."""

        #changing the gold variable
        self.gold = self.gold + change

    def getScore(self,inventory):
        """returns a number that represents the overall score that the player has.

    inventory - the player's inventory"""

        #checking for the base case
        if len(inventory) ==0:
            #returning the player's health
            return self.health

        #running the recursive part
        else:
            #returning the first object's power in the inventory and calling the
            #the function again for the rest of the items
            return inventory[0].getPower() + self.getScore(inventory[1:])

class Opponent:
    
    def __init__(self,name,items,power):
        """creates an opponent in skyrim that has power and weapons

    name - the name of the opponent
    items - a list of all of the items that the opponent has
    power - the power that the opponent has"""

        #initializing the instance variables
        self.name = name
        self.items = items
        self.power = power

    def getName(self):
        "returns the name of the opponent"

        #returning the name variable
        return self.name

    def getInventory(self):
        "returns all of the items that the opponent has"

        #returning the items list variable
        return self.items

    def getPower(self):
        """returns the opponent's power"""

        #returing the power variable
        return self.power

class Wizard(Opponent):

    def printRiddle(self):
        """asks the user a random riddle and checks if their answer is correct"""

        # list of correct riddle answers and corresponding questions
        answers = ['silence','wholesome','ton']
        questions = ['Say my name and I dissapear. What am I?',
                     'What is it that after you take away the whole, still some remains?',
                     'Forward I am heavy, but backwards I am not. What am I?']

        # selecting a random riddle from questions list and printing it
        prompt = questions[random.randint(0,2)]
        print(prompt)

        # prompting user for answer
        answer = input("\nYour answer: ")

        # if the answer is in the list of answers then print correct and run potions
        if answer.lower() in answers:
            print("\nThat is correct!")
            print("\nI am impressed. Very rarely does someone answer my riddles correctly.")
            return self.potions()

        # else print incorrect statement 
        else:
            print("\nThat is incorrect!")
            print("I'm sorry, but you will not be recieving any potions today.")

    def potions(self):

        """creates potion items and allows user to choose a potion"""

        # create list of corresponding potion names and effects
        name = ['Argonian Blood','Redguard Tears','Imperial Elixir','Dragon Tears','Khajiit Extract']
        effect = ['inchealth','incpower','FrostIncPower','dechealth','decpower']
        # create dictionary of print statements that are printed when user selects a potion to inform
        # them of the potion's effect
        names = {'Argonian Blood':'\nYou are a fortunate one. \nThe Argonian Blood has given you added health.',
        'Redguard Tears':'\nYou are a fortunate one. \nThe Redguard Tears have given you added power.',
        'Imperial Elixir':"\nYou have harnessed the power of Morrowind's Frost Bolt and gained Frost Damage power.",
        'Dragon Tears':'\nHow unfortunate. The Dragon Tears have damanged your muscles and thus decreased your health.',
        'Khajiit Extract':'\nHow unfortuante. The Khajiit Extract has caused you to lose some of your power.'}
        # create empty list potions and add potion items to list
        potions = []
        for i in range(5):
            potions.append(Potion(name[i],effect[i]))

        # print warning statement and potions list
        print("Since you answered my riddle correctly, I will grant you the potion I promised.")
        print("Here are all the potions I have, but I will not tell you the potions' effects!")
        print("You have been warned.")
        print()
        print("Here is a list of my powerful potions: ")
        print()
        c = 1
        for i in name:
            print(str(c)+".",i)
            c = c + 1
        print()
        # check and get user input for potion selection
        choice = check("Which potion do you desire? (1,2,3,4, or 5?) ",[1,2,3,4,5],0)
        print(names[name[int(choice) - 1]])
        # also award one blade
        print("""\nI will also award you one Blade of Woe for your journey.
\nNow be off, my friend. And remember, beware.\n\n""")
        # return potion item the user chooses
        return potions[int(choice) - 1]


class Item:
    def __init__(self,name,power,cost):
        """creates an item with a name, power, and specific cost

    name - the item's name
    power - the item's power
    cost - the item's cost"""

        #initializing the instance variables
        self.name = name
        self.power = power
        self.cost = cost

    def getCost(self):
        "returns the cost of the item"

        #returning the cost variable
        return self.cost

    def getPower(self):
        "returns the item's power"

        #returning the power variable
        return self.power

    def getName(self):
        "returns the item's name"

        #returning the name variable
        return self.name

    def getEffect(self):
        "returns the item's effect"

        #returning none because normal items do not have effects
        return None

    def __str__(self):
        "allows the object to be printed by a vendor"

        #properly formating all of the information
        x = "{0:<25}".format(self.name) + "Power: {0:<15}".format(self.power)
        x = x + "Gold: {0:<10}".format(self.cost)

        #returning the formatted string
        return x

    
class Potion(Item):

    def __init__(self,name,effect):
        """create potion object"""
        # save name and effect in object
        self.name = name
        self.effect = effect

    def getEffect(self):
        """returns effect of potion"""
        return self.effect
    
    def getName(self):
        """returns name of potion"""
        return self.name
    
    def getPower(self):
        """returns potion power"""
        return 0

#
# check()
#
# this program asks the user for an input and keeps asking until a proper
# response has been made
#
# inputs: question - the question you want to ask the user
#         validAnswers - a list of all of the valid answers in string form
#         exactness - the level of exactness that you want the user's input to be
#                    (0) - the user needs to exactly input one of the answers
#                    (1) - the user only needs to get the first letter of one
#                          of the answers correct
#                    (2) - same as 0, but the correct answers will not be printed
#                          every time the user inputs a wrong answer. Useful for
#                          questions with a ton of answers
#
# outputs: x - the user's answer in string form
#
def check(question,validAnswers,exactness):

    #making a correct prompt that details every correct answer
    prompt = "That input was incorrect. The choices are "
    for i in validAnswers:
        prompt = prompt + str(i) + ", "
        validAnswers[validAnswers.index(i)] = str(i).upper()
    prompt = prompt[:-2]

    #while loop to keep getting the user input
    while True:

        #initializing a test varaible
        test = False

        #getting the user's input
        x = input(question)

        #checking to see if the exactness is 0
        if exactness == 0:
            #checking to see if the input matches one of the answers
            #and breaking
            if x.upper() in validAnswers: break

        #checking to see if the exactness is 1
        elif exactness == 1:

            #checking to see if the user input matches any of the answers' first
            #letters and if so, changing the test variable to true
            for i in validAnswers:
                if x != "" and i[0] == x[0].upper():
                    test = True
                    
            #checking to see if the test variable is true, and if so, breaking
            #the while loop
            if test == True: break

        #checking to see if the exactness is 2
        elif exactness == 2:

            #seeing if the user input matches any of the valid answers and breaking
            if x.upper() in validAnswers: break

            #catching if the user had a wrong input
            else:
                #telling the user to pick a correct name and restarting the while loop
                print("\n Please give a correct name\n")
                continue
        #printing the prompt to the user
        print("\n" + prompt +"\n")

    #returning the correct input string
    return x
                    
                
class Game:
    def __init__(self):
        """creates a game of Skyrim for the user to play"""

        #initializing a player variable
        self.player = Player(input("Please enter your name: "))

        #initializing the wizard instance variable
        self.Wizard = Wizard("Wizard",[],0)
        

    def play(self):
        """runs through one trial of Skyrim"""

        #runs the first city
        self.__Windhelm()

        #checking to see if the user wants to play again
        x = check("Do you want to play again? ", ["yes","no"],1)

        #checking to see if they said yes
        if x[0].upper() == "Y":

            #reseting the player
            self.player.reset()

            #playing again
            self.play()

        #if the user said no, stopping the program
        else: print("\nGoodbye")
        


    def __Windhelm(self):
        """prints game intro, decree from king"""
        print()
        print(self.player.getName())
        # print the official decree
        print("""\n\nA DECREE FROM THE PALACE OF WINDHELM IN THE LAND OF SKYRIM \nA SUMMON FROM THE KING OF SKYRIM
\n\nYou are hereby summoned by the King of Skyrim to fight on behalf of the kingdom
in the quest to slay the DRAGON of Markarth.
\n\nYour quest is a dangerous one. In return for killing the DRAGON, the King
will declare you a Knight and royal savior of the city. You will be granted
a generous plot of land and more gold than you could ever imagine.
\nYou are to depart the Kingdom immediately and travel to Markarth.
\nYou have been granted 100 gold coins that you may use to purchase weapons on your way to Markarth.
\nBe wary brave soldier, for this is no easy quest.
\n\nThe King and kingdom of Windhelm thanks you for your service and sacrifice
to protect this great land of Skyrim.
\n\nGodspeed.
\n\nSigned and Approved by King Christopher Thalmor Snow IV""")
        # wait for user to enter
        input("\nPress <enter> to continue")
        # run whiterun 
        self.__Whiterun()

    def __Whiterun(self):
        """runs through the Whiterun city"""

        #printing information to the user
        print("""\n\nAfter weeks of travel, you have finally reached Whiterun. Because the dragon
already destroying things, time is of the essence. Therefore, once you choose
a path, you will not be able to come back again. At the gates of Whiterun you
see main street to your left and residential houses to the right.\n""")

        #checking to see if the user wants to go left or right
        x = check("Do you want to go left or right? ", ["left","right"],1)

        #checkign to see if the user picked left
        if x[0].upper() == 'L':

            #running the whiterun main street function
            self.__WhiterunMainStreet()

        #catching if the user picked to go right
        else:

            #running the whiterun residental function
            self.__WhiterunResidential()

        #giving the user a pause
        input("Press <enter> to continue\n")

        #telling the user some more information
        print("""You have reached the end of the road at Whiterun. Now you must choose where to
go next. On your map of Skyrim, you see that there is a city to the North and
to the South. To the North there is Swindler's Den and to the South there is
Sleeping Tree Camp\n""")

        #checking to see if the user wants to go north or south
        y = check("Do you want to go North or South? ",["North","South"],0)

        #running the appropriate function given the user's input
        if y.upper() == "NORTH": self.__SwindlersDen()
        else: self.__SleepingTreeCamp()


    def __WhiterunMainStreet(self):
        "allows the player to walk down whiterun's main street"

        #printing some information
        print("""\nAs you're walking down Whiterun's main street, you see an iron dagger on the
ground. As you look around, there are no guards in sight. After some
diliberation, you realize that a decision need to be made.\n""")

        #seeing if the user wants to steal the dagger
        x = check("Do you want to steal the dagger? ", ["yes","no"],1)

        #checking if the user said yes
        if x[0].upper() == "Y":

            #generating a random number for a 50-50 chance of success
            g = random.randint(0,1)

            #checking to see if the random number was zero
            if g == 0:

                #telling the user that the user failed the theft
                print("""\nYou take the iron dagger and put it in your pocket. Unfortunately, when you
were diliberating with yourself, a Whiterun guard walked onto main street and
saw you steal the dagger. You offer to give the guard a bribe to keep quiet.
The guard accepts the bribe, but after you pay him the 15 gold, he arrests you
and forces you to give him the stolen dagger. Maybe next time you should try not
to steal.\n""")

                #changing the player's gold
                self.player.changeGold(-15)

            #otherwise the number was 1
            else:
                #telling the user that they successfully stole the dagger
                print("""\nYou take the iron dagger and put it in your pocket. As you are about to turn
around, you hear the footsteps of what must be a Whiterun guard. You know he's
on to you, so you quickly dart behind on the houses and hide in a small cabbage
field. After you wait a few minutes, the guard gives up his search and walks
back to his post. You have successfully stolen the dagger.\n""")
                
                #adding the dagger item to the player's inventory
                self.player.addItem(Item("Iron Dagger",10,0))
                
        #catching if the user didn't want to steal the dagger
        else:
            #telling the user some information
            print("""\nAs you walk past the iron dagger, you see a Whiterun guard turn onto the main
street. You decide to tell the guard about the dagger. The guard informs you
that the owner of the dagger had a reward for finding it. The guard happily
gives you 5 gold in exchange for the dagger.\n""")

            #adding 5 to the player's gold
            self.player.changeGold(5)

    def __WhiterunResidential(self):
        "allows the player to walk through the residential area of Whiterun"

        #printing some information
        print("""\nAs you walk through the residential part of Whiterun, you come across a
homeless person on the side of the road. He asked you for a generous donation
of 5 gold.\n""")

        #checking to see if the user wants to give the homeless person money
        x = check("Do you want to give the 5 gold? ", ["yes","no"],1)

        #checking to see if the user said yes
        if x[0].upper() == "Y":
            #telling the user what happened
            print("""\nYou give the homeless person the 5 gold, and as you bend down, a homeowner sees
your generous act. She is pleased with your generousity and comes outside to
talk with you. She gives you a basket full of food to repay your kindness. This
food increases your maximum health by 10 points.\n""")
            
            #adding 10 to the player's health
            self.player.changeHealth(10)
            
        #checking to see if the user didn't want to give money
        else:

            #telling the user what happened
            print("""\nYou walk by the homeless man without even looking twice. A homeowner sees your
actions and wonders what the world has come to. Your gold remains unchanged.\n""")


    def __SwindlersDen(self):
        """prompts user with wizard story and asks to solve riddle"""
        # prints scene prompt 
        print("""\n\nThe night grows cold and dark. Snow falls gently from the grey clouds hanging in
the sky. You walk along a path lined with tall pine until you see a small flame
growing closer in the woods. As the flame approaches you see the shadowy outline
of a sweaping coat and tall pointed hat. The figure continues to approach you,
and you soon realize that the tall man before you is a wizard. He begins to
speak.""")
        # wait for user to continue
        input("\nPress <enter> to continue\n")
        # wizard introduces himself
        print("""\nGreetings, wary traveler. My name is Belthere, Wizard of the
West. I can see that you are on some sort of journey, serving your kingdom, no
doubt. I, too, wish to serve my King and Kingdom, and so I offer you, brave
warrior, this challenge. A warrior must not only be of strong heart and body
but strong in the mind. If you can answer my riddle correctly, I will give you a
potion of your choice and one weapon. If you answer incorrectly, we will both
depart on our separate ways, and I will have only my prayer of protection for
you as you continue on your journey.\n""")
        # asks whether or not user wants to try and solve riddle
        x = check("Would you like to take a stab at my riddle? ",["yes","no"],1)
        print()
        # if user says yes print riddle and printriddle returns potion (user solved
        # correctly) then add potion item and blade of woe
        if x[0].upper() == "Y":
            potion = self.Wizard.printRiddle()
            if potion != None:
                self.player.addItem(potion)
                self.player.addItem(Item("Blade of Woe",10,0))
        # else just print farewell statement
        if x[0].upper() == "N":
            print("""Alright. I wish you well on your quest, brave knight.\n
Remember, in this land, no one is your ally, and everyone is your foe.\n\n """)
        print("You now must travel to Rorikstead")
        input("\nPress <enter> to continue")
        # run rorikstead
        self.__Rorikstead()



    def __SleepingTreeCamp(self):
        "allows the user to go through sleeping tree camp"

        #printing information to the user
        print("""\nAfter traveling for a couple of days, you finally see a smoke stack in the
distance. As you get closer, you realize that you have reached Sleeping Tree
Camp. Even though it's almost midnight, there are a couple of people around the
fire. One of the residents of Sleeping Tree gives you some hot food so you can
replenish. When telling travelling stories, one of the drunk residents begins
to think that you are lying. This anger turns into violence. You can either
choose to fight this resident or give him money to calm him down.\n""")

        #getting the user's score
        n = self.player.getScore(self.player.getInventory())

        #seeing if the user's score is less than 100
        if n < 100:

            #setting the odds to 55%
            x = 55

            #telling the user of the odds
            print("""Unfortunately, because you're unarmed, the chances of survival are slim. You
only have a 55% chance of survival.\n""")

        #catching when the user's score has incresaed    
        else:

            #setting the odds at 70%
            x = 70

            #telling the user about the 70%
            print("""Because your stats have increased, you have a great chance of survival. You
have a 70% chance of survival.\n""")

        #asking the user if they want to fight
        b = check("Do you want to pick the fight?",["yes","no"],1)

        #checking to see if the user said yes
        if b[0].upper() == "Y":

            #picking a random number between 1 and 100
            temp = random.randint(1,100)

            #checking to see if the random number was less than the odds number
            #and running the win funtion
            if temp < x: self.__SleepingTreeCampWin()

            #otherwise, running the loss function
            else:
                self.__SleepingTreeCampLoss()
                return 1

        #checking to see if the user did not want to fight    
        else:
            #printing information to the user
            print("""\nThe resident stands up and some of the other people around the fire hold him
back. You offer to give a little money to make everyone happy. The angry
resident takes your offer and you barter a trade. You want to give him 5 gold,
but you end up agreeing on 10 gold. You pay the resident 15 gold out of your
pocket.\n""")

            #decreasing the user's gold by 10
            self.player.changeGold(-10)

        #allowing the user to pause
        input("Press <enter> to continue")

        #telling the user it is time to move on
        print("""\nAfter that ordeal, you realize that it's time to move on. You start off on your
trek to Rorikstead.\n""")

        #allowing the user to pause
        input("Press <enter> to continue")

        #calling Rorikstead
        self.__Rorikstead()

    def __SleepingTreeCampWin(self):
        "tells the user that he/she has won the fight"

        #making an opponent object
        resident = Opponent("Rauli",[Item("Glass Mace",25,0),Item("Health Potion",10,0)],100)

        #printing information to the user
        print("""\nYou stand up and make the first move. You make two quick jabs to his face and
he is stunned. While ther resident is stumbling back, you hit him with the
bus-driver upcut. The resident imidiately falls to the ground. You move in to
curbstomp him, but the other residents stop you. They tell you that you are no
longer welcome at the camp, but they allow you to take all of the items on the
person that you knocked out.

You have acquired a glass mace, a health potion and a 30 gold.\n""")

        #adding all of the plunder to the user's inventory
        for i in resident.getInventory():
            self.player.addItem(i)
        self.player.changeGold(30)
        
        

    def __SleepingTreeCampLoss(self):
        "tells the user that he/she has lost the fight"

        #printing infomation to the user
        print("""\nAs you stand up, the resident makes a quick right jab. You stagger backwards
and realize that you face is bleeding. You able to gather yourself and kick the
resident a couple of times. Unfortunely this is not very effective, and while
kicking, you leave yourself vunerable. The resident gives you an uppercut and
you fall down. He hits you a couple more times before you lose consciousness.
After a few hours you bleed out.\n\nYou Lost\n""")

    def __Rorikstead(self):
        "allows the player to walk through Rorikstead"

        #prints information to the user
        print("""\nWhen you get to Rorikstead, you see a blacksmith in the town square.
You walk over to him because you have money to spend and you need to get some
weapons to fight the dragon. Don't be afraid to spend your money, the faster
you get your weapons, the faster you can take the dragon down.\n""")

        #allows the user to pause
        input("Press <enter> to continue")

        #while loop to run through the blacksmith vendor
        while True:

            #checking to see if the user does not have enough gold
            if self.player.getGold() < 2:

                #telling the user that they do not have enough money
                print("You ran out of money, so you left.")
                #breaking the while loop
                break

            #welcoming the user to the Blacksmith
            print("\nWelcome to the Blacksmith\n")

            #checking to see if the user wants to purchase a weapon
            a = check("Do you want to purchase a weapon? ",["yes","no"],1)

            #if the user said no, breaking the while loop
            if a[0].upper() == "N": break

            #running the blacksmith program
            self.__Blacksmith()

        #telling the user about some information
        print("""\nAfter you finish with the blacksmith, you realize it's night time. You
realize that it is time for the battle. You must go to Markarth tonight. Good
luck warrior, you are going to need it.\n""")

        #running the markarth function
        self.__Markarth()

    def __Blacksmith(self):

        #creating multiple reference lists
        a = ["Blade of Woe","Borvir's Dagger","Iron Dagger","Orcish Dagger","Shiv",
             "Daedric Mace",'Iron Mace','Steel Mace',"Amren's Family Sword",
             "Drainheart","Imperial Sword","Iron Sword","Soulrender",
             "Nightingale Blade","Ancient Nord War Axe","Daedric War Axe","Forsorwn Axe",
             "Illusory War Axe","Iron War Axe","Pickaxe","Ancient Nord Bow",
             "Angi's Bow","Froki's Bow","Forsworn Bow","Imperial Bow","Fork","Knife"]
        b = [12,8,4,6,5,16,9,10,7,11,8,7,13,14,9,15,11,2,8,5,8,7,6,12,6,2,3]
        c = [88,18,10,30,5,175,35,65,25,73,23,25,100,165,15,150,90,15,30,5,
             45,50,30,145,30,2,3]

        #printing the item info to the user
        self.__BlacksmithPrint()

        #asking the user which weapon they want
        x = check("Which weapon do you want? ",a,2)

        #initializing a reference variable
        reference = []

        #for loop to go through all of the weapon names
        for i in a:
            #adding each weapon name to a reference list
            reference.append(i.upper())

        #getting the indes of the weapon that the user chose
        Index = reference.index(x.upper())

        #checking to see if the player has enough gold to make the transaction
        if self.player.getGold() < c[Index]: print("You do not have enough gold to make that transaction.")

        #giving the player the item because he/she has enough gold
        else:
            #adding the item object to the user's player's inventory
            self.player.addItem(Item(a[Index],b[Index],c[Index]))

            #changing the player's gold
            self.player.changeGold(-1*c[Index])

            #telling the user that the item has been successfully added
            print(a[Index].title() + " has been added to your inventory.")

    def __BlacksmithPrint(self):
        "prints out all of the options for the blacksmith vendor"

        #defining reference lists
        a = ["Blade of Woe","Borvir's Dagger","Iron Dagger","Orcish Dagger","Shiv",
             "Daedric Mace",'Iron Mace','Steel Mace',"Amren's Family Sword",
             "Drainheart","Imperial Sword","Iron Sword","Soulrender",
             "Nightingale Blade","Ancient Nord War Axe","Daedric War Axe","Forsorwn Axe",
             "Illusory War Axe","Iron War Axe","Pickaxe","Ancient Nord Bow",
             "Angi's Bow","Froki's Bow","Forsworn Bow","Imperial Bow","Fork","Knife"]
        b = [12,8,4,6,5,16,9,10,7,11,8,7,13,14,9,15,11,2,8,5,8,7,6,12,6,2,3]
        c = [88,18,10,30,5,175,35,65,25,73,23,25,100,165,15,150,90,15,30,5,
             45,50,30,145,30,2,3]

        #initializing the list
        weapons = []

        #for loop to run through all of the reference list members
        for i in range(len(a)):

            #adding a new item object to the weapons list
            weapons.append(Item(a[i],b[i],c[i]))

        #making sure the list is in the right order
        weapons.reverse()

        #properly formating the text
        print("\n")

        #initializing new reference lists
        text = ["Daggers:","\nMaces:","\nSwords:","\nWar Axes:","\nBows:",""]
        nums = [5,3,6,6,5,2]

        #for loop to run through all of the categories
        for i in range(len(text)):

            #printing the category name
            print(text[i])

            #for loop to run through the number of items in each category
            for j in range(nums[i]):

                #printing the next item objec
                print(weapons.pop())

        #telling the user how much gold they have
        print("You have " + str(self.player.getGold())+ " gold left.")

    def __Markarth(self):
        """prints final boss battle of Markarth"""
        # print scene intro
        print("""\nYou reach the land of Markarth. The ground trembles as you feel the dragon's
each step, slowly rupturing the ground beneath it. You tremble, and tucked
behind a tall pine in the wood you can see the dragon's tail wisping back and
forth between the trees. You prepare yourself. You go through a list of all the
weapons you have brought with you to the battle.""")
        # run through all inventory items and print
        x = self.player.getInventory()
        c = 1
        for i in x:
            print("\n"+str(c)+". ",i.getName())
            c = c + 1
        input("\nPress <enter> to continue")
        # if user has no items set text to nothing
        if len(x) == 0:
            text = "nothing"
        # else set text to first item in inventory
        else: text = str(x[0].getName())
        print("""\n\nYou creep out from behind the trees. You stand face to face
with the dragon whose fiery breath steaming from its nostrils creates a dull
ring of smoke. \n\nYou are ready.
\nYou charge at the dragon, aiming for his left eye. The dragon swings its tail
and knocks you to the ground. It takes you a moment to recover, but again you
are on your feet and you see that the dragon has gotten closer. Your reach for
your """+text+""" and use it to drive a hole in the dragon's chest.
The dragon shrieks a cry of pain. You can feel it losing strength. You charge
again and climb on top of the dragon's head. The dragon swings its head back
and forth, you cling on to its scales with every last inch of strength you
posses. The dragon continues to forcefully swing its body against the trees.
You manage to avoid the large branches but you see that your legs have been
badly cut up and bruised.""")
        input("\nPress <enter> to continue")
        # if the user's score is over 150 then run win else print final message
        if self.player.getScore(self.player.getInventory()) >= 150: self.win()
        else:
            print("""\n\nAnd now, the final push. You use every weapon in your possession, slashing the
dragon's scales, you see the dragon's blood beginning to bleed through its
tough skin. The dragon begins to waver and stumbles as it fails to regain its
balance. You swing by a tree and notice that the dragon's repeated thrashing
against the trunk has weakened it to the point that it seems about to snap.
Your weapons lay scattered near the dragon's feet. You jump off the dragon and
run towards the splintering tree. You position yourself right by the last few
threads of bark that hold the tree together and wait. The dragon swings its
tail around just as you throw yourself to the ground. The dragon's tail swings
to meet the bark of the tree and it slowly begins to creek, falling over like a
brave knight. The dragon flies up to avoid the tree's crushing force, but just
as it takes off it breathes a ball of flame at you lying there amongst the
trees. You realize you are surrounded by fire and pine with no escape. You stand
amongst the brush and utter your final words.
\nI am sorry my King. I have failed.""")


    def win(self):
        """printing the win statement if user wins boss battle"""
        # print the final message saying the action and 
        print("""\n\nAnd now, the final push. You use every weapon in your possession, slashing the
dragon's scales, you see the dragon's blood beginning to bleed through its
tough skin. The dragon begins to waver and stumbles as it fails to regain its
balance. You swing by a tree and notice that the dragon's repeated thrashing
against the trunk has weakened it to the point that it seems about to snap.
Your weapons lay scattered near the dragon's feet. You jump off the dragon and
run towards the splintering tree. You position yourself right by the last few
threads of bark that hold the tree together and wait. The dragon swings its
tail around just as you throw yourself to the ground. The dragon's tail hits
forcefully against the trunk. The tree snaps, and with a slight groan cracks
and falls, crushing the dragon beneath it.
\n\nYou come out from behind the trees to see the dragon lying motionless
on the ground and you realize.. \n\nYou did it. You have won.""")



#
# main()
#
# runs through the game of skyrim
#
# inputs: none
# 
# outputs: none
#
def main():
    #defining a new game object
    x = Game()

    #running the game
    x.play()

main()
            
