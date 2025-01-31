'''
Jan 17, 2025
'''
import json, nltk, rapidfuzz

def processNamesDictionaryJson(nameJson):
    with open(nameJson, "r", encoding = "utf-8") as jsonContent:
        return jsonContent

def fuzzyLogicMatch(sampleText, nameJsonPath):
    nameDictionary = processNamesDictionaryJson(nameJsonPath)
    


if __name__ == "__main__":
    nameJsonDict = "/Users/Jerry/Desktop/DH proj-reading/DictionaryOfArtHistorians/doahGrammar/historianNames.json"
    sampleText = ""
    