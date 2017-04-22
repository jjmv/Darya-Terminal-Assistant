from Plugins.DocPlugin import funcs as docfuncs
from Plugins.CodePlugin import funcs as codefuncs
options = [
    "code", # Code generation options
    "-c", # Code generation options
    "-!",
    "-w", # Code question options
    "what",  # Code question options
    "-?", # Code question options
]

def getOption(ucommand, commandFromUser):
    rawCommand = commandFromUser.split(" ")
    if rawCommand[1] in options:
        return executeOption(rawCommand)
    else:
        return rawCommand[1] + " not finded"

def executeOption(rawCommand):
    if (rawCommand[1] == "-w" or rawCommand[1] == "what" or rawCommand[1] == "-?"):
        return docfuncs.getDoc(rawCommand[0], rawCommand[2])
    if (rawCommand[1] == "-c" or rawCommand[1] == "code" or rawCommand[1] == "-!" ):
        return codefuncs.switchoflangs(rawCommand)
