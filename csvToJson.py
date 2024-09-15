import pandas as pd, json, csv

def csvJson(csvFile, JsonFile):
    dictionaryDoAHContent = {} #format: {"name": [ID, "overview"]
    with open(csvFile, "r", encoding="utf-8") as csvContent:
        doahCSVContent = csv.reader(csvContent)
        for oneRowHistorian in doahCSVContent:
            try:
                historianID = int(oneRowHistorian[0])
                dictionaryDoAHContent[oneRowHistorian[1]] = [historianID, oneRowHistorian[2]]
            except ValueError: continue
    with open(JsonFile, "w", encoding="utf-8") as jsonFileDump:
        json.dump(dictionaryDoAHContent, jsonFileDump, ensure_ascii=False, indent=4)
    print("Converted to JSON.")

if __name__=="__main__":
    CsvFilePath = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/DoAHCSVContent.csv"
    JsonFilePathDestination = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/doahContentJSON.json"
    csvJson(CsvFilePath, JsonFilePathDestination)