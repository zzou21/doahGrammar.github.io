import json
         #to do after 9/21/2024: finish interface and .correct() method by pulling error messages from doahGrammarErrorStorage.json and manipulating the content.

# This class objects takes in the message error storage and deploys the correction user interface.
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
                        #for errorCount in range(totalNumOfErrorsInt):
                        print(f"\n>>>>>>> New revision session:")
                        #print(f"Currently at error {errorCount + 1} of {totalNumOfErrorsInt}  errors in this revision iteration.")
                        print(f"------Sentence and error to revise------\n")
                        print(originalSentence)
                        print(checkLocationSentence)
                        print("\n")
                        print("------Revision Suggestions------\n")
                        for numberOfSuggestion, suggestedChange in enumerate(correctionRecommendations):
                            print(f"{numberOfSuggestion + 1} --- {suggestedChange}")
                        while True:
                            try:
                                userRevisionSelection = input("Select the revision number to implement. Only input numbers: ")
                                userSelectionRevisionSuggestionIndexInt = int(userRevisionSelection)
                                userSelectedRevisionChoiceString = correctionRecommendations[userSelectionRevisionSuggestionIndexInt - 1]
                            except ValueError:
                                print("Please type a numerical value.")
                            except IndexError:
                                print("Please type a numerical value provided above.")
                            else:
                                print(f"This works: {userSelectionRevisionSuggestionIndexInt}")
                                print(correctionRecommendations)

                                revisedSentence = originalSentence[:startSlice] + userSelectedRevisionChoiceString + " " + originalSentence[endSlice:]
                                print(f"Revised sentence->>{revisedSentence}")
            # TO DO from September 27: finish implementing the interface and store the corrected sentences in a dictionary. Add the feature where the user could take a break from editing. Add the feature if user doesn't see what they want to edit. Add the feature where the user wants to go back.
                                break



                        print(type(userRevisionSelection))
                        print(userRevisionSelection)

    def operations(self):
        self.readSentenceLevelErrorStorageAndDisplayInterface()

if __name__ == "__main__":
    errorMessageStorageJson = "/Users/Jerry/Desktop/DictionaryOfArtHistorians/doahGrammar/doahGrammarErrorStorage.json"
    sentenceLevelRevisionInterface = grammarCheckSentenceLevelRevisionInterface(errorMessageStorageJson)
    sentenceLevelRevisionInterface.operations()