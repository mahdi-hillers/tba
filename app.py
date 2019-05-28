# All computers in the CS Class has been stolen. You need to figure out who did this.'
## You find some cables out ##1 Check the cables to fingerprint ##2 See where the cables have been taken from
    ##1 You need to wait for 5 days. ##3 Pressure the agent ##4 Let it go
        ##3 You get the results and you have 3 suspects ##5 Prosecute them immidiately ##6 Ask questions from the suspects 
        ##4 Four empty loops. Nothing happens
import os
import time
scenes = 6
funci = 0
def intro():
    print("All computers in the CS Class have been stolen. You need to figure out who did this!\n Mrs. Fournier trusts you to find who stole all the computers.")
def cables():
    global funci
    print("There are some cables found on the ground near pile of mess in the robotics room. Cables are used by everyone for compiling programs. What would you do?\n")
    print("A: Pick up the cables and do a fingerprint analysis on them")
    print("B: The fingerprint of everyone would be on them. Don't pick them up and keep searching ")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += 14
    if (userInput == "B"):
        funci += 1
    return userInput
def cablesA():
    global funci
    print("Tboy is an expert in the fingerprint analysis. He says it takes 5 days to do the analysis.")
    print("\n What would you do?")
    print("\n A: Give it to TBOY and wait for the results to come in")
    print("\n B: NO YOU TELL TBOY HOW MUCH YOU CARE ABOUT MRS FOURNIER AND CS CLASS! HE SHOULD GIVE THE RESULTS TODAY!")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += 14
    if (userInput == "B"):
        funci += 1
    return userInput
def cablesAA():
    global funci
    print("Wait for 10 seconds until the results come in.")
    time.sleep(10)
    print("The results are here! We have five suspects!")
    print("\n The suspects are:")
    print("\n - Michael Y \n - Faateh Mohammad \n - Pablo D \n - Jay Katyan \n - Who Said Shake")
    print ("\n BTW IF YOU DON'T KNOW ALREAYD, WHO SAID SHAKE IS: Usayd S")
    print("\n What do you want to do with the suspects?")
    print("\n A: Talk to them all and get some clues")
    print("\n B: Ehh you know what just arrest them all")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci -= 5
    if (userInput == "B"):
        funci -= 11
    return userInput
def cablesAB():
    global funci
    print("The results are here! We have five suspects!")
    print("\n The suspects are:")
    print("\n - Michael Y \n - Faateh Mohammad \n - Pablo D \n - Jay Katyan \n - Who Said Shake")
    print ("\n BTW IF YOU DON'T KNOW ALREAYD, WHO SAID SHAKE IS: Usayd S")
    print("\n What do you want to do with the suspects?")
    print("\n A: Talk to them all and get some clues")
    print("\n B: Ehh you know what just arrest them all")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += 8
    if (userInput == "B"):
        funci += 1
    return userInput
def cablesABA():
    global funci
    print("None of them talks except Faateh. Faateh says Michael has stolen the laptops for political reasons.")
    print("\n A: Get more information")
    print("\n B: Michael is a nice guy. Don't do anything. Just quit.")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += int(((scenes/2)/2) + scenes/2)
    if (userInput == "B"):
        funci += 1
    return userInput
def cablesABAA():
    global funci
    print("Faateh shows you the video of a surveillence camera. Michael did actually pick all the laptops.")
    print("\n A: Arrest Michael")
    print("\n B: Nah. Justin is good at editing photos and videos. These are all fake.")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += 1
    if (userInput == "B"):
        funci += 4
    return userInput
def cablesABAAA():
    print("CONGRATS YOU WON!")
def cablesABAAB():
    global funci
    print("Michael did actually steal the laptops. So nice job.")
    print("\n GAME OVER")
def cablesABAB():
    global funci
    print("Michael did actually steal the laptops. So nice job.")
    print("\n GAME OVER")
def cablesABB():
    global funci
    print("Michael is protesting that he didn't do it and that he shouldn't be arrested.")
    print("\n A: Tell him to shut up")
    print("\n B: Ask Michael who did this")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += 2
    if (userInput == "B"):
        funci += 1
    return userInput
def cablesABBA():
    global funci
    print("That's it. You're a horrible gamer.")
    print("\n Everyone's pissed rn and you've been criticized for not doing your job properly")
    print("\n A: Flee to Egypt")
    print("\n B: Ehhh life is life. Get some emotional support instead")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += 2
    if (userInput == "B"):
        funci += 1
    return userInput
