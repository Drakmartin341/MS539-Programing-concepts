# ZDF: Zombie Defense Force - Mysthaven
# Player variables (shared throughout the game)
health = 100
food = 20
water = 50
time = 800  # 8:00 AM, stored as HHMM
day = 0
infection = 0
weapon = "Tire Iron"
#inventory = [weapon]

# FUNCTIONS #
def wip():
    print("\nThis is the end of the current simulation. More content will be added in the future.\n")
    input("\nPress Enter to END the Simulation...Thanks for playing.")

def display_stats(health, food, water, day, time, infection, weapon): # this displays player stats
    #Display the player's status without changing any values.
    print("_" * 150)
    print("Current Stats\n")
    print(f"Health: {health}/100")
    if health < 20:
        print("You are critically injured.")
    elif health < 50:
        print("You are injured.")
    elif health < 80:
        print("You are feeling good.")
    print(f"Food: {food}/100")
    if food == 0:
        print("You are starving and will lose health until you eat.")
        health -= 5
    elif food < 10:
        print("You are very hungry.")
    elif food < 30:
        print("You are hungry.")
    elif food < 50:
        print("Your stomach is growling.")
    print(f"Water: {water}/100")
    if water == 0:
        print("You are severely dehydrated and will lose health until you drink.")
    elif water < 20:
        print("You are very thirsty and should find water.")
    elif water < 50:
        print("You are thirsty.")
    print(f"Weapon: {weapon}")
    print(f"Day: {day}")
    print(f"Time: {time // 100:02d}:{time % 100:02d}")
    print(f"Infection: {infection}")
    print("")
    print("_" * 150)

