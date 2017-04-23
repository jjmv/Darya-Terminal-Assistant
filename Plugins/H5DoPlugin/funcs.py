import os

def main(rawCommand):
    rawCommand = rawCommand.split(" ")
    try:
            return html5funcs(rawCommand)
    except Exception:
        return "Master, type 'darya help new'"

def html5funcs(rawCommand):
    if rawCommand[1] == "n" or rawCommand[1] == "normal":
        return os.system("/usr/local/bin/dlib/Plugins/H5DoPlugin/CodeGeneratorScripts/html/normalStruct.sh " + rawCommand[2])
