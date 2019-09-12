#Bond Ragsdale, Devan Tighe, Kiersten Mikulsky, Bryan Stone, Nathan Smith

characterNumber = 0
chapter = 0

def startFunction():
    print("1. Dante")
    print("2. Virgil")
    print("3. Charon")
    characterNumber = int(input("Please type the number of the character you want to learn about: "))
    chapter = int(input("Which chapter are you up too? "))
    getSummary(chapter, characterNumber)



#writing helper functions for each character, that just prints a string based on the chapter 

def danteFunction(chapter):
    if chapter == 1:
        print("Dante finds himself in a dark wooded forest, walking alone and encountering wild beasts. He is then saved from the animals by Virgil")
    elif chapter == 2 or chapter == 3:
        print("Dante was in a wooded forest, until Virgil came to his aid. He has now progressed to the entrance of hell")

def virgilFunction(chapter):
    if chapter == 1:
        print("Virgil comes to help Dante when he is lost in a wood. He is a deceased poet and exists now as a shade, and tells Dante that he will guide him through hell")
    elif chapter == 2 or chapter == 3: 
        print("Virgil has saved Dante and led him to the entrance of hell")

def charonFunction(chapter):
    if chapter < 3:
        print("Invalid")
    elif chapter >= 3:
        print("Charon is the demon that brings people to hell across the river Acheron")



#getSummary takes in the values from the user, and matches the desired character, and then calls the corresponding helper function

def getSummary(chapterNum, characterNum):
    chapter = chapterNum
    character = characterNum
    
    if characterNum == 1:
        danteFunction(chapter)
    elif characterNum == 2: 
        virgilFunction(chapter)


startFunction()


