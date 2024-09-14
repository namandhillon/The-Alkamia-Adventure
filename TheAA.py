# Name: Namanpreet Dhillon

# Program Description: The Alkamia Adventure is an adventure game following two explorers, Robin and Lucky, through their journey in the Congo Basin Rainforest. The goal of their adventure is to find a rare species of flower called Alkamia, which can heal animal wounds. Their journey takes an unexpected turn when a mountain gorilla chases them through the forest, leading the two characters away from each other. The explorers must go through a series of games and puzzles in the hopes of reuniting with their friend.

import random # import random package, allows program to generate random numbers 
chpOne = ["ORE", "SEA", "AIR", "FAR", "TIE", "ION"] # stores possible secret words to unlock chapter 2 
chpTwo = ["STAR", "FATE", "FIRE", "EAST", "ROAR", "RAIN"] # stores possible secret words to unlock chapter 3
chpThree = ["SONAR", "STONE", "TEARS", "FROST", "ASTER", "FERIA"] # stores possible secret words to unlock the ending 

print("THE ALKAMIA ADVENTURE") # game introduction/storyline

print("\nDeep in the humid Congo Basin Rainforest, two explorers began an adventure to find an Alkamia flower. A rare species, this flower could heal wounds on any animal imaginable.\nBeing best friends since childhood, Robin and Lucky knew this challenge was perfect for them.")
print("\nRobin was a tall, but soft-faced, ambitious woman who seemed to enjoy teasing Lucky more than she should. Known to be quite bubbly and talkative she was much different than her\ncompanion Lucky.")
print("\nHe was a sad young man who looked at least ten years older than he should’ve, not exactly the type of guy you’d picture when you hear the name Lucky!")

print("\nLucky: Man, it’s hot out here! How the heck are you walking so fast?")
print("Robin: The faster we find that flower, the faster we get out of this place. For someone named after the best cereal brand you aren’t doing much in the ‘luck’ factor right now.")
print("Lucky: What are you? Six years old? Stop rambling and start looking for that flower! I bet we’re getting farther from it if anything.")
print("Robin: Add twenty years to that you mindless monkey. I’m twenty-six, older than you by a year. Respect your elders!")
print("Lucky: You’re so annoying…")

print("\nRobin: Lucky? Did you hear that?")
print("Lucky stops in his tracks and becomes silent")
print("Lucky: It kind of sounds like… footsteps?")

print("\nLucky and Robin look around for any hints as to where the noise is coming from.")

print("\nRobin: LUCKY IT’S A GORILLA, RUN!")

print("\nAn angry mountain gorilla chases the two explorers who run like they never have before. Robin curses loudly over and over again while running way ahead of both the gorilla and \nLucky. Before Lucky can tell her to wait for him he finds himself off the ground and falling into a ditch. Robin, unaware of the situation, continues to run until she hears the \ngorilla’s footsteps fade into the rainforest ambience. She turns hoping to see only Lucky, but to her surprise, neither him nor the gorilla were in sight.")
print("\nLucky and Robin, two explorers who came to the Congo Basin Rainforest for an adventure with their best friend, were now separated and awaiting an unexpected journey to reunite.")

def checkWord (word): # functional method to check user's answers for the secret word 
    global tries # creates global variable for tries, for use outside of method 
    global wordList # creates global variable for list of user answers, for use outside of method 
    if (word == secCode): # if user enters the secret word 
        tries = -1 # breaks loop 
        return "Win" # ends method and return string value "Win" 
    else: # if user does not enter the secret word 
        if (word in wordList): # if user repeats a guess for the secret word 
            print("You have already entered this word. You have", tries, "tries left.") # let user know they have already entered the word, outputs tries left 
        else: # if user does not repeat a guess for the secret word 
            wordList.append(word) # adds guess to word list 
            tries = tries - 1 # user loses one try 
            if (tries == 0): # if user has no tries left 
                print("\nYou were not able to find the secret code!") # let user know they did not get the correct word 
                tries = -1 # breaks loop 
                return "Loss" # ends method and return string value "Loss" 
            elif (tries == 10): # if user has 10 tries left 
                print("That is incorrect.") # let user know they did not enter the correct word 
                print("\nHINT: The second letter of the code is", secCode[1]) # give user a hint with the second letter of the code 
            else: # if user has tries left 
                print("That is incorrect! You have", tries, "tries left.") # let user know they are incorrect and the number of tries left 

