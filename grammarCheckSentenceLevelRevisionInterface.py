import json

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
        revisedContentStorageDictionary = {}
        totalErrorsRemaining = self.totalNumOfErrorsInt
        errorsCorrectedInOneSessionCount = 0
        print(f"--------Begins Error Correction Interface--------\n\n")
        for historianIndex in range(len(outerDictionaryList0thIndexHistorian)): # "historianIndex" tracks which historian the user is currently iterating through. Format for outerDictionaryList0thIndexHistorian[historianIndex]: ["Name, Historian", [["sentence", ["errors"]], ["sentence", ["errors"]]]
            historianBeingEditedString = outerDictionaryList0thIndexHistorian[historianIndex][0]
            # print(f"Currently editing the entry for: {historianBeingEditedString}")
            if outerDictionaryList0thIndexHistorian[historianIndex][0] not in revisedContentStorageDictionary:
                revisedContentStorageDictionary[historianBeingEditedString] = []
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
                        correctionRecommendationsList = temporaryStorageOneErrorList[2]
                        checkErrorLocationInOriginalSentenceString = "".join([letter if startSlice <= letterIndexCount < endSlice else "." for letterIndexCount, letter in enumerate(originalSentence)])

                        #Start of interface
                        print(f"Number of errors at th beginning of session: {totalErrorsRemaining}")
                        print(f"\n\n>>>>>> New Error Correction Window. Corrected {errorsCorrectedInOneSessionCount} errors in this session.")
                        print(f"Remaining errors to correct: {totalErrorsRemaining}")
                        print(f"---------Sentence and error to correct---------")
                        print(originalSentence)
                        print(checkErrorLocationInOriginalSentenceString)
                        print(f"Revision Recommendations:")
                        for countOfRecommendation, revisionRecommendationString in enumerate(correctionRecommendationsList):
                            print(f"{countOfRecommendation + 1} ---- {revisionRecommendationString}")
                        
                        class emptySelectionError(Exception): # To prevent users from selecting a number not provided
                            pass
                        class returnToPrevious(Exception): # This triggers interface to return to a previous error message display
                            pass
                        class manualEdit(Exception): # This triggers interface to allow users to manually enter an edit
                            pass
                        class quitEditing(Exception): # This allows users to exit the interface
                            pass

                        while True:
                            try:
                                userSelectionOfRecommendationIndex = input("Select the revision number to implement by inputting ONLY numbers. \nTo return to a previous revision, type 'up'\nTo manually enter an edit, type 'edit'\nTo save progress and quit, type 'quit': ")
                                if userSelectionOfRecommendationIndex not in range(1, len(correctionRecommendationsList) + 1):
                                    raise emptySelectionError
                                if userSelectionOfRecommendationIndex == "up":
                                    raise returnToPrevious
                                if userSelectionOfRecommendationIndex == "edit":
                                    raise manualEdit
                                if userSelectionOfRecommendationIndex == "quit":
                                    raise quitEditing
                                userSelectionOfRecommendationContentString = correctionRecommendationsList[userSelectionOfRecommendationIndex - 1]
                            except ValueError:
                                print(f"Please type a numerical value.")
                            except IndexError:
                                print(f"Please type a numerical selection listed above.")
                            except emptySelectionError:
                                print(f"Please type a numerical selection listed above.")
                            except returnToPrevious: # TODO in progress 11/9/2024
                                if totalErrorsRemaining == self.totalNumOfErrorsInt:
                                    print("This is the first error being corrected.")
                                # else:
                                # TODO in progress 11/9/2024 
                                    
                            except manualEdit:# TODO in progress 11/9/2024
                                pass
                            except quitEditing:# TODO in progress 11/9/2024
                                pass #placeholder. Function in progress
                            else:
                                revisedSentence = originalSentence[:startSlice] + userSelectionOfRecommendationContentString + " " + originalSentence[endSlice:]
                                print(f"Revised sentence->>\n{revisedSentence}")
                                revisedContentStorageDictionary[historianBeingEditedString].append(revisedSentence)
                                break
                        
                        totalErrorsRemaining -= 1
                        errorsCorrectedInOneSessionCount += 1
                else:
                    revisedContentStorageDictionary[historianBeingEditedString].append(originalSentence)

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