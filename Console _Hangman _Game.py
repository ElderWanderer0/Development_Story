#Console hangman game
#have some issues, tryna fix them

import random


wordList = ["Book", "Internet", "Coffe", "Computer", "Human", "Square", "Circle", "Squid", "Crab", "Fish", "Gun",
            "Society", "Reject", "Temporary", "Temperature", "Crocodile", "Panda", "War", "Sword", "Dentist", "Rainbow",
            "Freedom", "Heaven"]

Word = random.choice(wordList).lower()
wordLenght = len(Word)

theHangman = [[" ", "O"],
              [" ", "|"],
              ["/", "|", "\\"],
              [" ", "|"],
              ["/", " ", "\\"]]

theFinalHangman = [[" ", " "],
                   [" ", " "],
                   [" ", " ", " "],
                   [" ", " "],
                   [" ", " ", " "]]

lines = []
for any_line in range(wordLenght):
    lines.append("_")
print(lines)

wordinlist = []
for any_word in Word:
    wordinlist.append(any_word)
# print(wordinlist)


for a in theHangman:
    print(" ".join(a))
print("")


givenWords = []


while True:
    enumList = []
    givenWord = str(input("Enter a letter : "))
    if givenWord in givenWords:
        print("This word has been used")
    else:
        givenWords.append(givenWord)
    print("You used those words " + "(" + ", ".join(givenWords) + ",)")
    if givenWord in Word:
        for num_finder, word_finder in enumerate(wordinlist):
            if givenWord == word_finder:
                enumList.append(num_finder)
                for t in range(len(enumList)):
                    lines[enumList[t]] = wordinlist[enumList[t]]
                    t = t + 1
        print(lines)
    else:
        print("This character is not in the word")
        print(lines)

        while True:
            deleteHangpiece = random.randint(0, 4)
            if deleteHangpiece == 2 or deleteHangpiece == 4:
                pieceChoicer = random.randint(0, 2)
                if theHangman[deleteHangpiece][pieceChoicer] == " ":
                    pass
                else:
                    break
            else:
                pieceChoicer = random.randint(0, 1)
                if theHangman[deleteHangpiece][pieceChoicer] == " ":
                    pass
                else:
                    break

        theHangman[deleteHangpiece][pieceChoicer] = " "
    for a in theHangman:
        print(" ".join(a))
    print("")

    if theHangman == theFinalHangman:
        print("You lost the game")
        print(f"The word was {Word}")
        break
    else:
        pass

    if lines == wordinlist:
        print("You won the game!")
        break
    else:
        pass
