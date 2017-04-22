import sys
from CommandList import commands
from Classes.UserCommand import UserCommand
from CommandFunctions import funcs

sys.argv.pop(0)
commandFromUser = " ".join(sys.argv)
userCommand = UserCommand(commandFromUser)
registeredCommand = userCommand.identifyCommand()
daryaAnswer = funcs.executeCommand(registeredCommand, commandFromUser)
if daryaAnswer != 0:
    print(daryaAnswer)
