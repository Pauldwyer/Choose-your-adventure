# This file is for long storie sections
# Moved stories here to declutter run.py

import sys
from time import sleep


def typewriter(text):
    """
    Function for slow typing in terminal window
    Loops through text and inputs by char with delay
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()


def start_game_function():
    """
    Start game
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter("""
    Your running through the woods
    Your feet are hurt from running so hard
    Why are you running?
    You cant quite remember

    The soles of your feet are screaming
    You cant keep going

    You come to a clearing in the woods
    You stop for a second to catch your breath

    Everything suddenly becomes more quite
    You take in your surroundings

    It looks like you have 2 paths
    Go left or go right
    """)


def bad_ending_function(username):
    """
    Bad ending function.
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter(f"""
    This is the bad ending, which means you died.

    Tough luck {username}

    Maybe rethink your choices and play again?

    If you dare.
    """)


def falling_asleep_function(username):
    """
    Falling asleep function
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter(f"""
    'Dont hurt her' you shout
    'Get back or else' you yell at the stranger
    The stranger slowly steps towards you
    He has a blade in one hand and a blackjack in the other
    You turn to Emily and say 'Everything will be ok baby'
    You turn again back to the stranger, he is edging closer slowly
    'What do you want' you scream
    'You must pay for your transgressions' says the stranger in a lowly growl
    You quickly grab the clock off the fireplace and you charge the stranger
    You swing with all your strength aiming for his head
    But he is too fast, he side steps your attemp
    and cracks you across the head with the blackjack
    You pass out

    You awake and find a bloody blade in your hand
    You throw it across the floor, your hand is covered in blood
    You look up and scan the room, you see Emily on the floor
    She is covered in blood
    The door opens and Emilys father walks in
    'What in the seven hells have you done' he shouts

    *Crack*

    You awake with a splitting headache, you are back in the forest clearing
    Your tied up against the tree
    5 men looking down on you
    You recognise Emilys father Pierre
    'You thought you could runaway' he says
    'Now you will die for what you did to my daughter'
    'Do you have any last words {username} ?'
    As you open your mouth to protest Pierre slashes our throat
    You bleed to death tied to the tree
    """)


def sea_scenario_function(username):
    """
    Sea Scenario function
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter(f"""
    You take off running in the left direction.
    You forget the pain in your feet.

    The hair starts to stand on the back of your neck.
    Oh {username} what have you done?
    You have a feeling you are being chased.
    Why are you running?
    What did you do?
    Why were those people so angry??
    You start to remember a little about the chase.

    '{username} you murderer get back here and face justice'

    Suddenly you are back in the current moment.
    The trees start to become less dense.
    You star to smell salt water.
    You can hear waves crashing in the distance.
    You start to run faster.
    But your feet are screaming at you.


    Finally you come out of the woods into a little hidden beach.
    You start to hear a voice singing, it sounds like a angel.
    You dont understand the words or language.
    But the sound makes you want to get closer to it.
    You can scan the beach.
    You see somebody on the rocks at the far end.
    That has to be a lady singing.
    """)


def forest_scene_function(username):
    """
    Going into the forest function
    Called from the forest clearing
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter(f"""
    You decide to go deeper into the woods.
    You need to find somewhere to rest.

    You walk deeper and deeper into the woods.
    The only sound you hear is twigs and branches crushing under your feet.

    How did you get into this situation.
    You cant remember what happened 5 hours ago.
    Oh {username} what have you gotten yourself into this time.

    But you start to remember some things.
    You start to get lost in your thoughts.

    You remember jumping out the window.
    You remember Pierre shouting murderer at you.
    Who did you kill??
    And why was your wives father calling you murderer??
    Why did Pierre and his 4 brothers chase you out of the village??

    You snap back into reality.
    You have never been this deep into the woods.
    Surely you are near the foot of the Everlook mountain.
    You are actually and whats that ahead?
    Is that a cave in the foot of the mountain?
    Do you hide in the cave or keep going through the woods?
    """)