randomNum = random.randint(0,5) # generate random number between 0 and 5 
secCode = chpOne[randomNum] # assign secCode to 1 of 6 words in the chapter 1 word list, randomly selected 
chpOnePlay = "Yes" # assign chapter 1 play, allows user to play through game once before asking to play again 

print("----------------------") # begins chapter 1 
print("CHAPTER 1")

while (chpOnePlay == "Yes"): # loops code if user chooses to play though chapter 1 again 
    character = int(input("\nWould you like to play as Robin (1) or Lucky (2)?: ")) # get character user will play as 

    while (character != 1 and character != 2): # loops code while user enters an invalid answer, not 1 or 2 
        print("You have entered an invalid number.") # let user know they have entered an invalid answer 
        character = int(input("\nWould you like to play as Robin (1) or Lucky (2)?: ")) # get character user will play as 

    if (character == 1): # if user chooses to play as Robin 
        print("\nRobin: Okay, I’m sure he’s fine. Lucky can take care of himself... I should still look for him though.") # storyline
        print("Robin begins to walk around the forest for any sign of a ditch. She makes slow movements, trying her best to avoid making noise so as not to attract the attention of the gorilla.")
        print("After a while of walking, she comes across two paths, leading to opposite directions.")

        print("\nRobin: Hmm, to the right is a trail labeled Pathway", secCode[1], "and to the left there's Pathway",secCode[2]) # gives choice of two pathways, includes hints for the secret word 
        pathway = input("Which pathway would you like to follow? (Please enter the letter): ") # get pathway 

        while (pathway != secCode[1] and pathway != secCode[2]): # loops code while user enters an invalid answer, not listed in the question 
            print("\nYou have entered an invalid letter.") # let user know they have entered an invalid answer 
            pathway = input("\nWhich pathway would you like to follow? (Please enter the letter): ") # get pathway 

        while (pathway == secCode[1]): # loops while user chooses to go right 
            print("\nRobin walks to the right, and uncovers… ANOTHER GORILLA! She books it once more, and finds herself back to square one.") # storyline
            print("Again, she comes across the same two pathways, leading to opposite directions.") # lets user know to choose a pathway again 
            pathway = input("\nWhich pathway would you like to follow? (Please enter the letter): ") # get pathway 
            while (pathway != secCode[1] and pathway != secCode[2]): # loops code while user enters an invalid answer, not listed in the question  
                print("\nYou have entered an invalid letter.") # let user know they have entered an invalid answer
                pathway = input("\nWhich pathway would you like to follow? (Please enter the letter): ") # get pathway 

        print("\nRobin walks to the left, leading deeper into the forest.") # continues story if user chooses to go left 

    elif (character == 2): # if user chooses to play as Lucky 
        print("\nLucky: Oww, my whole body hurts… Wait, where am I?! Did I fall into a ditch?!") # storyline
        print("Lucky looks around for a way to escape. With bars on one side of the wall, he realizes he’s in a type of dungeon. The only way out is to get past the bars and into a dark, hallway.")
        print("Lucky: There’s a lock with a three-digit code to unlock the cell, I guess that’s my only way out. But how am I supposed to know this code? Wait, the wall has math equations on it!")
        print("Lucky: Three equations, three digits, this must be it. Math was never my best subject though… I guess teachers were right about math being important later on in life.")

        print("\nEquations: A . 25 - 17 = ?") # output three equations for user to solve 
        print("          ", secCode[0], ". 2 x 4 = ?") # hint for secret word 
        print("           C . 6/2 = ?")

        code = int(input("\nWhat is the code?: ")) # get code 

        while (code != 883): # loops while user does not enter the correct code 
            print("Ugh, it didn’t open, I should try again!") # let user know they are incorrect 
            code = int(input("\nWhat is the code?: ")) # get code 

        print("I got it right, maybe I am a genius! Now to explore the rest of this creepy temple...")  # continues story if user enters the correct code, 883 

    print("\nEND OF CHAPTER 1.") # ends chapter 1 
    print("----------------------")

    ans = input("Do you have the hidden word to unlock Chapter 2? (Yes/No): ") # get ans, asks user if they have the secret word 
    while (ans != "Yes" and ans!= "No"): # loops while user enters an invalid answer, not "Yes" or "No"
        print("You have entered an invalid answer.") # let user know their answer is invalid 
        ans = input("\nDo you have the hidden word to unlock Chapter 2? (Yes/No): ") # get ans 

    if (ans == "Yes"): # if user does have the secret word 
        tries = 15 # user has 15 tries to guess the secret word 
        wordList = [] # stores user answers 
        while (tries >= 0): # loops while user has tries left 
            word = input("\nLook for clues throughout the chapter 1 story! What is the secret word? (Uppercase Letters): ") # get word, asks user to enter their guess 
            result = checkWord (word) # calls check answer method, assigns return value to result 

        if (result == "Win"): # if method returned the string value "Win", user got the secret word 
            print("----------------------") # begins chapter 2 
            print("CHAPTER 2")
            chpOnePlay = "No" # breaks loop for chapter 1 

        elif (result == "Loss"): # if method returned the string value "Loss", user did not get the secret word 
            ans = "No" # changes ans to "No", user does not have the secret word 

    if (ans == "No"): # if user does not have the secret word 
        chpOnePlay = input("\nWould you like to play chapter 1 again? (Yes/No): ") # get chpOnePlay, ask user if they would like to play chapter 1 again 

        while (chpOnePlay != "Yes" and chpOnePlay!= "No"): # loops while user enters an invalid answer, not "Yes" or "No"
            print("You have entered an invalid answer.") # let user know they entered an invalid answer 
            chpOnePlay = input("\nWould you like to play chapter 1 again? (Yes/No): ") # get chpOnePlay, ask user if they would like to play chapter 1 again 

        while (chpOnePlay == "No"): # if user does not want to play chapter 1 again 
            leave = input("\nWould you like to leave the game? (Yes/No): ") # get leave, ask user if they would like to leave the game 
            if (leave == "Yes"): # if user wants to leave the game 
                print("\nThank you for playing: The Alkamia Adventure!") # ending message 
                exit () # stops the program from continuing 

            elif (leave == "No"): # if user does not want to leave the game 
                chpOnePlay = input("\nWould you like to play chapter 1 again? (Yes/No): ") # get chpOnePlay, ask user if they would like to play chapter 1 again 

        if (chpOnePlay == "Yes"): # if user chooses to play chapter 1 again 
            print("----------------------") # repeats chapter 1 
            print("CHAPTER 1")

