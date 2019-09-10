#Bond Ragsdale, Devan Tighe, Kiersten Mikulsky, Bryan Stone, Nathan Smith

# define the function blocks
# def zero():
#     print ("You typed zero.\n")

# def sqr():
#     print ("n is a perfect square\n")

# def even():
#     print ("n is an even number\n")

# def prime():
#     print ("n is a prime number\n")

# # map the inputs to the function blocks
# options = {0 : zero,
#            1 : sqr,
#            4 : sqr,
#            9 : sqr,
#            2 : even,
#            3 : prime,
#            5 : prime,
#            7 : prime,
# }


characterName = ""
chapter = ""

def startFunction():
    characterName = input("Please type the name of the character you want to learn about: ")
    chapter = input("Which chapter are you up too? ")
    print(characterName)
    print(chapter)

startFunction()

if characterName == "Dante":
    danteHelper()



def danteHelper():
    print("Dante is a cool dude")