def on_the_rocks_function(username):
    """
    On the rocks
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter(f"""
    You set out crossing the beach.
    The smell of the salt water filles your nose.
    The wind blows sand up into your face.
    You look out across the sea.
    Is there a way here to escape this nightmare?

    You get closer to the rocks.
    The song the person is singing is hypnotizing.
    You have no idea what language.
    But it is the sweetest song you have ever heard.

    You get closer to the person and realise it is a woman.
    She has her back to you.
    She dosent hear you approach, atleast dosent show it.

    The singing gets louder.
    You now feel compelled to walk towards her.

    '{username} come closer'
    You now feel compelled to walk towards her.
    As if your brain is not controlling your body.

    Something else is controlling your body.
    Your legs walk with a mind of there own.

    All you can think about is the voice singing the song.

    You are now around 3 metres away from the woman.
    Golden blonde hair dangles down her back.
    In a pale white dress.
    Sleek slender shoulders.
    Is this an angel from heaven?

    She turns and glances over her shoulder at you.
    You can only see her green eyes, shoulder hiding her face.
    She turns to face you.


    You can still hear the singing in your ears.
    But her mouth isnt moving!
    You are fozen in time, you cant move!


    Your eyes look to her hands, they are claws!
    She laughs and you see her mouth is full of fangs!
    She disappears into a puff of smoke.
    The song is ringing in your ears.

    You feel her presence behind you.
    'Just in time' she whispers in your ear.
    'I was starting to get hungry'
    She sinks her fangs into your neck.
    """)


def cave_scenario_function(username):
    """
    Into the cave we go
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter(f"""
    You decide to head towards the cave.

    As you approach the cave face you feel a cold air blow out.

    The entrance to the cave is big and the ground leading in is will trodden.
    This isnt some random cave, this is well used.
    You kneel down and feel the dirt.
    Looking for foot prints.
    But you only feel flat earth.

    You start to remember your previous life as a ranger.
    Before you settled down in the village.
    Before you met Emily.
    You did some horrible things in your time.
    Before you took an arrow to the knee.

    You stop at the entrance, almost second guessing your decision.
    Come on {username} lets go you whisper to yourself.

    You continue inside
    The entrance is quite big, as if its made for men twice your size
    The large entrance makes it quite bright when you walk in
    You follow the path in cave as far as it will take you
    It snakes and turns but you keep following it
    The light is all but gone and you can barely see 2 ft in front of yourself
    You keep walking
    Its eirily quite... until *whoosh* bats fly past you
    You feel like you have been walking in this cave for an hour
    You have almost lost all sight until you make out light ahead
    It looks like a fire is giving off light around a turn ahead
    """)


def deeper_into_cave_function(username):
    """
    Into the dark depths we go
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter(f"""
    You go around the corner and suddenly you are amazed
    You walk into this huge cavern
    There is a fire in the middle, surrounded by benches
    You count 5 beds a one end of the cavern
    You see a huge golden leather bound chest at one end
    The light from the fire makes the chest shine
    You can see the flames dancing on the reflection off the gold

    You approach the fire when suddenly the air infront of you contorts
    A man materialises in front of you!

    An old man, hunched over leaning on a staff
    Hes wrapped in a cloak with a hood over his head

    'Ah {username} i wondered if you would make it here'
    You are shocked, what the hell is going on here you wonder 

    'Ah dont worry {username} all will be clear soon' says the man
    Hes reading your mind?! Who the hell is this guy
    You start to take 2 steps back preparing to run
    Suddenly the pain in your feet returns with a vengence

    'I am Damon, and please dont run. Sit down your feet will thank you'
    Damon you think... Damon !! the legendary mage?!

    The Damon who stopped the orc invasion from the southlands?
    Legen has it Damon the mage stopped the invasion of 100k orcs 
    And turned the tide of the war of the long night

    'Yes yes that was me but it wasnt quite 100k more like 10k'
    You feel compelled to sit down
    'Good those poor feet of yours, i dread to think of the blisters you will have'

    'Your time is limited so lets get to it'
    'You may have heard i am a very powerful mage'
    'I know of your a little confused, you cant quite remember why you are being pursued'

    You keenly listen to the man, taking it all in
    'A ghost from your ranger past caught up with you and attacked you in your house'
    'All your memories will be back in time dont worry'
    'This ghost killed your beloved wife Emily'
    'Her father walked in on you with the murder weapon in your hand'
    'You ofcourse were knocked out, the ghost hit you over the head with a blackjack'#
    'The Pierre the father in law threw you out the window'
    'All of that head trauma made you lose your memory'
    'Dont worry it will come back in time'

    You hear dogs barking echoing in the cave

    'I offer you a way to escape'
    'That is Pierre and his goods with dogs, they got your scent'

    'I will teleport you somewhere but you must choose quickly'
    'I will give you 3 choices'


    'What will it be? And yes you will travel through time before you ask'
    'But you wont remember meeting me, or will you??'
    """)


def deeper_into_forest_function(username):
    """
    deeper deeper
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter(f"""
    You avoid the spooky looking cave.
    You set off, feeling the pain in your feet again.
    You are exhausted.
    You find a big fallen branch and decide to fashion a walking stick
    from the branch.
    You start to venture deeper into the forest.

    You start to remember about your ranger past.
    Many a time you would march through woods.
    Similar to these woods but not these woods.
    You are a stranger to these lands.
    You left your previous life behind you.
    Settled down in this village and started a new life.
    The village has a funny name, they call it 'Duncannon'.
    These woods are called The Far Woods.

    Oh how long this new life lasted.
    One cant escape ghosts of ones past he would say.
    Oh Vesemir you think, how you wish you could
    ask your old master for advice right now.
    His wisdom knew no bounds.
    He thought you all you knew about the ranger life.

    'I can remember now' you say to yourself.
    You stop for a moment to focus your mind.
    You came to the village 2 years ago, to escape..
    To escape... to escape the Bloody Baron !
    The Bloody Baron of Fethard on Sea.
    The local vagabond who roused a group of sell swords to
    his cause and captured the Fethard Barony in a bloody war.

    You came to this village to hide.
    You crossed the bloody baron and had to lay low.
    {username} what did you do?

    *Arf arf arf arf"
    3 dogs burst out of nowhere and are running at you full pelt!
    What do you do??
    Fight the dogs with your walking stick?
    Or run?
    """)


