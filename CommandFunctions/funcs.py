import os
from CommandList import commands
from langFuncs import langfuncs
commandsList = []
commandsList = commands.returnCommandList()
def identifyCommand(ucommand):
    global commandsList
    sentence = ucommand.split()
    for word in sentence:
        for command in commandsList:
            if command in sentence:
                return sentence[sentence.index(command)]
    letters = []
    concurency = []
    cont = 0;
    for l in ucommand:
        letters.append(l)
    
    for command in commandsList:
        cont = 0
        for letter in letters:
            if letter in command:
                cont += 1
        concurency.append(cont)
    
    maxCurrency = max(concurency)
    commandUsed = commandsList[concurency.index(maxCurrency)]
    return commandUsed                 

def executeCommand(rCommand, commandFromUser):
    if(rCommand == "date"):
        return os.system(rCommand)
    if(rCommand == "calendar"):
        return os.system("cal")
    if(rCommand == "location"):
        from LocationFunctions import locationFunctions
        return locationFunctions.returnLocation()
    if(rCommand == "where am i"):
        from LocationFunctions import locationFunctions 
        return locationFunctions.returnLocation()
    if(rCommand == "py3"):
        return langfuncs.getOption("py3",commandFromUser)
    if(rCommand == "html" or rCommand == "h5"):
        return langfuncs.getOption("html", commandFromUser)