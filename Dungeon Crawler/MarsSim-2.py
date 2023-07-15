#Global Variabes
health = 100
play_again = True

# Create dictionary for puzzle hints for the user.
Dungeon_guide = {
    # ';' will separate the word and its definition
    "Puzzle 1": "Be sure to look at what is hidden... you may be tricked if you aren't careful...",
    "Puzzle 2": "A door that cannot be opened without the knowledge of shapes, ensure you think carefully before making your decision.",
    "Puzzle 3": "Less of a puzzle and more of an 'encounter' to say the least... adventurer please ensure you are careful with the beast deep inside the cavern."
}


# a function named CheckHealth will see the value of health and describe your situation accordingly
def CheckHealth(health, play_again):
    # print statement to show the player their health
    # you cannot concatonate an int with a string so you have to make the int value a string using str
    print("Your health is " + str(health))
    # if statements to show you the correct print statement
    if health == 100:
        print("You are healthy and alive, but you still feel uneasy.")
    if health == 75:
        print("You have a few minor wounds, but they won't hold you back.")
    if health == 50:
        print("You have sustained a few major hits and it has become hard to walk...")
    if health == 25:
        print("Your open would continue to bleed and the pain is the only thing keeping you awake.")
    # if health = zero take user input and ask if the player will play again
    if health == 0:
        print("Your eyes begin to cloud, and you can't see or feel a thing.")
        print(" Thank you for playing my game! ")
        print("Would you like to play again?")
        user_choice = input("Enter 'y' to play again or 'n' to stop.")
        if user_choice == "y":
            return
        if user_choice == "n":
            play_again = False
            quit()

        
# intro prints
def DisplayTitle():
    print("*** Welcome to The Dungeon Crawl! ***")
    print("Please be careful when entering the cave!")
# function that gets the players name an their input and returns the variable value
def GetPlayerName():
    player_name = input("Please enter your adventuerer name...")
    return player_name
# gather player_name and use it to display the player_name
def Introduction(player_name):
    print("You look into the darkness and see nothing.")
    print("The cave you see is your mission, and you have no other choice but to succeed.")
    print("If you complete this mission you will become the greatest adventurer alive.")
    print("You must find and slay the dragon resting inside.")
    print("Many have entered but never left...")
    print("You are scared...")
    # Use concatination to use a variable in a print statement
    print("But the name '" + player_name + " the dragon slayer' rings in your head.")
    print("You notice a sign that says 'DO NOT ENTER' as you walk into the dark.")
    print("You look in your pocket and notice that you have a paper to warn you of things in the dungeon.")
    user_choice = input("Would you like to read it?")
    if user_choice == "y":
        # if user wants to read then we need to set the value and number for the dictionary, here puzzle_num is the number used to iterate and Dungeon_guide.items(): will list the definition for the value
        for puzzle_num, value in Dungeon_guide.items():
            print(puzzle_num,' : ', value)
    if user_choice == "n":
        print("You stuff the paper back into your pocket.")
# first health decrease
def GoblinAttack(health):
    print("You begin to walk in and notice that there is a fork, you have to choose the left tunnel or the right...")
    print("You notice that the left tunnel has many torches lighting the way, this is odd because it seems to be hiding the right tunnel.")
    print("You do not notice anything special about the tunnels except the torches there to obscure the right tunnel.")
    print("What will you do? Take the Right or Left tunnel?")
    #take user input
    user_choice = input(" Please enter 'r' or 'l'")
    if user_choice == "r":
        print(" Noticing the obvious trick you follow the hidden tunnel and find a goblin lair...")
        print("You steathily find your way past the goblins while they are asleep.")
    if user_choice == "l":
        print("You chose to enter the well lit path, after a few minutes of walking you begin to hear snickering ahead of you.")
        print("You ready your blade and face your opponent. You see half a dozen goblins lying in wait...")
        print("You ready your first swing and take one out quickly. The others begin to run around scared, but as you chase them around you hear something from behind you...")
        print("The same snickering you heard is coming from the other direction!")
        print("Before you can react you feel a sharp pain in your shoulder, an arrow shot my the goblins...")
        print("You think 'Damn, I knew something was hiding that other tunnel...' ")
        print("You eventually take down the goblins, but not without taking a few hits from their arrows and blades.")
        #decreases health by 25 and returns the new value
        health = health - 25
    return health

def PlayerPuzzle(health):
    # here we create a list for the different options for the puzzle separate by ','
    Shapes = ["pyramid", "cube", "sphere", "cylinder", "cone"]

    #run check health to show user health inside of the function
    CheckHealth(health, play_again)
    print("You make your way past the goblins and find a larger room with a weird looking wall. ")
    print("This room is filled with many shapes, but only one large hole in wall.")
    print("The shape look to have six sides which all have equal lengths...")
    print("Seems you need to find a matching piece to open the door. Here are the shapes you can choose...")
    #Lets use a for loop to loop the shapes to write less code! each_shape is used as the iterator
    for each_shape in Shapes:
        print(each_shape)
    user_choice = input("Please enter a shape to use to match the hole. (Use Lowercase Letters) ")

    if user_choice == "square":
        print("You find a square shaped stone and drag it over to the door. Eventually finding the strength to pick up this large stone, you fit it into the door.")
        print("You hear a loud thud as the door begins to swing open...")
        
    if user_choice == "cube":
        print("You find a cube shaped stone and drag it over to the door. Eventually finding the strength to pick up this large stone, you fit it into the door.")
        print("You hear a large thud as the door swings open...")
    else:
        print("You begin to look for a shape that fits, but no matter how many times you try and use your selected piece the door will not open.")
        print("You hear a loud thud as the door swings open...")
        print("You begin to walk through and toxic fumes make their way into your mouth and eyes.")
        print("You will need some time to recover before moving on.")
        health = health - 25
    return health
    
