from CommandFunctions import funcs

class UserCommand:
    def __init__(self, ucommand):
        self.userCommand = ucommand
    
    def returnUserCommand(self):
        return self.userCommand
    
    def identifyCommand(self):
        return funcs.identifyCommand(self.userCommand)