def cablesABBAA():
    global funci
    print("Okay coward, since you don't know any Arabic you have two options:")
    print("\n A: Get your passport and leave RN")
    print("\n B: Ask Michael to teach you Arabic")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += 2
    if (userInput == "B"):
        funci += 1
    return userInput
def cablesABBAAA():
    global funci
    print("\n You're in the streets of Egypt and you're enjoying some fine beer when you're arrested for dirnking.")
    print("\n You're in the prison now. WHAT A WEIRD LIFE")
def cablesABBAAB():
    global funci
    print("\n Michael is not teaching you arabic. Time is up. FBI has arrested you.")
    print("\n GAME OVER")

def cablesABBAB():
    global funci
    print("\n No one is willing to give you some emotional support. ")
    print("\n You just died from depression. ")
    print("\n \n GAME OVER! ")
def cablesABBB():
    print("You just died because of small pox.")
    print("\n GAME OVER!")
def cablesB():
    global funci
    print("You see Pablo at his table (where he usually always certainly seats). You ask him this questions:")
    print("\n Do like the Emoji Movie? But then you realize the movie is really gay. So you ask him the real question:")
    print("\n Did you see anyone using the laptops this morning on school?")
    print("\n He says yeah. Jay was programming his BIG ROBOT!")
    print("\n Cameron confirms the first statement. But he says Jay's robot is really small.")
    print("\n What would you do?")
    print("\n A: Talk to Jay and see what he was doing with the laptops")
    print("\n B: Jay is a nice kid. Someone else should've done it. ")
    userInput = input("You selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += 8
    if (userInput == "B"):
        funci += 1
def cablesBA():
    global funci
    print("Jay says he was coding his BIG ROBOT!")
    print("\n A: Arrest jay for lying about the size of his robot")
    print("\n B: Leave jay alone")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += 4
    if (userInput == "B"):
        funci += 1
    return userInput
def cablesBAA():
    global funci
    print("Congrats! You found who had stolen the laptops! JAY!")
    print("\n YOU'RE WRONG. Jay didn't steal the laptops. He actually had a big robot.")
    print("\n You are asked to leave your duties to WHO SAID SHAKE until Mrs. Fournier has investigated your case and the mistaked you've made.")

def cablesBAB():
    global funci
    print("Okay nice job. You have no suspects left. ")
    print("\n A: Just tell Mrs. Fournier WHO SAID SHAKE has stolen the laptops")
    print("\n B: Tell Mrs. Fournier you are not fit to decide who did this mess")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += 2
    if (userInput == "B"):
        funci += 1
    return userInput
def cablesBABA():
    print("\n Horrible. Usayd wasn't the one who stole the latops. Oh well. Life is life.")
    print("\n nice job. game over")
def cablesBABB():
    print("\n Okay nice. You have an F in CSP rn. ")
    print("game over")
def cablesBB():
    global funci
    print("Okay nice job. You have no suspects left. ")
    print("\n A: Just tell Mrs. Fournier WHO SAID SHAKE has stolen the laptops")
    print("\n B: Tell Mrs. Fournier you are not fit to decide who did this mess")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += 2
    if (userInput == "B"):
        funci += 1
    return userInput
def cablesBBA():
    global funci
    print("Usayd has been arrested. He is saying that you haven't done your job correctly.")
    print("\n A: I know what I'm doing")
    print("\n B: Tell Usayd no he's the one who hasn't done the right thing")
    userInput = input("Your selection (UPPER CASE!): ")
    if (userInput == "A"):
        funci += 2
    if (userInput == "B"):
        funci += 1
    return userInput
def cablesBBAA():
    global funci
    print("\n Mrs. Fournier punishes Usayd. Horrible. Usayd wasn't the one who stole the latops. Oh well. Life is life.")
    print("\n nice job. game over")
def cablesBBAB():
    global funci
    print("\n Mrs. Fournier punishes Usayd. Horrible. Usayd wasn't the one who stole the latops. Oh well. Life is life.")
    print("\n nice job. game over")
def cablesBBB():
    global funci
    print("\n Okay nice. You have an F in CSP rn. ")
    print("game over")
funcArray = [cables, cablesB, cablesBB, cablesBBB, cablesBBA, cablesBBAB, cablesBBAA, cablesBBAB, cablesBBAA, cablesBA, cablesBAB, cablesBABB, cablesBABA, cablesBAA, cablesA, cablesAB, cablesABB, cablesABBB, cablesABBA, cablesABBAB, cablesABBAA, cablesABBAAB, cablesABBAAA, cablesABA, cablesABAA, cablesABAAA, cablesABAAB, cablesABAB, cablesAA]
funciArray = []
intro()
while (funci < 50):
    os.system("clear")
    userInput = funcArray[funci]()
