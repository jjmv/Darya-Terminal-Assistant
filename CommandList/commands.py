commandsRegistered = [
    "help", #Summons helper plugin
    "date",
    "calendar",
    #Langs
    'py3', # Python 3 with -c summons codePlugin and with -w summons docsPlugin
    'html', #Html 5 with -c summons codePlugin and with -w summons docsPlugin
    "h5", #Html 5 with -c summons codePlugin and with -w summons docsPlugin
    #langs finished
    'location',
    'where am i',
]

def returnCommandList():
    global commandsRegistered
    return commandsRegistered
