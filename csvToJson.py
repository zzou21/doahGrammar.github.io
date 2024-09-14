import pandas as pd
import json

#test

def csvJson(csvFile, JsonFile):
    dictionaryDoAHContent = {}
    doahContentDF = pd.read_csv(csvFile)
    for i in range(len(doahContentDF)):
        oneRowContent = tuple(doahContentDF.loc[i].values)
        dictionaryDoAHContent[oneRowContent[:2]] = oneRowContent[2]
    print(dictionaryDoAHContent)


    
    # with open(JsonFile, "w") as jsonFileDump:
    #     json.dump(dictionaryDoAHContent, jsonFileDump, indnet=4)
    print("Converted to JSON.")




if __name__=="__main__":
    CsvFilePath = "/Users/Jerry/Desktop/Dictionary of Art Historians/doahGrammar/Art-Historians-Export-2024-September-10-1339.csv"
    JsonFilePathDestination = "/Users/Jerry/Desktop/Dictionary of Art Historians/GrammarCheckerDoAH/DoahContent.json"
    print(csvJson(CsvFilePath, JsonFilePathDestination))
    