import re

# int = 9
# for num in range(int):
#     print("hi")
#     print(num)

# word = "world"
# slice = word[2:4]
# word2 = "happy"

# for x in range(4):
#     print("this")
#     print(x)

testString = "As Freud experimented with psychoanalytic interpretation of art (his <em>Eine Kindheitserinnerung des Leonardo da Vinci</em>, 1910), Abraham did the same for Segantini in 1911, his book <em>Giovanni Segantini: ein psychoanalytischer Versuch</em>. At Harvard he met <a href=\"/barra\">Alfred H. Barr, Jr.</a>, who would become the first director of the Museum of Modern Art"

first = testString.find("<em>")
pattern = r"<em>(.*?)</em>|<a.*?>(.*?)</a>"
appearances = re.findall(pattern, testString)
print(appearances)
for word in appearances:
    print(f"word: {word}")
    xa, ya = word
    print(f"xa: {xa}")
    print(f"ya: {ya}")

    print(f"xa type: {type(xa)}")
    print(f"xa length: {len(xa)}")
    print(f"ya type: {type(ya)}")




# print(appearances)

string = "234567890"
print([string.index("345"), string.index("345") + len("345")])