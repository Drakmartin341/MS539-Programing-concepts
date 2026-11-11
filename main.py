#Global code goes here remember that if you change something here it will effect the enitire code where the instances occur


health = 100
food = 20
water = 50
time = 800
day = 0
infection = 0
weapon = "tire Iron"


def display_statistics(health, food, water, day, time, infection, weapon):
    print(f"Health: {health}/100")
    # If stat drops below 20, print a warning message
    if health <20:
        print("You are critically injured")
    elif health < 50:
        print("You are bleeding")
    elif health > 50:
        print("You are feeling good")

    print(f"Food: {food}/100")
    if food == 0:
        print("You are starving and will lose health till you eat")
        health -= 5
    elif food < 10:
        print("You are very Hungry")
    elif food < 30:
        print("You are hungry")
    elif food < 50:
        print("your stomach if growling")

    print(f"Water: {water}/100")
    if water == 0:
        print("You are severly dehydrated and will lose health if you do not drink")
        health -= 10
    elif water < 20:
        print("You are very thirsty and shoudl find water")
    elif water < 50:
        print("You are thirsty")

    print(f"Weapon: {weapon}")
    print(f"Day: {day}")
    print(f"Time: {time}")
    print(f"Infection: {infection}")


# create an adventure sim
# First let's display the title
print("=====================================================================================================")
print("                              ZDF: Zombie Defense Force                                ")
print("=====================================================================================================")

# let's print the introduction

print("Five months ago, the world changed forever.\n")
print("A mysterious infection spread across the country, turning ordinary people into mindless") 
print("zombies. Cities collapsed, governments disappeared, and the electrical grid failed. Food")
print("became scarce, clean drinking water became valuable, and the few remaining survivors") 
print("struggled to stay alive.\n\n")
print("After weeks of searching, you discover the town of Mysthaven, a once-thriving")
print("community with homes, stores, farms, a clinic, and an industrial district.")
print("Most of the town has been abandoned. Zombies wander the streets, supplies are limited,")
print("and many buildings are falling apart.\n")
print("Mysthaven ofers you and the weary group of survivors something that you haven't had in months\n\n")
print("A chance to rebuild.\n\n")
input("\nPress Enter to Continue...") # This allows player to input a keystroke
print("_" * 100) # creates a seperation for readability

print("====================================================================================================\n")
print("                                  How to Play                                                       \n")
print("====================================================================================================\n")

#Using the ("""   """) allows a multi-line text format
print("""
This is a text based adventure that allows you to build and maintain a long term survival base during a zombie apocalypse
you will need to find shelter, explore the town of Mysthaven for resources, and build a long-term shelter.

The goal of the game is to see how long you can survive using your skills and knowledge. remember that fighting the zombies
is not the actual goal of the game.... But to survive.

Each action you do will take time. there are 24 hours in a day but 6 will be needed for sleep. if you do not sleep
and the timer reaches the 18 hour mark you will automatically go to sleep and unless you are in a safe area,
you run the risk of being attacked by either random zombies or raiders

If wish to check the status of your character press the "c" key
for Inventory press "i"
For Objectives and Quests press "q"
""")

print("_" * 100)
print("Current Stats")
display_statistics(health, food, water, day, time, infection, weapon)

print("_" * 100)    

input("\nPress Enter to Continue...") # input() This allows player to input a keystroke
print("_" * 100)
print("""
Select where you wish to enter the town of Mysthaven.
1. Main Street from the North
2. Trucktrail Road from the West
3. Railroad Tracks from the South
4. First Avenue from the East
""")

print("_" * 100)
print("")

#This will take a user choice and store it in a variable called user_choice
user_choice = input("Enter your choice (1, 2, 3, or 4): ").strip().upper()

# Now to evaluate the user's choice and update the player stats

if user_choice == "1":
    print("""
    You are greeted by a worn wooden sigh 'Welome to Mysthaven. Where Peace and Home are the same thing'
    There is a ripped and torn bundle of rags near the sign. The bundle apears to be a satchel or bag of sometype.
    the bag has obvious signs of distress and there apears to be some kind of redish-brown stains on it.
    But, it's probably best not to think about what those stain truly are.\n\n""")
    #print("What do you do?\n")

    #print("""
    #1. Continue on down the road and leave the bag behind
    #2. Search the bag
    #3. Take the bag with you and keep moving
    #""")
    time += 10 # This will add time to time of day variable in global code
    food -= 2
    water -= 4

elif user_choice == "2":
    print("""
    The old dirt road was well used, probably by the farmers that owned this land before the dead started walking.
    There are brown fields of overgrown crops on both sides of the road and on the road ahead you can see two figures.
    From this distance you cannot tell if the are alive or just walking corpses. But the way they hold themselves like
    it's the later rather than the former.   \n\n""")
    time += 15
    food -= 2
    water -= 4

elif user_choice == "3":
    print("""
    You approach the town of Mysthaven form the South following the railroad tracks. After days of traveling and with
     little food and water you stumble and fall hard scraping your knee and hand in the process. After picking yourself
      up and dusting yourself off. you can see a neighborhood about a mile up the tracks and to the East.\n\n """)
    time += 5
    health -= 2
    food -= 2
    water -= 4

elif user_choice == "4":
    print("""
    You enter the town of Mysthaven's commercial district. There are several storefronts along the streets as well as a mass
    of 15 vehicles. it apears that during the initial panic an accident occured at the intersection of Main Street and
    1st Avenue, the road you are currently on, there are several grizzly reminders of the chaos and carnage that occured in
    those first moments when the dead began to eat the living.

    You can see several of the walking dead shuffling among the cars, some bumping into the vehciles or sliding along them
    as they move. There are also several just standing in the road waiting for some type of stimulus. 
     \n\n""")
    time += 5
    food -= 2
    water -= 4

else:
    print("invalid choice, please choose 1, 2, 3, or 4")

display_statistics(health, food, water, day, time, infection, weapon)






# Print code above this line so that this lower code displays always. remove when game is complete
print("_" * 100)
print("\n\nThis is the end of the current simulation. more content will be added in the future.\n\n")
# The user will have to press end to continue the sim
input("\nPress Enter to END the Simulation...Thanks for playing.")