import json, language_tool_python
from nltk.tokenize import PunktSentenceTokenizer
from langdetect import detect, LangDetectException
import re

class errorCheckWordLevel:
    def __init__(self, jsonFilePath, nameDictionary, errorMessageStorageJson, doAHContentSentSegmentedJsonFile):
        self.jsonFilePath = jsonFilePath
        self.nameDict = nameDictionary
        self.errorMessageStorageJson = errorMessageStorageJson
        self.doAHContentSentSegmentedJsonFile = doAHContentSentSegmentedJsonFile
        self.DoAHJsonContentDict = None
        self.DoAHSentSegDict = {}
        self.foreignLanguage = "en" #default language is English.

    def processJson(self):
        with open(self.jsonFilePath, "r", encoding="utf-8") as jsonContent:
            self.DoAHJsonContentDict = json.load(jsonContent)
    
    def sentenceSegmentation(self):
        sentSegmentator = PunktSentenceTokenizer()
        for historianString, IdOverviewList in self.DoAHJsonContentDict.items():
            historianIdInt = IdOverviewList[0]
            historianOverviewString = IdOverviewList[1]
            segmentationResult = sentSegmentator.tokenize(historianOverviewString)
            singleHistorianSentSegList = [singleSentence for singleSentence in segmentationResult]
            self.DoAHSentSegDict[historianString] = [historianIdInt, singleHistorianSentSegList]

    def isForeign(self, word):
        try:
            detectedlanguage = detect(word) #check lang
            return detectedlanguage != self.foreignLanguage #is it not english?
        except:
            return False #the language is english.
        
    

        

