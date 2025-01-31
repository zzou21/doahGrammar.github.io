import pandas as pd, json, csv

# This function turns CSV to JSON
def csvJson(csvFile, JsonFile):
    dictionaryDoAHContent = {} #format: {"name": [ID, "overview"]
    with open(csvFile, "r", encoding="utf-8") as csvContent:
        doahCSVContent = csv.reader(csvContent)
        for oneRowHistorian in doahCSVContent:
            try:
                historianID = int(oneRowHistorian[0])
                historianName = oneRowHistorian[1]
                historianOverview = oneRowHistorian[2]
                dictionaryDoAHContent[historianName] = [historianID, historianOverview]
            except ValueError: continue
    with open(JsonFile, "w", encoding="utf-8") as jsonFileDump:
        json.dump(dictionaryDoAHContent, jsonFileDump, ensure_ascii=False, indent=4)
    print("Converted to JSON.")

# This function stores all historian names with their ID numbers in another JSON.
# DO NOT cross-reference variable names among functions.
def historianIDJSON(csvFile, JsonFile):
    nameIdDict = {}
    with open(csvFile, "r", encoding="utf-8") as csvContent:
        doahCSVContent = csv.reader(csvContent)
        for oneRowHistorian in doahCSVContent:
            try:
                historianID = int(oneRowHistorian[0])
                historianName = oneRowHistorian[1]
                # historianOverview = oneRowHistorian[2]
                nameIdDict[historianID] = historianName
            except ValueError: continue
    with open(JsonFile, "w", encoding="utf-8") as jsonContent:
        json.dump(nameIdDict, jsonContent, ensure_ascii=False, indent = 4)

if __name__=="__main__":
    csvFilePath = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/DoAHCSVContent.csv"
    JsonFilePathDestination = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/doahContentJSON.json"
    historianNamesJson = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/historianNames.json"
    # csvJson(csvFilePath, JsonFilePathDestination)
    historianIDJSON(csvFilePath, historianNamesJson)