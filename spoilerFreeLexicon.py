#Bond Ragsdale, Devan Tighe, Kiersten Mikulsky, Bryan Stone, Nathan Smith

characterNumber = 0
chapter = 0

def startFunction():
    print("1. Dante")
    print("2. Virgil")
    print("3. Charon")
    print("4. Homer")
    print("5. Plato")
    print("6. Socrates")
    print("7. Minos")
    print("8. Francesca")
    print("9. Cerberus")
    print("10. Plutus")
    print("11. Phlegyas")
    print("12. Filippo Argenti")
    print("13. Furies")
    print("14. Farinata")
    print("15. Beatrice")
    print("16. Minotaur")
    print("17. Frederick II")
    print("18. Capaneus")
    print("000. Exit program, enter chapter 0 as well")

    characterNumber = int(input("Please type the number of the character you want to learn about: "))
    chapter = int(input("Which chapter are you up too? "))
    getSummary(chapter, characterNumber)



#writing helper functions for each character, that just prints a string based on the chapter 

def danteFunction(chapter):
    if chapter >= 1:
        print("Dante, of Florence Italy, is the protagonist of 'The Inferno'. He embarks on a journey throughout Hell, learning about the after life and the tortures that await souls.")
    
def virgilFunction(chapter):
    if chapter >= 1:
        print("Virgil, a famous Poet, is Dante's guide through Hell. When he finds him in a darkened wood, he tells Dante they can go through all of Hell so that Dante may continue his adventure. Virgil provides insights into sinners, and being familiar with Hell, helps Dante navigate the dangerous and unfamiliar territory.")
    
def charonFunction(chapter):
    if chapter < 3:
        print("This character has not been encountered yet")
    elif chapter >= 3:
        print("Charon is the demon that brings people to hell across the river Acheron")

def homerFunction(chapter):
    if chapter < 4:
        print("This character has not been encountered yet")
    elif chapter >= 4:
        print("Homer is a shade that exists in Limbo, having lived before Christianity")

def platoFunction(chapter):
    if chapter < 4:
        print("This character has not been encountered yet")
    elif chapter >= 4:
        print("Plato is a shade that exists in Limbo, having lived before Christianity")

def socratesFunction(chapter):
    if chapter < 4:
        print("This character has not been encountered yet")
    elif chapter >= 4:
        print("Socrates is a shade that exists in Limbo, having lived before Christianity")

def minosFunction(chapter):
    if chapter < 5:
        print("This character has not been encountered yet")
    elif chapter >= 5:
        print("Minos is the beast who stands at the entrance of the second circle of Hell, and evaluates souls to determine which circle they belong in")

def francescaFunction(chapter):
    if chapter < 5:
        print("This character has not been encountered yet")
    elif chapter >= 5:
        print("Francesca is a soul doomed to the second circle, due to her lustful and adulterous acts in life")

def cerberusFunction(chapter):
    if chapter < 6:
        print("This character has not been encountered yet")
    elif chapter >= 6:
        print("Cerberus is a three-headed, monsterous dog who tortures the souls in the third circle (the circle of the Gluttons) by chasing and clawing them")

def plutusFunction(chapter):
    if chapter < 7:
        print("This character has not been encountered yet")
    elif chapter >= 7:
        print("Plutus is the god of wealth and riches, and guards the Fourth Circle of Hell, which contains Hoarders and Wasters, who are doomed to roll stones at one another for eternity")

def phlegyasFunction(chapter):
    if chapter < 8:
        print("This character has not been encountered yet")
    elif chapter >= 8:
        print("The boatman who takes souls through the marsh of Styx, from the fifth to the sixth circle")

def argentiFunction(chapter):
    if chapter < 8:
        print("This character has not been encountered yet")
    elif chapter >= 8:
        print("An enemy of Dante in his earthly life, who has been damned to the fifth circle for being wrathful. After getting into an argument, Dante wishes Argenti to recieve even harsher punishment, and the other wrathful souls come and tear Argenti to pieces")

def furiesFunction(chapter):
    if chapter < 9:
        print("This character has not been encountered yet")
    elif chapter >= 9:
        print("Demons that attempt to impede Dante's progress through hell")

def farinataFunction(chapter):
    if chapter < 10:
        print("This character has not been encountered yet")
    elif chapter >= 10:
        print("Dante's political enemy from life")

def beatriceFunction(chapter):
    if chapter < 10:
        print("This character has not been encountered yet")
    elif chapter >= 10:
        print("Dante's lover")

def minotaurFunction(chapter):
    if chapter < 12:
        print("This character has not been encountered yet")
    elif chapter >= 12:
        print("Half man half bull that guards the seventh circle, the circle of violence")

def frederickFunction(chapter):
    if chapter < 13:
        print("This character has not been encountered yet")
    elif chapter >= 13:
        print("A soul who killed himself in life and is eternally doomed to being a tree, picked at by harpies")

def capaneusFunction(chapter):
    if chapter < 14:
        print("This character has not been encountered yet")
    elif chapter >= 14:
        print("A man who scorned god in life, and was slain by a thunderbolt thrown from the hand of Zeus. Suffers on a desert under a rain of fire.")





#getSummary takes in the values from the user, and matches the desired character, and then calls the corresponding helper function

def getSummary(chapterNum, characterNum):
    chapter = chapterNum
    character = characterNum
    
    if characterNum == 1:
        danteFunction(chapter)
        startFunction()
    elif characterNum == 2: 
        virgilFunction(chapter)
        startFunction()
    elif characterNum == 3:
        charonFunction(chapter)
        startFunction()
    elif characterNum == 4:
        homerFunction(chapter)
        startFunction()
    elif characterNum == 5:
        platoFunction(chapter)
        startFunction()
    elif characterNum == 6:
        socratesFunction(chapter)
        startFunction()
    elif characterNum == 7:
        minosFunction(chapter)
        startFunction()
    elif characterNum == 8:
        francescaFunction(chapter)
        startFunction()
    elif characterNum == 9:
        cerberusFunction(chapter)
        startFunction()
    elif characterNum == 10:
        plutusFunction(chapter)
        startFunction()
    elif characterNum == 11:
        phlegyasFunction(chapter)
        startFunction()
    elif characterNum == 12:
        argentiFunction(chapter)
        startFunction()
    elif characterNum == 13:
        furiesFunction(chapter)
        startFunction()
    elif characterNum == 14:
        farinataFunction(chapter)
        startFunction()
    elif characterNum == 15:
        beatriceFunction(chapter)
        startFunction()
    elif characterNum == 16:
        beatriceFunction(chapter)
        startFunction()
    elif characterNum == 17:
        frederickFunction(chapter)
        startFunction()
    elif characterNum == 18:
        frederickFunction(chapter)
        startFunction()
    elif characterNum == 000:
        print("The Lexicon has been terminated.")


startFunction()