randomNum = random.randint(0,5) # generate random number between 0 and 5 
secCode = chpTwo[randomNum] # assign secCode to 1 of 6 words in the chapter 2 word list, randomly selected 
chpTwoPlay = "Yes" # assign chapter 2 play, allows user to play through game once before

while (chpTwoPlay == "Yes"): # loops code if user chooses to play though chapter 2 again 
    character = int(input("\nWould you like to play as Robin (1) or Lucky (2)?: ")) # get character user will play as 

    while (character != 1 and character != 2): # loops code while user enters an invalid answer, not 1 or 2 
        print("You have entered an invalid number.") # let user know they have entered an invalid answer 
        character = int(input("\nWould you like to play as Robin (1) or Lucky (2)?: ")) # get character user will play as 

    if (character == 1): # if user chooses to play as Robin 
        print("\nRobin: It feels like I’ve been looking around forever! I don’t want to get mauled by gorillas but holy cow am I moving slowly too. Maybe I should review my knowledge of this \nrainforest before I go any further?") # storyline

        questOne = int(input("\nHow many species of mammals are found in Congo Basin Rainforest?: ")) # get questOne 
        while (questOne != 400): # loops while user does not enter the correct answer
            print("Ah wait, I’m not sure if that’s right!") # let user know they are incorrect 
            questOne = int(input("\nHow many species of mammals are found in Congo Basin Rainforest?: ")) # get questOne 

        print("Okay, this is a good start! Next question...") # continues story if user enters the correct answer, 400

        questTwo = int(input("\nHow many tree species are found in Congo Basin Rainforest?: ")) # get questTwo 
        while (questTwo != 600): # loops while user does not enter the correct answer 
            print("That doesn’t seem quite right…") # let user know they are incorrect 
            questTwo = int(input("\nHow many tree species are found in Congo Basin Rainforest?: ")) # get questTwo 

        print("I’m on a roll! Next!") # continues story if user enters the correct answer, 600

        questThree = int(input("\nHow many countries does the Congo Basin Rainforest span?: ")) # get questThree 
        while (questThree != 6): # loops while user does not enter the correct answer 
            print("That's not it...") # let user know they are incorrect 
            questThree = int(input("\nHow many countries does the Congo Basin Rainforest span?: ")) # get questThree 

        print("I really know my stuff! I shouldn’t be so worried about walking through this forest, I just need to find Lucky as soon as possible.") # continues story if user enters the correct answer, 6

        print("\nRobin: Hm… I keep seeing trees with a carving of the letter", secCode[3], ", I wonder what that means?") # hint for secret word 
        print("\nAs Robin continued her journey throughout the humid forest, she encountered an ancient temple. Unsure of where to go next, she tries to unlock the door, but there seems to be a \nfour-digit lock!")

        ranCode = random.randint(1000,9999) # generate random number between 1000 and 9999
        ranCode = str(ranCode) # converts integer type to string, to use each seperate digit in output 

        print("\nRobin: This temple looks so interesting, there are so many carvings on the golden door! Oh, it’s a gorilla with", ranCode[0], "arms. That seems a little strange. There are some stones on the \ndoor too, I wonder what type of gems they are? I see another gorilla, this one has", ranCode[1], "arms. The temple seems to be ancient. Wait, another gorilla with", ranCode[2], "arms? Hm… I see some moss \ntoo, it's covering a carving of the letter", secCode[0], "and a gorilla with", ranCode[3], "arms. What is it with all the gorilla carvings?") # hint for secret word and answer to next question

        print("\nI guess I should try to unlock this door now! I hope I find Lucky here…") 
        guess = input("What is the code: ") # get guess 

        while (guess != ranCode): # loops while user does not enter the correct code 
            print("\nI really want to get inside, let me try again!") # let user know they are incorrect 
            guess = input("What is the code: ") # get guess 

        print("\nYes! Gorilla’s aren’t so bad after all. Now, let’s see what’s inside the ancient temple...") # continues story if user enters the correct answer

    elif (character == 2): # if user chooses to play as Lucky 
        print("\nLucky: This temple is so creepy... I’m sleepy though. All I want is to take a nice nap, but there is no way I can do that in this type of atmosphere. I should just get out of here as \nsoon as possible. I’d rather sleep among the gorillas.") # storyline
        print("\nLucky walks through narrow halls until he reaches a door. What awaits him is another lock, this is one with a two-digit code.")
        print("\nLucky: Not another lock... let me test my luck and try the last number I heard someone say.")

        lastNum = int(input("\nWhat was the last number Lucky heard?: ")) # get lastNum 
        while (lastNum != 26): # loops while user does not enter the correct number 
            print("Wait that wasn’t what I heard last... let me think again. The last person I talked to was Robin, right?") # hint for user to look at first storyline
            lastNum = int(input("\nWhat was the last number Lucky heard?: ")) # get lastNum

        print("Wait, that was right? Ay, my name’s being put to good use for once!") # continues story if user enters the correct answer

        print("\nLucky: Hm 26… Robin’s age... I should really try to get out so I can find her, I hope she’s okay.") # storyline
        print("\nLucky walks through the door to reach… just another room in the temple.")
        print ("Lucky:I thought I couldn’t sleep in the previous room but this room is so much worse. I see trails of blood going up to the walls… It looks like it was supposed to outline the letters", secCode[1], "and", secCode[2], "\nAre there any doors in this room? Oh, looks there’s the door, WHY IS THERE ANOTHER LOCK ON IT? \nThis bloody lock has a 1-digit code, time to guess again... yay...") # hint for secret word

        ranGame = random.randint(0,9) # generate random number between 0 and 9
        digit = int(input("\nEnter the single digit: ")) # get digit 

        while (digit != ranGame): # loops while user does not enter the correct digit 
            print("Ah, let me try again.") # let user know they are incorrect 
            digit = int(input("\nEnter the single digit: ")) # get digit 

        print("My luck wins again! I really hope this doesn’t just lead to another room...") # continues story if user enters the correct answer

    print("\nEND OF CHAPTER 2.") # ends chapter 2 
    print("----------------------")

    ans = input("Do you have the hidden word to unlock Chapter 3? (Yes/No): ") # get ans, asks user if they have the secret word 
    while (ans != "Yes" and ans!= "No"): # loops while user enters an invalid answer, not "Yes" or "No"
        print("You have entered an invalid answer.") # let user know their answer is invalid 
        ans = input("\nDo you have the hidden word to unlock Chapter 3? (Yes/No): ") # get ans  

    if (ans == "Yes"): # if user does have the secret word 
        tries = 15 # user has 15 tries to guess the secret word 
        wordList = [] # stores user answers 
        while (tries >= 0): # loops while user has tries left 
            word = input("\nLook for clues throughout the chapter 2 story! What is the secret word? (Uppercase Letters): ")  # get word, asks user to enter their guess 
            result = checkWord (word) # calls check answer method, assigns return value to result 

        if (result == "Win"): # if method returned the string value "Win", user got the secret word 
            print("----------------------") # begins chapter 3 
            print("CHAPTER 3")
            chpTwoPlay = "No" # breaks loop for chapter 2 

        elif (result == "Loss"): # if method returned the string value "Loss", user did not get the secret word 
            ans = "No" # changes ans to "No", user does not have the secret word 

    if (ans == "No"): # if user does not have the secret word 
        chpTwoPlay = input("\nWould you like to play chapter 2 again? (Yes/No): ") # get chpTwoPlay, ask user if they would like to play chapter 2 again 

        while (chpTwoPlay != "Yes" and chpTwoPlay!= "No"): # loops while user enters an invalid answer, not "Yes" or "No"
            print("You have entered an invalid answer.") # let user know they entered an invalid answer 
            chpTwoPlay = input("\nWould you like to play chapter 2 again? (Yes/No): ") # get chpTwoPlay, ask user if they would like to play chapter 2 again 

        while (chpTwoPlay == "No"): # if user does not want to play chapter 2 again 
            leave = input("\nWould you like to leave the game? (Yes/No): ") # get leave, ask user if they would like to leave the game 
            if (leave == "Yes"): # if user wants to leave the game 
                print("\nThank you for playing: The Alkamia Adventure!") # ending message 
                exit () # stops the program from continuing 

            elif (leave == "No"): # if user does not want to leave the game 
                chpTwoPlay = input("\nWould you like to play chapter 2 again? (Yes/No): ") # get chpTwoPlay, ask user if they would like to play chapter 2 again 

        if (chpTwoPlay == "Yes"): # if user chooses to play chapter 2 again 
            print("----------------------") # repeats chapter 2 
            print("CHAPTER 2")

