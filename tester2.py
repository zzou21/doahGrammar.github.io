# import re
# from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline


# # int = 9
# # for num in range(int):
# #     print("hi")
# #     print(num)

# # word = "world"
# # slice = word[2:4]
# # word2 = "happy"

# # for x in range(4):
# #     print("this")
# #     print(x)

# testString = "As Freud experimented with psychoanalytic interpretation of art (his <em>Eine Kindheitserinnerung des Leonardo da Vinci</em>, 1910), Abraham did the same for Segantini in 1911, his book <em>Giovanni Segantini: ein psychoanalytischer Versuch</em>. At Harvard he met <a href=\"/barra\">Alfred H. Barr, Jr.</a>, who would become the first director of the Museum of Modern Art"
# print("Launching tokenizer and model")
# tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
# model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
# print("Launched tokenizer and model")
# print("Launching pipeline")

# NER = pipeline("ner", model=model, tokenizer=tokenizer)
# print("Launched pipeline")
# print("Performing NER")

# results = NER(testString)

# list = [{'entity': 'B-PER', 'score': 0.9986652, 'index': 2, 'word': 'Freud', 'start': 3, 'end': 8}, {'entity': 'B-MISC', 'score': 0.5987004, 'index': 17, 'word': 'Ein', 'start': 73, 'end': 76}, {'entity': 'I-MISC', 'score': 0.87417364, 'index': 18, 'word': '##e', 'start': 76, 'end': 77}, {'entity': 'I-MISC', 'score': 0.9568443, 'index': 19, 'word': 'Kind', 'start': 78, 'end': 82}, {'entity': 'I-MISC', 'score': 0.9785865, 'index': 20, 'word': '##he', 'start': 82, 'end': 84}, {'entity': 'I-MISC', 'score': 0.65624917, 'index': 21, 'word': '##its', 'start': 84, 'end': 87}, {'entity': 'I-MISC', 'score': 0.8529621, 'index': 23, 'word': '##nner', 'start': 90, 'end': 94}, {'entity': 'I-MISC', 'score': 0.84399796, 'index': 24, 'word': '##ung', 'start': 94, 'end': 97}, {'entity': 'B-PER', 'score': 0.98277515, 'index': 26, 'word': 'Leonardo', 'start': 102, 'end': 110}, {'entity': 'I-PER', 'score': 0.5050553, 'index': 27, 'word': 'da', 'start': 111, 'end': 113}, {'entity': 'I-MISC', 'score': 0.500737, 'index': 28, 'word': 'Vinci', 'start': 114, 'end': 119}, {'entity': 'B-PER', 'score': 0.9991972, 'index': 37, 'word': 'Abraham', 'start': 133, 'end': 140}, {'entity': 'B-PER', 'score': 0.99893624, 'index': 42, 'word': 'Sega', 'start': 158, 'end': 162}, {'entity': 'I-PER', 'score': 0.92881864, 'index': 43, 'word': '##ntin', 'start': 162, 'end': 166}, {'entity': 'I-PER', 'score': 0.4079361, 'index': 44, 'word': '##i', 'start': 166, 'end': 167}, {'entity': 'B-PER', 'score': 0.99860173, 'index': 53, 'word': 'Giovanni', 'start': 190, 'end': 198}, {'entity': 'I-PER', 'score': 0.9991186, 'index': 54, 'word': 'Sega', 'start': 199, 'end': 203}, {'entity': 'I-PER', 'score': 0.96075475, 'index': 55, 'word': '##ntin', 'start': 203, 'end': 207}, {'entity': 'I-MISC', 'score': 0.7759309, 'index': 65, 'word': '##cher', 'start': 228, 'end': 232}, {'entity': 'I-MISC', 'score': 0.8635601, 'index': 66, 'word': 'V', 'start': 233, 'end': 234}, {'entity': 'I-MISC', 'score': 0.9667936, 'index': 67, 'word': '##ers', 'start': 234, 'end': 237}, {'entity': 'I-MISC', 'score': 0.5841619, 'index': 68, 'word': '##uch', 'start': 237, 'end': 240}, {'entity': 'B-ORG', 'score': 0.9391334, 'index': 75, 'word': 'Harvard', 'start': 250, 'end': 257}, {'entity': 'B-PER', 'score': 0.9992143, 'index': 90, 'word': 'Alfred', 'start': 282, 'end': 288}, {'entity': 'I-PER', 'score': 0.99347997, 'index': 91, 'word': 'H', 'start': 289, 'end': 290}, {'entity': 'I-PER', 'score': 0.9843045, 'index': 92, 'word': '.', 'start': 290, 'end': 291}, {'entity': 'I-PER', 'score': 0.9995372, 'index': 93, 'word': 'Barr', 'start': 292, 'end': 296}, {'entity': 'I-PER', 'score': 0.50140476, 'index': 94, 'word': ',', 'start': 296, 'end': 297}, {'entity': 'I-PER', 'score': 0.9885129, 'index': 95, 'word': 'Jr', 'start': 298, 'end': 300}, {'entity': 'B-ORG', 'score': 0.9926399, 'index': 110, 'word': 'Museum', 'start': 350, 'end': 356}, {'entity': 'I-ORG', 'score': 0.988641, 'index': 111, 'word': 'of', 'start': 357, 'end': 359}, {'entity': 'I-ORG', 'score': 0.98948365, 'index': 112, 'word': 'Modern', 'start': 360, 'end': 366}, {'entity': 'I-ORG', 'score': 0.983452, 'index': 113, 'word': 'Art', 'start': 367, 'end': 370}]


# for dictionary in list:
#     print(dictionary)

# lst = [(9, 0), (3, 4), (5, 6)]
# print(range(1, len(lst) + 1))

# if 4 in range(1, len(lst) + 1):
#     print("yes")

import re

def split_sentence(sentence):
    result = []
    # Use regex to find words along with their start and end indices
    for match in re.finditer(r'\S+', sentence):
        start = match.start()
        end = match.end()
        word = match.group()
        result.append([start, end, word])
    return result

# Example usage
sentence = "I like this this room"
output = split_sentence(sentence)
print(output)
