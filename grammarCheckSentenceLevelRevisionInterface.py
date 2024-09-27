import json

class grammarCheckSentenceLevelRevisionInterface:
    def __init__ (self, errorMessageStorageJson):
        self.errorMessageStorageJson = errorMessageStorageJson

    def readSentenceLevelErrorStorageAndDisplayInterface(self):
        with open(self.errorMessageStorageJson, "r") as errorMessageStorageContent:
            errorMessageStorageOpenDict = json.load(errorMessageStorageContent)
        totalNumOfErrorsInt = sum([len(errorMessage) for errorMessageDict in errorMessageStorageOpenDict.values() for errorMessage in errorMessageDict.values() if errorMessage]) # this tracks how many total errors were stored in self.errorMessageStorageJson 

        for historian, errorMessageDict in errorMessageStorageOpenDict.items():
            print(historian)
            for originalSentence, errorMessage in errorMessageDict.items():
                if errorMessage:
                    for oneError in errorMessage:
                        print(f"This is errorMessage: {errorMessage}")
                        #errorMessage format: type - list; [startSlice, endSlide, ["suggestions for change"]]
                        startSlice = oneError[0]
                        endSlice = oneError[1]
                        correctionRecommendations = oneError[2]
                        checkLocationSentence = "".join([letter if startSlice <= count < endSlice else "." for count, letter in enumerate(originalSentence)])

                        #interface:
                        for errorCount in range(totalNumOfErrorsInt):
                            print(f"Currently at error {errorCount + 1} of {totalNumOfErrorsInt} total errors in this revision iteration.")
                            

                            print(checkLocationSentence)
                            print(originalSentence)
                            print(correctionRecommendations)

if __name__ == "__main__":
    errorMessageStorageJson = 