def take_action(minutes, food_cost=0, water_cost=0): # this is thE attrition of stats and time 
    #Advance the clock, consume supplies, and apply starvation/dehydration damage.
    global health, food, water, day, time

    # Convert HHMM to minutes before adding elapsed time.
    minutes_since_midnight = (time // 100) * 60 + (time % 100) + minutes
    day += minutes_since_midnight // (24 * 60)
    minutes_since_midnight %= 24 * 60
    time = (minutes_since_midnight // 60) * 100 + minutes_since_midnight % 60

    food = max(0, food - food_cost)
    water = max(0, water - water_cost)

    # Damage happens after an action, not whenever the player views their stats.
    if food == 0:
        health = max(0, health - 5)
    if water == 0:
        health = max(0, health - 10)

def get_choice(prompt, valid_choices): #Accept a numbered response; allow C/I/Q without losing the current choice.
        while True:
            choice = input(prompt).strip().upper()
            if choice == "C":
                print("\nCurrent Stats")
                display_stats(health, food, water, day, time, infection, weapon)
            elif choice == "I":
                #print("\nInventory:", ", ".join(inventory) if inventory else "Empty")
                print("This feature is currently being worked on")
            elif choice == "Q":
                print("\nObjective: Explore Mysthaven, gather supplies, and establish a safe base.")
            elif choice in valid_choices:
                return choice
            else:
                print("Invalid choice. Please select one of:", ", ".join(valid_choices))

def display_title():
    print("=" * 150)
    print("                            Adventure Academy: Zombie Survival")
    print("=" * 150)
    print("\n\n")

def display_introduction(): # Displays the story and allows player to choose where they start the game from
    print("""Five months ago, the world changed forever.....

    A mysterious infection spread across the country, turning ordinary people into mindless zombies. Cities collapsed, governments disappeared, and
    the electrical grid failed. Food became scarce, clean drinking water became valuable, and the few remaining survivors struggled to stay alive.
    
    You have been traveling for months, you are hungry, thristy, and tired when you come across the town of Mysthaven a rural community with homes,
    a couple of farms, a small shopping district, and an industrial/storage hud, on the other side of the river. After months of wandering, Mysthaven
    provides you with something you haven't had for a long time...... Hope.

    If you are to rebuild. You must make difficult decisions about where to explore, how to use resources, and which survivors to trust.
    Will you rebuild Mysthaven into a thriving settlement, or will your community become another forgotten casualty of the apocalypse? 
    
    That is for you to decide. 
    
    Select where you wish to enter the town of Mysthaven.
    1. Main Street from the North
    2. Trucktrail Road from the West
    3. Railroad Tracks from the South
    4. First Avenue from the East
    """)
    print("_" * 100)
    get_choice()

def display_directions():
    print("=" * 150)
    print("                                            HOW TO PLAY")
    print("=" * 150)
    print("""
                    THIS GAME USES DESCRIPTIVE TEXT OF BLOOD, GORE, AND VIOLENCE---- YOU HAVE BEEN WARNED!!!!

        This is a text-based adventure in which you build and maintain a long-term survival base during a zombie apocalypse. 
        You must find shelter, explore Mysthaven for resources, and construct a safe settlement. The goal is to survive using your skills
        and knowledge. Fighting zombies is not the main objective. While there will be encounters with the walking dead and even other
        survivors. The main focus is survival, not finding a cure, or running around bashing every zombie in the head till they stop moving.
        Every encounter with one of the wlaking dead runs the risk of you getting infected. if you get infected you can only slow its course
        not cure it.

        Almost every action takes time, food, and water:

        If your "Food" reaches 0 you will loose health.
        If your "Water" reaches 0 you will also lose health.
        If your "Health" reaches 0 you will die, and your game will restart.
        If your "Infection" reaches 100% you will die and join the walking dead, and your game will restart
    
        You can check your stats, Inventory (currently under delevopment), and any quests (currently under development) at any choice prompt:

        Enter "C" to check character stats
        Enter "I" to see your inventory
        Enter "Q" to check your current objectives
    
        """)


    entrance_choice = get_choice("Enter your choice (1, 2, 3, or 4): ", {"1", "2", "3", "4"})
    if entrance_choice == "1":
        print("""
            You are greeted by a worn wooden sign: 'Welcome to Mysthaven. Where Peace and Home are the same thing.'
            There is a ripped and torn bundle of rags near the sign. The bundle appears to be a satchel or bag.
            The bag has obvious signs of distress and reddish-brown stains on it.
            But it's probably best not to think about what those stains truly are.
            """)
        take_action(minutes=10, food_cost=2, water_cost=4)
           
            
    
            #print("\nYou pick up the bag and carry it with you as you continue toward Mysthaven.")
            #inventory.append("Worn Satchel")
            #take_action(minutes=5, water_cost=1)
            
        # This is Trucktrail Road path
    elif entrance_choice == "2":
        print("""
        The old dirt road was well used, probably by the farmers who owned this land before the dead
        started walking. Brown fields of overgrown crops stretch along both sides. Up ahead, you see
        two figures. You cannot tell whether they are alive, but by the way they hold themselves suggests
        They are not.
    
            1. I approach the wearily
            2. I attack them with my weapon
            3. I go into the fields and avoid them completely
            4. I sneak past them quietly using the crops as cover
            """)
        take_action(minutes=15, food_cost=2, water_cost=4)
        dirt_road_choice = get_choice("Enter your choice (1, 2, 3, or 4): ", {"1", "2", "3", "4"})
    
    
         # Railroad Tracks   
    elif entrance_choice == "3":
        print("""
            You approach Mysthaven from the south, following the railroad tracks. After days of travel
            with little food or water, you stumble and fall, scraping your knee and hand. As you pick
            yourself up, you see a neighborhood about a mile up the tracks to the east.
            """)
        take_action(minutes=5, food_cost=2, water_cost=4)
        health = max(0, health - 2)
    
    elif entrance_choice == "4":
        print("""
        You enter Mysthaven's commercial district. Storefronts line the streets, and about 15 vehicles
        are piled up at the intersection of Main Street and First Avenue. It looks as if a serious
        accident happened during the initial panic.
    
        Several zombies shuffle among the cars, bumping and sliding along the vehicles as they move.
        Others stand in the road as if waiting for something to attract their attention.
        """)
        take_action(minutes=5, food_cost=2, water_cost=4)

def start_sign(): # If players choose to start at the sign
    print("""
    You are greeted by a worn wooden sign: 'Welcome to Mysthaven. Where Peace and Home are the same thing.'
    There is a ripped and torn bundle of rags near the sign. The bundle appears to be a satchel or bag.
    The bag has obvious signs of distress and reddish-brown stains on it. But it's probably best not to
    think about what those stains truly are.
    
    In the distance, maybe a mile or two, you can see farm fields. They have turned brown from neglect but there are
    patches of green still. Further down you can see teh rise of buildings that is Mysthaven proper. Columns of smoke 
    rise up from various places throughout the town. It would appear that you are entering the town down the main road.
    leading into town. 

    What do you do?
    1. Ignore the bag and continue on down the road
    2. Search the bag
    3. Pick up the bag and search it later
       """)
    get_choice("Enter your choice (1, 2, or 3): ", {"1", "2", "3"})

def start_trucktrail(): # if player choice is to start at the Trucktrail Road
    print("""
        The old dirt road was well used, probably by the farmers who owned this land before the dead
        started walking. Brown fields of overgrown crops stretch along both sides. Up ahead, you see
        two figures. You cannot tell whether they are alive, but by the way they hold themselves suggests
        They are not.
        
        What do you do?

        1. I approach the wearily
        2. I attack them with my weapon
        3. I go into the fields and avoid them completely
        4. I sneak past them quietly using the crops as cover  
        """)
    print("_" * 150)

def start_railroad(): # player chooses to start at the railroad tracks
    print("""
        You approach Mysthaven from the south, following the railroad tracks. After days of travel
        with little food or water, you stumble and fall, scraping your knee and hand. As you pick
        yourself up, you see a neighborhood about a mile up the tracks to the east.
        """)
    take_action(minutes=5, food_cost=2, water_cost=4)
    health = max(0, health - 2)

def start_first_ave(): # player chooses to start on 1st Avenue
    print("""You enter Mysthaven's commercial district. Storefronts line the streets, and about 15 vehicles
            are piled up at the intersection of Main Street and First Avenue. It looks as if a serious
            accident happened during the initial panic.
    
            Several zombies shuffle among the cars, bumping and sliding along the vehicles as they move.
            Others stand in the road as if waiting for something to attract their attention.
            """)

    
# GAME CODE STARTS HERE
#Start with intro, title, directions
display_title()
display_directions()
input("\nPress Enter to Continue...")
display_introduction()

entrance_choice = get_choice("Enter your choice (1, 2, 3, or 4): ", {"1", "2", "3", "4"})
if entrance_choice == "1":
    start_sign()
elif entrance_choice == "2":
    start_trucktrail()
elif entrance_choice == "3":
    start_railroad()
elif entrance_choice == "4":
    start_first_ave()

    wip()