randomNum = random.randint(0,5) # generate random number between 0 and 5 
secCode = chpThree[randomNum] # assign secCode to 1 of 6 words in the chapter 3 word list, randomly selected 
chpThreePlay = "Yes" # assign chapter 3 play, allows user to play through game once before

def easyLevel(): # procedure method if user chooses an easy level 
    print("\nYou really think that low of yourself? Come on, you should try the hard quiz!") # storyline 
    print("Lucky: I may have the coolest job on the planet but I have the academic intelligence of a bowl of soggy cereal... wait.")
    print("Well, you didn’t really have a choice, here is the hard quiz >:)") # lets user know they must do the hard question 

while (chpThreePlay == "Yes"): # loops code if user chooses to play though chapter 3 again 
    character = int(input("\nWould you like to play as Robin (1) or Lucky (2)?: ")) # get character user will play as 

    while (character != 1 and character != 2): # loops code while user enters an invalid answer, not 1 or 2
        print("You have entered an invalid number.") # let user know they have entered an invalid answer 
        character = int(input("\nWould you like to play as Robin (1) or Lucky (2)?: ")) # get character user will play as 

    if (character == 1): # if user chooses to play as Robin 
        print("\nRobin: This ancient temple is a bit scary, but still better than being chased by a gorilla.") # storyline
        print("Robin walks into a", secCode[2], "shaped room. She’s stuck on one side as there’s a giant hole right in the center of the room!") # hint for secret word

        print("\nRobin: How am I supposed to get past this? Wait... did I just hear something?") # storyline
        print("An ominous voice whispers through Robin’s ear. 'Want to get to the other side? Shout the name of the person you want to see the most right now and I may be able to help.’")
        print("Lucky’s name pops in her mind and without hesitation, Robin screams ‘LUCKY!’. The disappointed voice tickles her ear once more, ‘No, no, you must shout his FULL name.'")

        lastName = input("\nWhat is Lucky's last name?: ") # get lastName, hint in beginning storyline
        while (lastName != "Charms"): # loops while user does not enter the correct answer
            print("Wait, that's not the right name... and I call myself his best friend...") # let user know they are incorrect 
            lastName = input("\nWhat is Lucky's last name?: ") # get lastName

        print("Ha, I couldn’t imagine having such a ridiculous name.") # continues story if user enters the correct answer, Charms

        print("\nAs Robin shouts her best friend's name, a small bridge appears across the pit.") # storyline 
        print("Robin: Not the strangest thing I’ve seen today! Time to explore this temple even further.")
        print("Robin continues to walk further in the temple until she reaches a dead end. Robin looks around in a panic, hoping to see a door or any way of escape.")
        print("Suddenly, a riddle begins to appear on the wall in front of her.")

        print("\nQuestion", secCode[3], "!") # hint for secret word

        riddleAns = input("\nWhat is at the end of rainbow?: ") # get riddleAns
        while (riddleAns != "W"): # loops while user does not enter the correct answer 
            print("Wrong answer... let me try again") # let user know they are incorrect 
            riddleAns = input("\nWhat is at the end of rainbow?: ") # get riddleAns

        print("This riddle makes no sense. IT’S CLEARLY A POT OF GOLD!\n") # continues story if user enters the correct answer, W

        for counter in range (5,-1,-1): # loop for numbers in the range of 5 and -1, counting down by 1 
            if (counter == 0): # if counter is equal to 0, output the number with 3 dots 
                print (counter, "...")
                continue # continue, does not print 0 again 
            print(counter) # print counter, creates a countdown from 5 to 0 

        print("\nThe wall slowly begins to rise, and behind it is a large room with a skinny man sleeping in the center...") 

    elif (character == 2): # if user chooses to play as Lucky 
        print("\nLucky: I walk past the door, and suddenly I hear a sharp noise. I turn around to see… SPIKES? The door turned into a bunch of spikes in the shape of the letter", secCode[0]) # hint for secret word
        print("Lucky: THE SPIKES ARE CLOSING IN ON ME, I HAVE TO RUN!")
        print("Lucky sprints away from the spikes, when a panicked voice whispers to him ‘QUICK YOU HAVE TO ANSWER THIS QUESTION TO ESCAPE THE SPIKES.’")

        lockAns = int(input("\nHow many locks have you unlocked today?: ")) # get lockAns
        while (lockAns != 3): # loops while user does not enter the correct answer
            print("I hear the voice again, ‘INCORRECT, ANSWER AGAIN BEFORE THE SPIKES HIT'") # let user know they are incorrect 
            lockAns = int(input("\nHow many locks have you unlocked today?: ")) # get lockAns

        print("Lucky: Let me get out of here!") # continues story if user enters the correct answer, 3
        print("\nAfter Lucky shouts his answer, he sees a narrow opening through the corner of his eye. He quickly gets on his hands and knees, and begins to crawl through the narrow tunnel.")
        print("Lucky: THIS TUNNEL HAS BEEN GOING ON FOREVER. Wait what’s that... a notepad? The notepad reads ‘If you would like to get out of this tunnel, complete this quiz!’ NOT ANOTHER PUZZLE!")

        subject = int(input("\nWhich subject would you like for the quiz? Math (1) or Science (2): ")) # get subject 
        while (subject != 1 and subject != 2): # loops code while user enters an invalid answer, not 1 or 2 
            print("You have entered an invalid answer.") # let user know they have entered an invalid answer 
            subject = int(input("\nWhich subject would you like for the quiz? Math (1) or Science (2): ")) # get subject 

        if (subject == 1): # if user chooses math 
            print("\nWould you like an easy or hard quiz? Type", secCode[1], "for easy and", secCode[4], "for hard.") # gives choice of two levels, includes hints for the secret word 
            level = input ("\nWhich quiz would you like to take?: ") # get level

            while (level != secCode[1] and level != secCode[4]): # loops code while user enters an invalid answer, not 1 or 2 
                print("You have entered an invalid answer.") # let user know they have entered an invalid answer 
                level = input ("\nWhich quiz would you like to take?: ") # get level

            if (level == secCode[1]): # if user chooses to play again 
                easyLevel() # calls easy level method 

            mathAns = int(input("\nIf gorilla + gorilla + gorilla = 120, gorilla + alkamia + alkamia = 100 and alkamia + robin + gorilla = 105, what is alkamia + robin?: ")) # get mathAns
            while (mathAns != 65): # loops while user does not enter the correct answer
                print("Incorrect, try again.") # let user know they are incorrect 
                mathAns = int(input("\nIf gorilla + gorilla + gorilla = 120, gorilla + alkamia + alkamia = 100 and alkamia + robin + gorilla = 105, what is alkamia + robin?: ")) # get mathAns

            print("Easy, I’m a genius!") # continues story if user enters the correct answer, 65

        elif (subject == 2): # if user chooses science  
            print ("\nWould you like an easy or hard quiz? Type", secCode[1], "for easy and", secCode[4], "for hard.") # gives choice of two levels, includes hints for the secret word 
            level = input("\nWhich quiz would you like to take?: ") # get level

            while (level != secCode[1] and level != secCode[4]): # loops code while user enters an invalid answer, not 1 or 2 
                print("You have entered an invalid answer.") # let user know they have entered an invalid answer 
                level = input ("\nWhich quiz would you like to take?: ") # get level

            if (level == secCode[1]): # if user chooses to play again 
                easyLevel() # calls easy level method 

            sciAns = input("\nWhat is the first element on the periodic table?: ") # get sciAns
            while (sciAns != "Hydrogen"): # loops while user does not enter the correct answer
                print("Incorrect, try again.") # let user know they are incorrect 
                sciAns = input("\nWhat is the first element on the periodic table?: ") # get sciAns

            print("Easy, I’m a genius!") # continues story if user enters the correct answer, "Hydrogen"

        print("\nA door finally appears in front of Lucky, and he runs towards it. Mentally and physically exhausted, he opens the door and collapses once inside.")
        print("The room has light instead of blood and Lucky decides it's the right time to take a nap!")

    print("\nEND OF CHAPTER 3.") # ends chapter 3 
    print("----------------------")

    ans = input("Do you have the hidden word to end the game? (Yes/No): ") # get ans, asks user if they have the secret word 
    while (ans != "Yes" and ans!= "No"): # loops while user enters an invalid answer, not "Yes" or "No"
        print("You have entered an invalid answer.") # let user know their answer is invalid 
        ans = input("\nDo you have the hidden word to end the game? (Yes/No): ") # get ans  

    if (ans == "Yes"): # if user does have the secret word 
        tries = 15 # user has 15 tries to guess the secret word 
        wordList = [] # stores user answers 
        while (tries >= 0): # loops while user has tries left 
            word = input("\nLook for clues throughout the chapter 3 story! What is the secret word? (Uppercase Letters): ") # get word, asks user to enter their guess 
            result = checkWord (word) # calls check answer method, assigns return value to result 

        if (result == "Win"): # if method returned the string value "Win", user got the secret word 
            print("----------------------") # begins epilogue 
            print("EPILOGUE")
            chpThreePlay = "No" # breaks loop for chapter 3 

        elif (result == "Loss"): # if method returned the string value "Loss", user did not get the secret word 
            ans = "No" # changes ans to "No", user does not have the secret word 

    if (ans == "No"): # if user does not have the secret word 
        chpThreePlay = input("\nWould you like to play chapter 3 again? (Yes/No): ") # get chpThreePlay, ask user if they would like to play chapter 3 again 

        while (chpThreePlay != "Yes" and chpThreePlay!= "No"): # loops while user enters an invalid answer, not "Yes" or "No"
            print("\nYou have entered an invalid answer.") # let user know they entered an invalid answer 
            chpThreePlay = input("\nWould you like to play chapter 3 again? (Yes/No): ") # get chpThreePlay, ask user if they would like to play chapter 3 again 

        while (chpThreePlay == "No"): # if user does not want to play chapter 3 again 
            leave = input("\nWould you like to leave the game? (Yes/No): ") # get leave, ask user if they would like to leave the game
            if (leave == "Yes"): # if user wants to leave the game 
                print("\nThank you for playing: The Alkamia Adventure!") # ending message 
                exit () # stops the program from continuing 

            elif (leave == "No"): # if user does not want to leave the game 
                chpThreePlay = input("\nWould you like to play chapter 3 again? (Yes/No): ") # get chpThreePlay, ask user if they would like to play chapter 3 again 

        if (chpThreePlay == "Yes"): # if user chooses to play chapter 3 again 
            print("----------------------") # repeats chapter 3 
            print("CHAPTER 3")

