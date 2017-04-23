import os

def main(rawCommand):
    rawCommand = rawCommand.split(" ")
    try:
        if rawCommand[1] == "py3":
            return python3funcs(rawCommand)
        if rawCommand[1] == "html" or rawCommand[1] == "h5":
            return html5funcs(rawCommand)
        else:
            return "Master, type 'darya help new'"
    except Exception:
        return "Master, type 'darya help new'"

def python3funcs(rawCommand):
    return "! wth python3"

def html5funcs(rawCommand):
    if rawCommand[2] == "n" or rawCommand[2] == "normal":
        return os.system("/usr/local/bin/dlib/Plugins/CodePlugin/CodeGeneratorScripts/html/normalStruct.sh " + rawCommand[3])
