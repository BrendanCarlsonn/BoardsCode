from chatterbot import ChatBot
print("Importing Libraries...")
#Create the chatbot's name!
chatbot = ChatBot('AVI-G')
#add packages to train the chatbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#Now lets create the personalities for the chatbot!
#I am going to create a major personality as well as 1 or 2 minor ones.
#For now I am going to focus on making the bot tell you what certain phrases in gaming mean.

personality_Gaming = [
    "F2P",
    "Free To Play; You can access basics of the game for free.",
    "FGC",
    "Fighting Game Community",
    "FPS",
    "First Person Shooter; a major genre in gaming.",
    "MMO",
    "Massively Multiplayer Online Game; A large scale game involving many players.",
    "RPG",
    "Role Playing Game; A game where players have seperate roles.",
    "RTS",
    "Real Time Strategy; Strategy games where the player deals with enemies in real time.",
    "SIM",
    "A Simulation Game.",
    "TBS",
    "Turn-Based Strategy; Strategy games where the player deals with enemies on a turn based time.",
    "TD",
    "Tower Defense; A game where you focus on protecting yourself via different placeable actors",
    "AoE",
    "Area of Effect; an ability that hits many actors.",
    "Actor",
    "An object within a game. Can be an NPC, a playable character, or even an inanimate object.",
    "CC",
    "Crowd Control; abilities that cause an actor to lose accessability to their character, such as slowing their movement.",
    "MS",
    "Movement Speed.",
    "FF",
    "Forfeit",
    "IGN",
    "In Game Name; The name the user goes by on certain online media.",
    "DOT",
    "Damage Over Time; an ability casted on an actor that deals portions of the damage over a certain amount of time.",
    "MP",
    "Mana Points; A resource for classes.",
    "HP",
    "Health Points; A resource for all actors",
    "FOV",
    "Field of View; the vision radius of the player.",
    "LAN",
    "Local Area Network; a connection established locally.",
    "LOS",
    "Line of Sight; often used to represent one individual players FOV of another actor",
    "HUD",
    "Heads-Up-Display; the interface of a game.",
    "Interface",
    "Often explained as the menu system used by a game or applications.",
    "Mod",
    "A modifiction of a game from a third party. These are add ons that the original creator did not make themselves.",
    "Gatcha",
    "A style of game focused on gathering heroes via a random table of possibilities.",
    "QTE",
    "Quick Time Event; an event in a game where the player must press a button before time runs out.",
    "Ganking",
    "Often used to describe an event where multiple players or actors attack one player or actor.",
    "Lvl",
    "Level; used to describe the stage a character is at.",
    "NPC",
    "Non-Playable Character.",
    "PC",
    "Player Character.",
    "PvP",
    "Player versus Player.",
    "PvE",
    "Player versus Environment.",
    "XP",
    "Experience Points.",
    "MOB",
    "Used to descripe actors representing monsters.",
    "FTW",
    "For the Win.",
    "GG",
    "Good Game.",
    "LFG",
    "Looking for Group.",
    "BG",
    "Bad Game.",
    "DC",
    "Disconnect.",
    "INT",
    "To intentionally lose.",
    "OMW",
    "On My Way",
    "AFK",
    "Away from Keyboard.",
    "123",
    "A request to be teleported by another player.",
    "QQ",
    "Symbolic or crying",
    "WTS",
    "Want to Sell",
    "WTB",
    "Want to Buy",
    "TL;DR",
    "Too Long, Didn't Read",
    "Aggro",
    "A resource for monsters that decides what they will target with attacks.",
    "DPS",
    "Damage per Second",
    "Tank",
    "A player who focuses on defensive capability.",
    "Stats",
    "Various aspects of a character ability.",
    "Healer",
    "A player who focuses on their ability to heal.",
    "RP",
    "Role-Playing",
    "TCG",
    "Trading Card Game",
    "BIS",
    "Best in Slot; refering to equippable items in game.",
    "Ping",
    "A form of non-verbal communication; A players connection to a server.",
    "Top Deck",
    "A players top card in a deck of cards; Can also refer to a 'necessary' card in a situation.",
    "MC",
    "Mind-Control; When an player characters control is taken via an ability.",
    "DLC",
    "Downloadable Content",
    "1-UP",
    "Extra Life",
    "SUS",
    "Refering to suspicious behaviors",
    "Poggers",
    "A slang word refering to an impressive display of skill.",
    "Broken",
    "When a portion of the game is unbalanced and unfair to the player.",
    "Busted",
    "When a portion of the game is unbalanced and unfair to the player.",
    "Combo"
    "When an actor or player strings abilities together.",
    "Troll",
    "When a player or actors does something to ruin an event intentionally.",
    "Noob",
    "A player that is new to the game.",
    "One Trick",
    "Someone who only plays one thing.",
    "Dive",
    "To go into enemy territory to accomplish a goal.",
    "P2W",
    "Pay to win.",
    "Whale",
    "A player who spends an abundance of money to gain an advantage.",
    "WP",
    "Well Played",
    "EZ",
    "Easy",
    "Buff",
    "An effect that empowers a player or actor.",
    "Nerf",
    "The changing of certain aspects of a game that weaken that aspect.",
    "CS",
    "Creep Score; refers to the amount of kills a player has on mobs.",
    "MVP",
    "Most Valuable Player",
    "Moly",
    "A molotov; An AoE that harms players that cross over it."
]

personality_Greetings = [
    "Hi how are you!",
    "I am good! I love helping people with the gaming understanding!",
    "How do you work?",
    "All you need to do is enter whatever it is you want to learn about!",
    "Hello",
    "Hi!"
]

personality_Finish = [
    "I am done now.",
    "Okay thanks for listening!",
    "Thanks for your help.",
    "No problem, I hope I was able to help!"
]


#This will train the chatbot with what you made in your persoanlities
trainer_personality_Gaming = ListTrainer(chatbot)
trainer_personality_Greetings = ListTrainer(chatbot)
trainer_personality_Finish = ListTrainer(chatbot)

#Now lets train the chatbot with our personalities
trainer_personality_Gaming.train(personality_Gaming)
trainer_personality_Greetings.train(personality_Greetings)
trainer_personality_Finish.train(personality_Finish)
#Create the trainer
trainer = ChatterBotCorpusTrainer(chatbot)

#Now lets train the chatbot with imported personalities
trainer.train("chatterbot.corpus.english")

#Now lets get input from the user using a loop until they quit
print(" Hello I am AVI-G, here for your gaming understanding needs!\n")
print(" What is it I can answer for you. \n")
print("Please put type what you want to learn about. Ex. MMO")
is_exit = False
while not is_exit:

    user_input = input(" Ready When You Are!")
    if user_input == "quit":
        is_exit = True
    else:
        response = chatbot.get_response(user_input)
        print("\n" + str(response))

