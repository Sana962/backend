import re
import string
from PreprocessingOnQuery import PreProcessQuery

import bs4 as bs
import requests
from autocorrect import spell
from googlesearch import search

class FetchUrl:

    def __init__(self, query, template):      #constuctor #self refering to instance of object like this in java
        self.query = query
        self.template = template

    def removeEmptySpaces(array):

        arr = list(filter(str.strip, array))
        return arr

    def removeDigits(array):

        pattern = '[0-9]'
        arr = [re.sub(pattern, '', i) for i in array]
        return arr

    def removePunctuation(array):

       arr = ["".join( j for j in i if j not in string.punctuation) for i in array]
       return arr

    def removeStringWithCertainWord(array):
        keywordFilter = ['Let', 'Tutorial', '...', '?','let', 'tutorial', ':', 'article']
        result = [sent for sent in array
                if not any(word in sent for word in keywordFilter)]
        return result

    def fetchDataSet(self):
        Template = self.template
        query = self.query
        obj = PreProcessQuery(self.query)
        self.pattern = obj.getPattern()

        if Template == 'Medium':
            Mediumquery1 = query
            ArryofUrlMediumQuery1 = []
            for FetchedUrl in search(Mediumquery1, tld='com', lang='en', stop=5, pause=2.0):
                ArryofUrlMediumQuery1.append(FetchedUrl)

            ArrayofMediumSentencesQuery1 = []

            for i in ArryofUrlMediumQuery1:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p']):
                    ArrayofMediumSentencesQuery1.append(content.text)

                NullFreeArrayofMediumSentencesQuery1 = FetchUrl.removeEmptySpaces(ArrayofMediumSentencesQuery1)
                DigitFreeArrayofMediumSentencesQuery1 = FetchUrl.removeDigits(NullFreeArrayofMediumSentencesQuery1)
                PunctuationFreeArrayofMediumSentencesQuery1 = FetchUrl.removePunctuation(DigitFreeArrayofMediumSentencesQuery1)

            Mediumquery2 = Mediumquery1 + 'what are its advantages and Disadvantages?'
            ArryofUrlMediumQuery2 = []
            for FetchedUrl in search(Mediumquery2, tld='com', lang='en', stop=5, pause=2.0):
                ArryofUrlMediumQuery2.append(FetchedUrl)

            ArrayofMediumSentencesQuery2 = []

            for i in ArryofUrlMediumQuery2:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p']):
                    ArrayofMediumSentencesQuery2.append(content.text)

                NullFreeArrayofMediumSentencesQuery2 = FetchUrl.removeEmptySpaces(ArrayofMediumSentencesQuery2)
                DigitFreeArrayofMediumSentencesQuery2 = FetchUrl.removeDigits(NullFreeArrayofMediumSentencesQuery2)
                PunctuationFreeArrayofMediumSentencesQuery2 = FetchUrl.removePunctuation(DigitFreeArrayofMediumSentencesQuery2)

            Mediumquery3 = Mediumquery1 + 'example'
            ArryofUrlMediumQuery3 = []
            for FetchedUrl in search(Mediumquery3, tld='com', lang='en', stop=5, pause=2.0):
                ArryofUrlMediumQuery3.append(FetchedUrl)

            ArrayofMediumSentencesQuery3 = []
            for i in ArryofUrlMediumQuery3:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p']):
                    ArrayofMediumSentencesQuery3.append(content.text)

            NullFreeArrayofMediumSentencesQuery3 = FetchUrl.removeEmptySpaces(ArrayofMediumSentencesQuery3)
            DigitFreeArrayofMediumSentencesQuery3 = FetchUrl.removeDigits(NullFreeArrayofMediumSentencesQuery3)
            PunctuationFreeArrayofMediumSentencesQuery3 = FetchUrl.removePunctuation(DigitFreeArrayofMediumSentencesQuery3)


            final_result = [[PunctuationFreeArrayofMediumSentencesQuery1, PunctuationFreeArrayofMediumSentencesQuery2, PunctuationFreeArrayofMediumSentencesQuery3], [Mediumquery1, Mediumquery2, Mediumquery3]]

        elif Template == 'Complex':
            Complexquery1 = query
            ArryofUrlComplexQuery1 = []
            for FetchedUrl in search(Complexquery1, tld='com', lang='en', stop=1, pause=2.0):
                ArryofUrlComplexQuery1.append(FetchedUrl)

            ArrayofComplexSentencesQuery1 = []

            for i in ArryofUrlComplexQuery1:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p']):
                    ArrayofComplexSentencesQuery1.append(content.text)

                NullFreeArrayofComplexSentencesQuery1 = FetchUrl.removeEmptySpaces(ArrayofComplexSentencesQuery1)
                DigitFreeArrayofComplexSentencesQuery1 = FetchUrl.removeDigits(NullFreeArrayofComplexSentencesQuery1)
                PunctuationFreeArrayofComplexSentencesQuery1 = FetchUrl.removePunctuation(DigitFreeArrayofComplexSentencesQuery1)



            Complexquery2 = Complexquery1 + 'and what are its advantages and Disadvantages?'
            ArryofUrlComplexQuery2 = []
            for FetchedUrl in search(Complexquery2, tld='com', lang='en', stop=5, pause=2.0):
                ArryofUrlComplexQuery2.append(FetchedUrl)

            ArrayofComplexSentencesQuery2 = []

            for i in ArryofUrlComplexQuery2:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p']):
                    ArrayofComplexSentencesQuery2.append(content.text)

                NullFreeArrayofComplexSentencesQuery2 = FetchUrl.removeEmptySpaces(ArrayofComplexSentencesQuery2)
                DigitFreeArrayofComplexSentencesQuery2= FetchUrl.removeDigits(NullFreeArrayofComplexSentencesQuery2)
                PunctuationFreeArrayofComplexSentencesQuery2 = FetchUrl.removePunctuation(DigitFreeArrayofComplexSentencesQuery2)

            Complexquery3 = Complexquery1 + 'example'
            ArryofUrlComplexQuery3 = []
            for FetchedUrl in search(Complexquery3, tld='com', lang='en', stop=5, pause=2.0):
                ArryofUrlComplexQuery3.append(FetchedUrl)

            ArrayofComplexSentencesQuery3 = []
            for i in ArryofUrlComplexQuery3:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p']):
                    ArrayofComplexSentencesQuery3.append(content.text)

                NullFreeArrayofComplexSentencesQuery3 = FetchUrl.removeEmptySpaces(ArrayofComplexSentencesQuery3)
                DigitFreeArrayofComplexSentencesQuery3 = FetchUrl.removeDigits(NullFreeArrayofComplexSentencesQuery3)
                PunctuationFreeArrayofComplexSentencesQuery3 = FetchUrl.removePunctuation(DigitFreeArrayofComplexSentencesQuery3)

            Complexquery4 = Complexquery1 + 'with diagram'
            ArryofUrlComplexQuery4 = []
            for FetchedUrl in search(Complexquery4, tld='com', lang='en', stop=5, pause=2.0):
                ArryofUrlComplexQuery4.append(FetchedUrl)

            ArrayofComplexSentencesQuery4 = []
            for i in ArryofUrlComplexQuery4:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p']):
                    ArrayofComplexSentencesQuery4.append(content.text)

                NullFreeArrayofComplexSentencesQuery4 = FetchUrl.removeEmptySpaces(ArrayofComplexSentencesQuery4)
                DigitFreeArrayofComplexSentencesQuery4 = FetchUrl.removeDigits(NullFreeArrayofComplexSentencesQuery4)
                PunctuationFreeArrayofComplexSentencesQuery4 = FetchUrl.removePunctuation(DigitFreeArrayofComplexSentencesQuery4)

            final_result = [[PunctuationFreeArrayofComplexSentencesQuery1, PunctuationFreeArrayofComplexSentencesQuery2, PunctuationFreeArrayofComplexSentencesQuery3, PunctuationFreeArrayofComplexSentencesQuery4], [Complexquery1, Complexquery2, Complexquery3, Complexquery4]]
            final_resultAfterEmptyString = FetchUrl.removeEmptySpaces(final_result)

        else:
            Blankquery1 = query
            ArryofUrlBlankQuery1 = []
            for FetchedUrl in search(Blankquery1, tld='com', lang='en', stop=3, pause=2.0):
                ArryofUrlBlankQuery1.append(FetchedUrl)
            print(ArryofUrlBlankQuery1)

            ArrayofBlankSentencesQuery1 = []

            for i in ArryofUrlBlankQuery1:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                #patterns = r'offshore | team | offshore team |maximum| productivity'
                print(self.pattern);
                for content in soup.find_all(['p'], text=re.compile('r'+self.pattern, re.I)):
                    ArrayofBlankSentencesQuery1.append(content.text)

                ResultWithoutCertainWord = FetchUrl.removeStringWithCertainWord(ArrayofBlankSentencesQuery1)
                NullFreeArrayofBlankSentencesQuery1 = FetchUrl.removeEmptySpaces(ResultWithoutCertainWord)
                DigitFreeArrayofBlankSentencesQuery1 = FetchUrl.removeDigits(NullFreeArrayofBlankSentencesQuery1)
                PunctuationFreeArrayofBlankSentencesQuery1 = FetchUrl.removePunctuation(DigitFreeArrayofBlankSentencesQuery1)

            final_result = [[PunctuationFreeArrayofBlankSentencesQuery1], [Blankquery1]]

        return final_result


a = FetchUrl('what are software testing objective?', 'Blank')
print(a.fetchDataSet())