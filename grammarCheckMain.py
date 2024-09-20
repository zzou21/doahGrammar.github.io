import language_tool_python, json
from nltk.tokenize import PunktSentenceTokenizer

# TO DO: do not forget to add work batch during interface design, so that the system automatically updates the correct dictionary routinely because the user cannot check all errors in one sitting. Could update the correct version dictionary after checking each historian's overview.

# json format: dictionary - {"lastName, firstName": [id, "description"]}

# # For testing purposes:
# sentence1 = "I is eating lunch."
# sentence2 = "She were going to the market."
# sentence3 = "They has completed their work."

class grammarCheckSentenceLevel:
    def __init__(self, jsonFilePath, nameDictionary, doAHContentSentSegmentedJsonFile):
        self.jsonFilePath = jsonFilePath
        self.nameDict = nameDictionary
        self.doAHContentSentSegmentedJsonFile = doAHContentSentSegmentedJsonFile

        self.DoAHJsonContentDict = None
        self.DoAHSentSegDict = {} # This dictionary stores the DoAH content that has been sentence-segmented. Format: {"lastName, firstName": [id, "sentence-segmented description"]}

    def processJson(self):
        with open(self.jsonFilePath, "r", encoding = "utf-8") as jsonContent:
            self.DoAHJsonContentDict = json.load(jsonContent)
    
    def sentenceSegmentation(self):
        sentSegmentator = PunktSentenceTokenizer()
        for historianString, IdOverviewList in self.DoAHJsonContentDict.items():
            historianIdInt = IdOverviewList[0]
            historianOverviewString = IdOverviewList[1]
            segmentationResult = sentSegmentator.tokenize(historianOverviewString)
            singleHistorianSentSegList = [singleSentence for singleSentence in segmentationResult]
            # print(singleHistorianSentSeg)
            self.DoAHSentSegDict[historianString] = [historianIdInt, singleHistorianSentSegList]
            
        # with open(self.doAHContentSentSegmentedJsonFile, "w", encoding="utf-8") as jsonSegContent:
            # json.dump(self.DoAHSentSegDict, jsonSegContent, ensure_ascii=False, indent = 4)
    
    # This function and interface check grammar and errors at the sentence-level, using historian overviews that have been sentence-segmented from the "sentenceSegmentation" function.

    def sentenceGrammarCheck(self):
        correctedVersion = {}
        grammarCheckerFunction = language_tool_python.LanguageTool("en-US")
        for historian, IdOverviewSegmentedList in self.DoAHSentSegDict.items():
            for Id, segmentedOverview in IdOverviewSegmentedList:
                sentenceCounter = 1
                for sentenceToCheck in segmentedOverview:
                    grammarCheckResults = grammarCheckerFunction.check(sentenceToCheck)
                    for errors in grammarCheckResults:
                        startSlice = errors.offset
                        endSlice = errors.offset+errors.errorLength+1
                        checkLocationSentence = "".join([letter if startSlice <= count < endSlice else "." for count, letter in enumerate(sentenceToCheck)])
                        print(errors.replacements)
                        print(f"Error sentence: {sentenceToCheck}")
                        print(f"Error location: {checkLocationSentence}")
                    

    # This helper function is mainly used during code testing to run the entire class object:
    def operations(self):
        self.processJson()
        # self.sentenceSegmentation()


# class errorCheckWordLevel:
#     def __init__(self, ):

if __name__ == "__main__":
    doAHContentJsonFile = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/doahContentJSON.json"
    nameDictionary = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/historianNames.json"
    doAHContentSentSegmentedJsonFile = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/doahContentSentSegmentedJSON.json"
    smallScaleTestJson = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/smalldoahContentSentSegPractice.json"
    grammarCheckSentenceLevelMachine = grammarCheckSentenceLevel(smallScaleTestJson, nameDictionary, doAHContentSentSegmentedJsonFile)
    grammarCheckSentenceLevelMachine.operations()
    # print(grammarCheckSentenceLevelMachine.DoAHSentSegDict)

#-----------------

# grammarChecker = language_tool_python.LanguageTool("en-US")
# sentences = [sentence1, sentence2, sentence3]

# for sentenceCount, sentenceToCheck in enumerate(sentences, start=1):
#     results = grammarChecker.check(sentenceToCheck)
#     print(f"Error for sentence # {sentenceCount} -- {sentenceToCheck}:")
#     for individualError in results:
#         print(f"RuleId: {individualError.replacements[0]}")