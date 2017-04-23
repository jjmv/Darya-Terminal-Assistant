import json
import os

def main(rawCommand):
    uCommand = rawCommand.split(" ")
    with open("/usr/local/bin/dlib/Plugins/HelperPlugin/tohelp.json") as data_file:
        data = json.load(data_file)
    try:
        toSearch = data[str(uCommand[1])]
    except Exception:
        return "Im sorry, i couldn't find anything "
    rute = "/usr/local/bin/dlib/Plugins/" + toSearch + "/info.json"

    try:
        with open(rute) as info:
            info_file = json.load(info)
    except Exception:
        return "Sorry, The plugin that you are searching for does not have Helper integration"

    stringToreturn = "name: " + info_file["name"] + "\n" + "version: " + info_file["version"]
    stringToreturn += "\n" + "author: " + info_file["author"] + "\n" + info_file["contact"]
    stringToreturn += "\n" + "description: " + info_file["desc"] + "\n\n"
    stringToreturn += "Features \n\n"

    for feature in info_file["features"]:
        stringToreturn += feature + "\n"

    stringToreturn += "\nNotes \n\n"

    for note in info_file["notes"]:
        stringToreturn += note + "\n"

    return stringToreturn
