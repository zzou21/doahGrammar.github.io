import language_tool_python, json
from nltk.tokenize import PunktSentenceTokenizer

# TO DO: do not forget to add work batch during interface design, so that the system automatically updates the correct dictionary routinely because the user cannot check all errors in one sitting. Could update the correct version dictionary after checking each historian's overview.

# json format: dictionary - {"lastName, firstName": [id, "description"]}
# language_tool_python error output example:
    # output = [Match({'ruleId': 'PERS_PRONOUN_AGREEMENT', 'message': 'Did you mean “am” or “will be”?', 'replacements': ['am', 'will be'], 'offsetInContext': 2, 'context': 'I is eating lunch.', 'offset': 2, 'errorLength': 2, 'category': 'GRAMMAR', 'ruleIssueType': 'grammar', 'sentence': 'I is eating lunch.'})]
    # access specific information through: output.message

class grammarCheckSentenceLevelPreparationForErrorMessageStorage:
    def __init__(self, jsonFilePathUnsegmented, nameDictionary, errorMessageStorageJson, doAHContentSentSegmentedJsonFile):
        self.jsonFilePathUnsegmented = jsonFilePathUnsegmented
        self.nameDict = nameDictionary
        self.errorMessageStorageJson = errorMessageStorageJson
        self.doAHContentSentSegmentedJsonFile = doAHContentSentSegmentedJsonFile
        self.DoAHJsonContentDict = None
        self.DoAHSentSegDict = {} # This dictionary stores the DoAH content that has been sentence-segmented. Format: {"lastName, firstName": [id, "sentence-segmented description"]}
        self.errorMessageStorageWithSentenceDict = {} #This dictionary holds the corrected list of sentences to be dumped into a new JSON. Format: {"historian name": {"sentence": [startSlicingIndex, endSlicingIndex, [suggested changes]}}. If a sentence has no error: {"historian name": {"sentence": []}}

    def processJsonUnsegmented(self):
        with open(self.jsonFilePathUnsegmented, "r", encoding = "utf-8") as jsonContent:
            self.DoAHJsonContentDict = json.load(jsonContent)

    def processJsonSegmented(self):
        with open(self.doAHContentSentSegmentedJsonFile, "r", encoding = "utf-8") as jsonContent:
            self.DoAHSentSegDict = json.load(jsonContent)
    
    def sentenceSegmentation(self):
        sentSegmentator = PunktSentenceTokenizer()
        for historianString, IdOverviewList in self.DoAHJsonContentDict.items():
            historianIdInt = IdOverviewList[0]
            historianOverviewString = IdOverviewList[1]
            segmentationResult = sentSegmentator.tokenize(historianOverviewString)
            singleHistorianSentSegList = [singleSentence for singleSentence in segmentationResult]
            # print(singleHistorianSentSeg)
            # self.DoAHSentSegDict[historianString] = [historianIdInt, singleHistorianSentSegList]
            self.DoAHSentSegDict[historianString] = singleHistorianSentSegList

        with open(self.doAHContentSentSegmentedJsonFile, "w", encoding="utf-8") as jsonSegContent:
            json.dump(self.DoAHSentSegDict, jsonSegContent, ensure_ascii=False, indent = 4)

    # This function and interface check grammar and errors at the sentence-level, using historian overviews that have been sentence-segmented from the "sentenceSegmentation" function.
    def sentenceGrammarCheck(self):
        grammarCheckerFunction = language_tool_python.LanguageTool("en-US")
        print(self.DoAHSentSegDict)
        for historian, IdOverviewSegmentedList in self.DoAHSentSegDict.items():
            sentenceCheckedForEachHistorianDict = {}
            for sentenceToCheck in IdOverviewSegmentedList:
                # for sentenceToCheck in segmentedOverview:
                print(sentenceToCheck)
                grammarCheckResults = grammarCheckerFunction.check(sentenceToCheck)
                sentenceCheckedForEachHistorianDict[sentenceToCheck] = []
                if grammarCheckResults:
                    errorMessageAndOffsetHolderList = []

                    for errors in grammarCheckResults:
                        startSlice = errors.offset
                        endSlice = errors.offset+errors.errorLength+1
                        checkLocationSentence = "".join([letter if startSlice <= count < endSlice else "." for count, letter in enumerate(sentenceToCheck)])
                        correctionSuggestions = errors.replacements[:6] if len(errors.replacements) > 6 else errors.replacements
                        errorMessageAndOffsetHolderList.append([startSlice, endSlice, correctionSuggestions])
                        print(f"For the entry for the historian {historian}: ")
                        print(f"Error sentence: {sentenceToCheck}")
                        print(f"Error location: {checkLocationSentence}")
                        print(f"The possible replacements are: {errors.replacements}")
                        print(f"Error list: {errorMessageAndOffsetHolderList}")
                        
                    sentenceCheckedForEachHistorianDict[sentenceToCheck] = errorMessageAndOffsetHolderList

                else: sentenceCheckedForEachHistorianDict[sentenceToCheck] = []

            self.errorMessageStorageWithSentenceDict[historian] = sentenceCheckedForEachHistorianDict

        with open(self.errorMessageStorageJson, "w", encoding="utf-8") as file:
            json.dump(self.errorMessageStorageWithSentenceDict, file, ensure_ascii=False, indent=4)

         #to do after 9/21/2024: finish interface and .correct() method by pulling error messages from doahGrammarErrorStorage.json and manipulating the content.
                    
    # This helper function is mainly used during code testing to run the entire class object:
    def operations(self):
        # self.processJsonUnsegmented()
        # self.processJsonSegmented()
        # self.sentenceSegmentation()
        # self.sentenceGrammarCheck()
        self.readSentenceLevelErrorStorageAndDisplayInterface()

if __name__ == "__main__":
    doAHContentJsonFile = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/doahContentJSON.json"
    nameDictionary = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/historianNames.json"

    doAHContentSentSegmentedJsonFile = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/doahContentSentSegmentedJSON.json"
    # doAHContentSentSegmentedJsonFile = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/smalldoahContentSegmentedWithoutIDNumber.json"

    smallScaleTestJson = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/smalldoahContentSegmentedWithoutIDNumber.json"
    errorMessageStorage = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/doahGrammarErrorStorage.json"

    grammarCheckSentenceLevelMachine = grammarCheckSentenceLevelPreparationForErrorMessageStorage(doAHContentJsonFile, nameDictionary, errorMessageStorage, smallScaleTestJson)

    grammarCheckSentenceLevelMachine.operations()
    print(grammarCheckSentenceLevelMachine.errorMessageStorageWithSentenceDict)

#-----------------

# grammarChecker = language_tool_python.LanguageTool("en-US")
# sentences = [sentence1, sentence2, sentence3]

# for sentenceCount, sentenceToCheck in enumerate(sentences, start=1):
#     results = grammarChecker.check(sentenceToCheck)
#     print(f"Error for sentence # {sentenceCount} -- {sentenceToCheck}:")
#     for individualError in results:
#         print(f"RuleId: {individualError.replacements[0]}")