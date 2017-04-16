import os
def switchoflags(rawCommand):
    if rawCommand[0] == "py3":
        return python3funcs(rawCommand)
    if rawCommand[0] == "html" or rawCommand[0] == "h5":
        return html5funcs(rawCommand)

def python3funcs(rawCommand):
    return "! wth python3"

def html5funcs(rawCommand):
    if rawCommand[2] == "n" or rawCommand[2] == "normal":
        return os.system("/usr/local/bin/dlib/CodeGeneratorScripts/html/normalStruct.sh " + rawCommand[3])
    if rawCommand[2] == "angular1":
        return os.system("/usr/local/bin/dlib/CodeGeneratorScripts/html/angular1Struct.sh" + rawCommand[3]) 