print("\nRobin walks through the door to see Lucky taking a nap on the floor.") # storyline

print("\nRobin: LUCKY!")

print("\nTears form in Robin’s eyes as she sees her best friend alive and well. Lucky jolts up from his slumber, annoyed at the sudden disturbance.")
print("He opens his eyes to see Robin crying.")

print("\nLucky: Ew, why are you crying?")
print("Robin: BECAUSE YOU'RE NOT DEAD.")
print("Lucky: ... Wait.. YOU’RE NOT DEAD EITHER!")

print("\nRobin runs up and gives Lucky a hug. The two are happier than ever to be reunited.")

print("\nLucky: Okay that’s enough of that.. Let’s just get out of here.")
print("Robin: Agreed, I’m already sick of the smell of this place. Let’s go.")

print("\nAfter another while of exploring the temple, the two explorers find a way to escape. Robin and Lucky walk into the rainforest, glad to have found no gorillas.")
print("Robin sees a little shimmer from the corner of her eye.")

print("\nRobin: Wait Lucky... Do you see that?")
print("Lucky: I don’t want to see anything, LET’S JUST GO HOME.")

print("\nRobin forces Lucky to turn in the direction of the shimmer. Robin’s eyes go wide as she finds the source of the glow.")

print("\nRobin: IT’S THE ALKAMIA! WE FOUND THEM, WE DID IT.")
print("Lucky: No way... who knew an angry gorilla, falling into a pit, running away from spikes, an endless tunnel and a nap in an ancient temple would lead us to what we were looking for.")
print("Robin: Guess Lucky Charms isn’t so unlucky after all.")

print("\nThe End. Thank you for playing: The Alkamia Adventure!") # ending message 
