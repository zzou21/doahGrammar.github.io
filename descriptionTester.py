import language_tool_python
from nltk.tokenize import PunktSentenceTokenizer

description = "Americanist art historian; first associate director of the Museum of Modern Art in New York. Abbott was born to Arthur Abbott and Flora Parkman (Abbott). After attending Dexter High School, Abbott graduated from Bowdin College with a bachelor's degree in science and attended graduate school at Harvard University in physics. At Harvard he met <a href=\"/barra\">Alfred H. Barr, Jr.</a>, who would become the first director of the Museum of Modern Art. Barr and Abbott spent time in Paris studying art. Barr appointed Abbott to be his first associate director, taking care of much of the day-to-day operations of the museum. In 1932 Abbott accepted a position as Director, Smith College Museum of Art, Northampton, Massachusetts where he remained until 1946. As director, Abbott was instrumental in acquiring modernist works such as Picasso's cubist <em>Table, Guitar, and Bottle</em> (1919) as he had done for the Museum of Modern Art. He was adjunct faculty at Smith and taught courses in art history. He was a fellow of the Pierpont Morgan Library in New York. After his retirement from Smith, Abbott moved to his hometown of Dexter, Maine, where his family operated the Amos Abbott Woolen Manufacturing Company. Abbott served as the treasurer for the Company. At his death, Abbott left a $4.3-million acquisition fund to the Colby College Museum of Art."

sentSegmentator = PunktSentenceTokenizer()
segmentationResult = sentSegmentator.tokenize(description)

for e in segmentationResult:
    print(e)