def DragonFight(health):
    CheckHealth(health, play_again)
    print("You have become frustrated walking through this dungeon of torrment and just want to find the dragon...")
    print("You think to yourself...")
    print(" ' I really wish the dragon would just show up in front of me. ' ")
    print("...")
    print("...")
    print("You stop moving...")
    print("You begin to shake your head... 'I didnt mean this soon'")
    print("As you say that outloud the dragon flies down and a ball of fire begins to emerge from its mouth.")
    print("You are prepared and roll out of the tunnel and into the dragons den.")
    print("You see the intense flame shoot past you and even though it missed the heat sears your arm.")
    print("Looking around you see the dragons wounds from previous attempts from other adventurers.")
    print("One spot you notice more than the rest, on its neck the scaling ends as a giant would made by a large weapon left a scar in the dragon.")
    print("But right next to the dragon you see a scroll lying on the ground, you can feel magic eminating from it.")
    print("You see the dragon ready its next move, but just before you act you notice one last thing, a wooden shield lying on the floor right next to you.")
    print("What skill would you like to use against the dragon?")
    # lets create a list for the users skills
    Player_skills = [" a: Sword Style", "b: Fireball", "c: Shield Slam", "d: Run Away"]
    #print the list like this.
    print(Player_skills)
    user_choice = input("Please enter 'a' 'b' 'c' or 'd'")
    if user_choice == "a":
        print("You block a few talon strikes and eventually see the dragon's mouth glow red. You choose to charge into dragon and hide below it.")
        print("The fire rushes past you and the dragons neck is in your reach...")
        print("You jump up with the boost of your sword and swing it at the wound in its neck.")
        print("The dragon screams and falls to the ground! The dragon is not dead, but is not moving.")
        print("You speak up and say 'I will not kill you dragon, we only need you gone. Give me one of you scales and in exchange I will let you leave this place.' ")
        print("The dragon closes its eyes in agreement, you cleave off one scale and begin to walk back to the adventurers guild.")
    elif user_choice == "b":
        print("After blocking a few strikes from the dragon you see an opening, you run up and grab the scroll and with your limited knowledge attempt to read the scroll.")
        print("Your first attempt is interupted from the dragons roar, but you try again and perfectly cast the powerful magic.")
        print("...")
        print("...")
        print("Nothing seem to be happening.")
        print("Until you see a vortex of fire engulf the room and the force pushes you to the ground as the fire condenses and launches at the large dragon.")
        print("The dragon falls in defeat, its body unable to move.")
        print("You cut a tooth from the dragon's mouth as proof and you leave the cave victorious.")
    elif user_choice == "c":
        print("You grab the wooden shield and the dragon begins to charge its fire breath.")
        print("You ready your shield and prepare for the fire.")
        print("Time slows and its in that moment you realize... The wooden shield was not going to cut it.")
        print("You try to roll out of the way, but you take the brunt of the heat.")
        #minus 50 this time to round out 100 if all bad choices
        health = health - 50
        print("The dragons breath leaves you writhing in pain.")
        CheckHealth(health, play_again)
        print("After the initial shock you realize you cannot lose here! You look around and find the scroll lying on the ground and recite the words.")
        print("You see a vortex of light engulf the room and a force pushes you to the ground as the light condenses and slices the space all around the room.")
        print("The dragon falls in defeat, its body unable to move.")
        print("You cut a tooth from the dragon's mouth as proof and you leave the cave victorious.")
    else:
        print("You turn your tail and run away!")
        print("As you begin to run away, the dragon flies above you and while you try and turn your head to dodge your knocked into the wall of the room.")
        print("The impact leaves you incapable of moving anymore and the dragon looks at you and puts you into a deep slumber, never to wake up.")
        CheckHealth(health, play_again)

    return health
#This function will run if you successfully complete the game
def Outro(player_name, play_again):
    print("You walk out of the cave and see the sun light once again.")
    print("You know what they will call you when you get back.")
    print( player_name + " The Dragon Slayer!")
    print("Thank you so much for playing my game!")
    user_input = input("Would you like to play again? 'y' or 'n'")
    # take user input to see if the player will play again
    if user_input == "n":
        play_again = False


def main():
# use global tag to make the variable global to the other functions
    global is_alive
    global health
    #set play_again to true to make sure the functions will run
    play_again = True
    # while loop allows for the code to re run if the user says yes to the replay question
    while play_again == True:
        #Functions
        DisplayTitle()
        #Must set the returned value to a variable
        player_name = GetPlayerName()
        Introduction(player_name)
        health = GoblinAttack(health)
        health = PlayerPuzzle(health)
        health = DragonFight(health)
        Outro(player_name, play_again)
# Checks to see if there is a main function, and if there is play the function first.
if __name__ == "__main__":
    main()