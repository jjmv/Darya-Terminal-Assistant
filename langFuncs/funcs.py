from Plugins.DocPlugin import funcs as docfuncs
from Plugins.CodePlugin import funcs as codefuncs
options = [
    "-c", # Code generation options
    "-w", # Code question options
]

def getOption(ucommand, commandFromUser):
    rawCommand = commandFromUser.split(" ")
    if rawCommand[1] in options:
        return executeOption(rawCommand)
    else:
        return rawCommand[1] + " not finded"

def executeOption(rawCommand):
    if (rawCommand[1] == "-w"):
        return docfuncs.getDoc(rawCommand[0], rawCommand[2])
    if (rawCommand[1] == "-c"):
        return codefuncs.switchoflangs(rawCommand)
