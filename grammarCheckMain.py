import language_tool_python

sentence1 = "I is eating lunch."
sentence2 = "She were going to the market."
sentence3 = "They has completed their work."
# class grammarCheck:
#     def __init__(jsonFilePath, nameDictionary):

# def grammarChecker(sentence):
    
grammarChecker = language_tool_python.LanguageTool("en-US")
sentences = [sentence1, sentence2, sentence3]

for sentenceCount, sentenceToCheck in enumerate(sentences, start=1):
    results = grammarChecker.check(sentenceToCheck)
    print(f"Error for sentence # {sentenceCount} -- {sentenceToCheck}:")
    for individualError in results:
        print(f"RuleId: {individualError.replacements[0]}")

# for index in results:
#     print(f"ruleId: {index.ruleId}")
#     print(index)

# print(f"Length of the error is: {len(results)}")
# print(f"The full error is: {results}")
# print(f"First index is: {results[0][ruleId]}")