def stand_and_fight_function(username):
    """
    deeper deeper
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter(f"""
    You stand your ground.
    You plant your feet, slight bend of the knees
    Twist your upperbody and hold your stick like a bat.
    These movements came naturally to you and were done
    in seconds.
    The first dog leaps at you
    *CRACK*
    You hit the first dog so hard he flies across the wood.
    He lies in a heap at the bottom of tree.
    The 2nd dog comes running at you.
    *CRACK*
    Another one bites the dust.
    The 3rd dog stands his ground looking at you.
    You meet his stare dead on.
    The dog is snarling at you, saliva dripping from its mouth.
    No move from the other 2 dogs you hit.
    '{username}' you hear someone shout

    '{username} if you touch that dog it will be the last thing you do !'

    You see 3 figures come out from behind the trees.
    Pierre, Emilys father.
    '{username} are you ready to face justice for killing my daughter?'
    'I didnt kill emily, I was framed!!' you protest.

    'Enough of this yibber yabber' snarls Pierre 'Get him Bobby !'
    Suddenly there is a flash of light.
    You feel like your blinded.
    You rub your eyes and look around.
    Things start coming into focus again.

    There is a man in a robe with a hood over his head.
    He is leaning on a staff.

    He looks at you and says 'It is not your time to die {username}'
    'I will open you a portal'
    'Go through the portal and find somewhere to rest'
    'The portal will bring you to Fethard'
    'The bloody baron found you and had your wife Emily killed'
    'I will help you get your revenge'

    Then the old man starts to speak a strange language and waves his staff.
    A portal opens.
    'Go quickly now'

    Do you go into the portal or run away??
    """)


def run_from_dogs_function():
    """
    deeper deeper
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter("""
    You start to run as hard as you can
    The 3 dogs are closing in on you
    You trip and fall
    The dogs pounce on you biting you all over
    Biting and tearing lumps out of you
    You hear someone call the dogs off
    You cant move
    You open your eyes and you see Pierres face
    'Say hello to my little friend' He shows you a knife
    And with that knife slashes your throat
    """)


def run_from_portal_function():
    """
    deeper deeper
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter("""
    You turn to run
    'Ugh why are you such a dissapointment' the mage said.
    The mage waves his staff and you collapse on the floor paralysed.
    'Pierre you can have him' the mage says.
    And with that he disappears in a flash.
    'Get him boys, we will bring him back to the village
    and flay him for all to see.'
    """)


def into_the_portal_function():
    """
    asdfd
    """
    print("""
    --------------------------------------------------------------
    """)
    typewriter("""
    You step towards the portal.
    Pierre screams 'No i wont stand for this !!!'

    The mage whispers some words and points his staff at Pierre
    In a flash Pierre turns into a smoking pile of ash
    'He wont be missed' the mage says.
    Pierres goons turn and run.

    You pause for a second turn to the mage and say
    'Who are you??'
    'I am Damon. The guardian of this realm. Now go on
    I will meet you on the otherside, there will be a house
    go inside and rest, i will come along soon'

    And with that you step through the portal.
    
    You are in the middle of a road and you see a small
    house on the side of the road.

    You start to hear a voice of a woman singing.
    You look around to see who it is.

    You notice a woman sitting on the wall outside the house.
    Golden blonde hair hanging down her back.

    Intrigued by the song you start to walk towards her.
    """)
    print("""
    --------------------------------------------------------------
    """)
    typewriter("""
    Congratulations!!!

    You have made it to the end of the story

    This is the 'happy' ending

    Hope you had fun!s
    """)


    
