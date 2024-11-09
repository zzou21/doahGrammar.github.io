import json
         #to do after 9/21/2024: finish interface and .correct() method by pulling error messages from doahGrammarErrorStorage.json and manipulating the content.

# This class objects takes in the message error storage and deploys the correction user interface.
class grammarCheckSentenceLevelRevisionInterface:
    def __init__ (self, errorMessageStorageJson):
        self.errorMessageStorageJson = errorMessageStorageJson
        self.storageOfCorrectedWriting = {}
        self.totalNumOfErrorsInt = 0  # this tracks how many total errors
    
    def readSentenceLevelErrorStorageJson(self, jsonErrorStorageFileToOpen): # This function opens the JSON file that stores the error messages
        with open(jsonErrorStorageFileToOpen, "r") as errorMessageStorageContent:
            errorMessageStorageOpenDict = json.load(errorMessageStorageContent)
        self.totalNumOfErrorsInt = sum([len(errorMessage) for errorMessageDict in errorMessageStorageOpenDict.values() for errorMessage in errorMessageDict.values() if errorMessage]) # this tracks how many total errors

        return errorMessageStorageOpenDict

    def displayInterface(self):
        outerDictionaryList0thIndexHistorian = self.turnDictToMultiList(self.readSentenceLevelErrorStorageJson(self.errorMessageStorageJson))  #Data structure: [[historian, [[sentence, [[startSlice, endSlice, [correctionSuggestion]]]], [sentence, []]], [historian, [[sentence, [error]], [sentence, [error]]]].
        
        '''--------
        Udpates from Nov 8, 2024:
        stopped using a dictionary as an iterator. changed to multi-layer nested list stored in "outerDictionaryList0thIndexHistorian". Run and print "outerDictionaryList0thIndexHistorian" before next edit. We are using a list format so that we could for loop index iteration through it to ensure that we could implement the function of going back to a previous error check.
        
        Rewrite the iterators below according to the multi-layer nested list format rather than a nested dictionary.
        '''
        totalErrorsRemaining = self.totalNumOfErrorsInt
        errorsCorrectedInOneSessionCount = 0
        print(f"--------Begins Error Correction Interface--------\n\n")
        for historianIndex in range(len(outerDictionaryList0thIndexHistorian)): # "historianIndex" tracks which historian the user is currently iterating through. Format for outerDictionaryList0thIndexHistorian[historianIndex]: ["Name, Historian", [["sentence", ["errors"]], ["sentence", ["errors"]]]
            historianBeingEditedString = outerDictionaryList0thIndexHistorian[historianIndex][0]
            # print(f"Currently editing the entry for: {historianBeingEditedString}")
            if outerDictionaryList0thIndexHistorian[historianIndex][0] not in self.storageOfCorrectedWriting:
                self.storageOfCorrectedWriting[historianBeingEditedString] = []
            temporaryHistorianEntryContentPointer = outerDictionaryList0thIndexHistorian[historianIndex][1]
            for sentenceErrorPairListIndex in range(len(temporaryHistorianEntryContentPointer)):
                #print(f"each sentence error pair: {temporaryHistorianEntryContentPointer[sentenceErrorPairListIndex]}")
                originalSentence = temporaryHistorianEntryContentPointer[sentenceErrorPairListIndex][0]
                errorMessageList = temporaryHistorianEntryContentPointer[sentenceErrorPairListIndex][1]
                if errorMessageList:
                    # print(f"error message list: {errorMessageList}")
                    for errorMessageIndex in range(len(errorMessageList)): #errorMessageIndex format: type - list; [startSlice, endSlide, ["suggestions for change"]]
                        # print(f"One error: {errorMessageList[errorMessageIndex]}")
                        temporaryStorageOneErrorList = errorMessageList[errorMessageIndex] #temporaryStorageOneErrorList format: type - list; [startSlice, endSlide, ["suggestions for change"]]
                        # print(f"This is error message: {temporaryStorageOneErrorList}")
                        startSlice = temporaryStorageOneErrorList[0]
                        endSlice = temporaryStorageOneErrorList[1]
                        correctionRecommendations = temporaryStorageOneErrorList[2]
                        checkErrorLocationInOriginalSentenceString = "".join([letter if startSlice <= letterIndexCount < endSlice else "." for letterIndexCount, letter in enumerate(originalSentence)])

                        #Start of interface
                        print(f"Number of errors at th beginning of session: {totalErrorsRemaining}")
                        # while totalErrorsRemaining > 0:
                        print(f"\n\n>>>>>> New Error Correction Window. Corrected {errorsCorrectedInOneSessionCount} errors in this session.")
                        print(f"Remaining errors to correct: {totalErrorsRemaining}")
                        print(f"---------Sentence and error to correct---------")
                        print(originalSentence)
                        print(checkErrorLocationInOriginalSentenceString)
                        print(f"Revision Recommendations:")
                        for countOfRecommendation, revisionRecommendation in enumerate(correctionRecommendations):
                            print(f"{countOfRecommendation + 1} ---- {revisionRecommendation}")
                        while True:
                            try:
                                userSelectionOfRecommendationIndex = int(input("Select the revision number to implement. Only input numbers: "))
                                userSelectionOfRecommendationContentString = revisionRecommendation[userSelectionOfRecommendationIndex]
                            except ValueError:
                                print(f"Please type a numerical value.")
                            except IndexError:
                                print(f"Please type a number listed above.")
                            else:
                                revisedSentence = originalSentence[:startSlice] + userSelectionOfRecommendationContentString + " " + originalSentence[endSlice:]
                                print(f"Revised sentence->>\n{revisedSentence}")
                                break
                            
                        totalErrorsRemaining -= 1
                        errorsCorrectedInOneSessionCount += 1
                        print(f"All errors corrected.")
                        # print(f"while loop count: {whileLoopCount}")

        # for historian, errorMessageDict in errorMessageStorageOpenDict.items():
        #     if historian not in self.storageOfCorrectedWriting:
        #         self.storageOfCorrectedWriting[historian] = []
        #     for originalSentence, errorMessage in errorMessageDict.items():
        #         if errorMessage:
        #             for oneError in errorMessage:
        #                 print(f"This is errorMessage: {errorMessage}")
        #                 #errorMessage format: type - list; [startSlice, endSlide, ["suggestions for change"]]
        #                 startSlice = oneError[0]
        #                 endSlice = oneError[1]
        #                 correctionRecommendations = oneError[2]
        #                 checkLocationSentence = "".join([letter if startSlice <= count < endSlice else "." for count, letter in enumerate(originalSentence)])

        #                 #interface:
        #                 #for errorCount in range(totalNumOfErrorsInt):
        #                 print(f"\n>>>>>>> New revision session:")
        #                 #print(f"Currently at error {errorCount + 1} of {totalNumOfErrorsInt}  errors in this revision iteration.")
        #                 print(f"------Sentence and error to revise------\n")
        #                 print(originalSentence)
        #                 print(checkLocationSentence)
        #                 print("\n")
        #                 print("------Revision Suggestions------\n")
        #                 for numberOfSuggestion, suggestedChange in enumerate(correctionRecommendations):
        #                     print(f"{numberOfSuggestion + 1} --- {suggestedChange}")
        #                 while True:
        #                     try:
        #                         userRevisionSelection = input("Select the revision number to implement. Only input numbers: ")
                                
        #                         userSelectionRevisionSuggestionIndexInt = int(userRevisionSelection)
        #                         userSelectedRevisionChoiceString = correctionRecommendations[userSelectionRevisionSuggestionIndexInt - 1]
        #                     except ValueError:
        #                         print("Please type a numerical value.")
        #                     except IndexError:
        #                         print("Please type a numerical value provided above.")
        #                     else:
        #                         print(f"This works: {userSelectionRevisionSuggestionIndexInt}")
        #                         print(correctionRecommendations)

        #                         revisedSentence = originalSentence[:startSlice] + userSelectedRevisionChoiceString + " " + originalSentence[endSlice:]
        #                         print(f"Revised sentence->>{revisedSentence}")
        #                         # TO DO from September 27: finish implementing the interface and store the corrected sentences in a dictionary. Add the feature where the user could take a break from editing. Add the feature if user doesn't see what they want to edit. Add the feature where the user wants to go back.
        #                         break
        #                 print(type(userRevisionSelection))
        #                 print(userRevisionSelection)

        #         else:
        #             self.storageOfCorrectedWriting[historian].append(originalSentence)

    def turnDictToMultiList(self, errorMessageStorageOpenDict):
        outerDictionaryTuple0thIndexHistorian = list(errorMessageStorageOpenDict.items()) #[(historian, {content}), (historian, {content})]
        outerDictionaryList0thIndexHistorian = [list(pair) for pair in outerDictionaryTuple0thIndexHistorian] #[[historian, {content}], [historian, {content}]]
        for index in range(len(outerDictionaryList0thIndexHistorian)):
            outerDictionaryList0thIndexHistorian[index][1] = [list(pair) for pair in list(outerDictionaryList0thIndexHistorian[index][1].items())]
        return outerDictionaryList0thIndexHistorian

    def operations(self):
        self.displayInterface()

if __name__ == "__main__":
    #errorMessageStorageJson = "/Users/Jerry/Desktop/DH proj-reading/DictionaryOfArtHistorians/doahGrammar/doahGrammarErrorStorage.json"
    errorMessageStorageJson = "C:/Users/zz341/Desktop/doahGrammar/doahGrammarErrorStorage.json"

    sentenceLevelRevisionInterface = grammarCheckSentenceLevelRevisionInterface(errorMessageStorageJson)
    sentenceLevelRevisionInterface.operations()