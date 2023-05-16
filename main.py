print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_decision = input("You come to a cross-road with signs, the left sign points to a wizard's castle at the top of a mountain, the right sign points to a narrow path leading to the gloomy path down the valleys. Which path do you choose? type 'left' or 'right'. ")
first_left = input ("You have chosen to approach the wizard's castle. As you climb the mountain, the sun begins to fall faster. You might not make it to the castle before sundown. Sundown is when the evil lurks from the shadows... You spot a shack off the path. Do you: chance the safety of the shack, or brave toward the castle? type 'shack' or 'castle'. ")
first_right = input("You approach the gloomy valleys at the bottom of the mountain. You journey on through the thick fog and find yourself at the entrance of a beautiful town. Your eyes wander and lock onto the 'STAY INSIDE' painted across numerous buildings. Do you: dart for safety into the closest building, or explore a little further through the town? type 'safety' or 'explore'. ")
shack = print("You have chosen to risk the safety of the shack. Bad idea, this is where the witches lay. Through the front door is complete darkness. One step forward and... Oh no! You fall 3 foot down into a cauldron. Sizzle and Boil!. Game Over.")
castle = input("You brave the night and make your way further up the mountain to the wizard's castle. You have been hiking the heights for 20 minutes when you begin to hear a rumbling sound from the bushes. Do you: pick up a stick to fight off whatever's lurking in the bushes, or run for your life? type 'fight' or 'run'. ")
safety = print("You chose to dart for safety. Although, running for safety is quite the opposite of what you did. Upon opening the rustic, loud-creaking door, you just woke up a den of 20 vampires. Let's just say, the garlic bread you packed didn't quite have enough garlic on it... Game Over. ")
explore = input("You chose to explore. As you carefully make your way through the town, you find a futuristic device laying on the ground. Looks like a portal gun. Do you: leave it on the ground, or put it in your backpack? type 'ignore' or 'backpack'. ")
fight = input("You chose to pick up a stick and fight. More rumbling ensues, you slowly back away slowly. SUDDENLY! Something jumps out of the bushes! It's a dog. The dog approaches you and gestures to throw the stick. Looks like a good boy. Do you: throw the stick, or toepunt the fuck outta the dog and leg it? type 'throw' or 'toepunt'. ")
run = print("You chose to run. You trip and fall on a rock. You dead. Game Over.")
ignore = input("You chose to leave the device on the ground. As you make your way through the town, your eyes dart from area to area. Your attention is drawn to the window of a dark mansion at the very end of town. A woman peering at you through the window. Do you: Wave at her, maybe she's friendly, or run for cover? type 'wave' or 'cover'. ")
backpack = print("You chose to put the device in your backpack. Turns out you were on a hidden camera show and you just got busted for stealing. Chris Hansen and a camera crew appear from behind one of the buildings, with 20 cops surrounding you. Don't steal. You get arrested. Game Over.")
throw_stick = input("You chose to throw the stick. The dog is a good boy and brings it back to you, you have gained a new friend for your journey. You reach the top of the mountain. You stand before two great doors. You knock and hear a voice. 'A sacrifice is required before entering the gates of paradise' - Do you: sacrifice the dog, or sacrifice your left arm? type 'dog' or 'arm'. ")
toepunt = print("You chose to toepunt the fuck outta the dog and leg it. Why would you choose to toepunt a dog when I just told you he looks like a good boy? Animal abuse ain't cool man. You failed the game. Check yourself. ")
wave = print("You chose to wave at the peering lady in the window of the dark mansion. She comes down to the front door and welcomes you into her home. She's a lovely lady and makes you a bowl of soup. 7 years later, you're married with 8 children. You refurbish the town and open for business. You are now the town's mayor. Mayor of Riverdale. Congratulations, you won the game.")
cover = print("You chose to run for cover. Bro, what are you doing? You can't expect to get rid of your anxiety with women if you keep running away from them. Things could have been different if you just waved at her. You ran for cover and fell into wet mud, turns out it's quicksand. Now look. You're sinking in quicksand all because you wanted to duck from a female again. Do better bro. Game Over. ")
dog = print("You chose to sacrifice the dog. You look down at the dog and go to approach it. The forces of the game prevent you from reaching the dog and throw you off the top of the mountain. Unlucky mate. Game Over. ")
arm = print("You choose to sacrifice your left arm. You exclaim to the voices you choose to sacrifice your arm. The dog then magically morphs into Chris Hansen as a wizard. You are on a magical camera show and a camera crew emerge from behind the gates to paradise. It was all just a funnny little camera show. Congratulations, you were granted access through the gates of paradise.")

if first_decision == 'left':
  print(first_left)
  if first_left == 'shack':
    print(shack)
  elif first_left == 'castle':
    print(castle)
    if castle == 'fight':
      print(fight)
      if fight == 'throw':
        print(throw_stick)
        if throw_stick == 'dog':
          print(dog)
        elif throw_stick == 'arm':
          print(arm)
      elif fight == 'toepunt':
        print(toepunt)
    elif castle == 'run':
      print(run)
elif first_decision == 'right':
  print(first_right)
  if first_right == 'safety':
    print(safety)
  elif first_right == 'explore':
    print(explore)
    if explore == 'ignore':
      print(ignore)
      if ignore == 'wave':
        print(wave)
      elif ignore == 'cover':
        print(cover)
    elif explore == 'backpack':
      print(backpack)
else:
  print("incorrect input bruv run again.")