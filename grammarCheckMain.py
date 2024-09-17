import language_tool_python, json
from nltk.tokenize import PunktSentenceTokenizer

# json format: dictionary - {"lastName, firstName": [id, "description"]}

sentence1 = "I is eating lunch."
sentence2 = "She were going to the market."
sentence3 = "They has completed their work."
class grammarCheck:
    def __init__(self, jsonFilePath, nameDictionary):
        self.jsonFilePath = jsonFilePath
        self.nameDict = nameDictionary
        self.DoAHJsonContentDict = None
        self.DoAHSentSegDict = {}

    def processJson(self):
        with open(self.jsonFilePath, "r") as jsonContent:
            self.DoAHJsonContentDict = json.load(jsonContent)
    
    def sentenceSegmentation(self):
        sentSegmentator = PunktSentenceTokenizer()
        for historianString, IdOverviewList in self.DoAHJsonContentDict.items():
            segmentationResult = sentSegmentator.tokenize(IdOverviewList[1])
            singleHistorianSentSeg = [singleSentence for singleSentence in segmentationResult]

if __name__ == "__main__":
    jsonFile = ""
    nameDictionary = ""
    grammarCheckMachine = grammarCheck(jsonFile, nameDictionary)
    print

#-----------------

grammarChecker = language_tool_python.LanguageTool("en-US")
sentences = [sentence1, sentence2, sentence3]

for sentenceCount, sentenceToCheck in enumerate(sentences, start=1):
    results = grammarChecker.check(sentenceToCheck)
    print(f"Error for sentence # {sentenceCount} -- {sentenceToCheck}:")
    for individualError in results:
        print(f"RuleId: {individualError.replacements[0]}")