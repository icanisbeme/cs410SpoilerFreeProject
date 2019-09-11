#Bond Ragsdale, Devan Tighe, Kiersten Mikulsky, Bryan Stone, Nathan Smith

characterNumber = 0
chapter = 0

def startFunction():
    print("1. Dante")
    print("2. Virgil")
    characterNumber = int(input("Please type the number of the character you want to learn about: "))
    chapter = int(input("Which chapter are you up too? "))
    getSummary(chapter, characterNumber)



#writing helper functions for each character, that just prints a string based on the chapter 

def danteFunction(chapter):
    if chapter == 1:
        print("dante up to ch 1")
    elif chapter == 2:
        print("dante up to ch 2")

def virgilFunction(chapter):
    if chapter == 1:
        print("virgil chapter 1")
    elif chapter == 2: 
        print("virgil chapter 2")



#getSummary takes in the values from the user, and matches the desired character, and then calls the corresponding helper function

def getSummary(chapterNum, characterNum):
    chapter = chapterNum
    character = characterNum
    
    if characterNum == 1:
        danteFunction(chapter)
    elif characterNum == 2: 
        virgilFunction(chapter)


startFunction()


