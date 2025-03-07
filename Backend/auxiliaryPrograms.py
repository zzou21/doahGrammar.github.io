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

#This function creates a dictionary of different variations of a historian's name in preparation for spelling check reference. Example data format: 'Pillsbury, Edmund': ['Pillsbury', ' Edmund Pillsbury']
def nameVariations(historianNameJsonFile, historianNamesUpdatedStorageJson):
    with open (historianNameJsonFile, "r", encoding="utf-8") as historianNames:
        historianNamesDict = json.load(historianNames)
    updatedHistoriansNamesDict = {}
    for historianID, name in historianNamesDict.items():
        updatedHistoriansNamesDict[name] = []
        nameSplitByComma = name.split(",")
        updatedHistoriansNamesDict[name].append(name)
        if len(nameSplitByComma) > 1 and len(nameSplitByComma) <= 3:
            updatedHistoriansNamesDict[name].append(nameSplitByComma[0])
            firstLastNames = nameSplitByComma[1] + " " + nameSplitByComma[0]
            firstLastNames.strip()
            # print(firstLastNames)
            updatedHistoriansNamesDict[name].append(firstLastNames[1:])
        elif len(nameSplitByComma) > 3:
            firstLastNames = nameSplitByComma[1] + " " + nameSplitByComma[0]
            firstLastNames.strip()
            updatedHistoriansNamesDict[name].append(firstLastNames)
        elif len(nameSplitByComma) > 1: #This is to check for names with more than 2 words long.
            firstNameSplitSpace = nameSplitByComma[1].split()
            if len(firstNameSplitSpace) > 1:
                firstLastNames = firstNameSplitSpace[0] + " " + nameSplitByComma[0]
                firstLastNames.strip()
                updatedHistoriansNamesDict[name].append(firstLastNames)

    with open(historianNamesUpdatedStorageJson, "w", encoding="utf-8") as jsonContent:
        json.dump(updatedHistoriansNamesDict, jsonContent, ensure_ascii=False, indent = 4)
    print("All dictionary exported to JSON.")

#This function is used to combine different specific error storage JSONs into one
def combineErrorStorageJSONs(individualJsonPathList, destinationJson):
    individualJsonDataList = []
    for individualJsonPath in individualJsonPathList:
        with open(individualJsonPath, "r", encoding="utf-8") as individualJsonContent:
            content = json.load(individualJsonContent)
            individualJsonDataList.append(content)
    mergedFinalJson = individualJsonDataList[0]
    for individualJsonContentIteration in individualJsonDataList[1:]:
        for key in individualJsonContentIteration:
            if key in mergedFinalJson:
                for sentence in individualJsonContentIteration[key]:
                    if sentence in mergedFinalJson[key]:
                        mergedFinalJson[key][sentence].extend(individualJsonContentIteration[key][sentence])
                    else:
                        mergedFinalJson[key][sentence] = individualJsonContentIteration[key][sentence]
            else:
                mergedFinalJson[key] = individualJsonContentIteration[key]
    with open(destinationJson, "w", encoding="utf-8") as storage:
        json.dump(mergedFinalJson, storage, indent=4)



if __name__=="__main__":
    csvFilePath = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/DoAHCSVContent.csv"
    JsonFilePathDestination = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/doahContentJSON.json"
    historianNamesJson = "/Users/Jerry/Desktop/DH proj-reading/DictionaryOfArtHistorians/doahGrammar/historianNames/historianNames.json"
    historianNamesUpdatedStorageJson = "/Users/Jerry/Desktop/DH proj-reading/DictionaryOfArtHistorians/doahGrammar/historianNames/historianNamesForComparison.json"
    # csvJson(csvFilePath, JsonFilePathDestination)
    # historianIDJSON(csvFilePath, historianNamesJson)
    # nameVariations(historianNamesJson, historianNamesUpdatedStorageJson)

    individualJsonErrorStorageList = [
        "/Users/Jerry/Desktop/DH proj-reading/DictionaryOfArtHistorians/doahGrammar/Backend/allErrorStorageJson/doahGrammarErrorStorage.json",
        "/Users/Jerry/Desktop/DH proj-reading/DictionaryOfArtHistorians/doahGrammar/Backend/allErrorStorageJson/historianNamesSpellingErrorStorage.json"
    ]
    destinationCombinedJsonErrorStorage = "/Users/Jerry/Desktop/DH proj-reading/DictionaryOfArtHistorians/doahGrammar/Backend/allErrorStorageJson/allCombinedErrorStorage.json"
    combineErrorStorageJSONs(individualJsonErrorStorageList, destinationCombinedJsonErrorStorage)