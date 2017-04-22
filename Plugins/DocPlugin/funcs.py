import json
import os

def getDoc(lang,feature):
    doc_needed = ""
    if lang == "py3":
        doc_needed = "python3"
    with open("/usr/local/bin/dlib/Plugins/DocPlugin/langDocs/"+ doc_needed + ".json") as data_file:
        data = json.load(data_file)

    try:
        sample = data["langDoc"][feature]["sample"]
    except Exception:
        return "Im sorry, i couldn't find anything "
    sampleText = ""
    for line in sample:
        sampleText += line + "\n"
    daryaResponse = "Wait Master, searching in " + doc_needed + " docs... \n" + str(data["langDoc"][feature]["desc"]) + "\n\n"
    daryaResponse += sampleText
    return daryaResponse
