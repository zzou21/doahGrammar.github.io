'''
Jan 17, 2025
'''
import json, nltk, rapidfuzz

class nameSpellingCheck:
    def __init__(self, nameJsonPath, sampleTextJsonPath):
        self.nameJsonPath = nameJsonPath
        self.sampleTextJsonPath = sampleTextJsonPath

    def processNamesDictionaryJson(self, nameJsonFilePath):
        with open(nameJsonFilePath, "r", encoding = "utf-8") as jsonContent:
            return jsonContent

    def fuzzyLogicMatch(self):
        nameDictionary = self.processNamesDictionaryJson(self.nameJsonPath)
        print(nameDictionary)
    
    def operations(self):
        self.fuzzyLogicMatch()


if __name__ == "__main__":
    nameJsonDict = "/Users/Jerry/Desktop/DH proj-reading/DictionaryOfArtHistorians/doahGrammar/historianNames.json"
    sampleText = "/Users/Jerry/Desktop/DH proj-reading/DictionaryOfArtHistorians/doahGrammar/unfinishedRevisedDictionaryErrors2024-11-22.json"
    nameSpellingCheckMachine = nameSpellingCheck(nameJsonDict, sampleText)
    nameSpellingCheckMachine.operations()