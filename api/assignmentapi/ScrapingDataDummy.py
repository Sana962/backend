import re
import string
from .PreprocessingOnQuery import PreProcessQuery
#from api.assignmentapi.PreprocessingOnQuery import PreProcessQuery
import bs4 as bs
import requests
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
        keywordFilter = ['Let', 'Tutorial', '...', '?','let', 'tutorial', ':', 'article', 'Material', 'I would like', 'Types', '@']
        result = [sent for sent in array
                if not any(word in sent for word in keywordFilter)]
        return result

    def fetchDataSet(self):
        Template = self.template
        query = self.query
        obj = PreProcessQuery(self.query)
        self.pattern = obj.getPattern()

        if Template == 'Medium':
            arrayMedium = []
            Mediumquery1 = query
            ArryofUrlMediumQuery1 = []
            for FetchedUrl in search(Mediumquery1, tld='com', lang='en', stop=3, pause=2.0):
                ArryofUrlMediumQuery1.append(FetchedUrl)
            ArrayofMediumSentencesQuery1 = []

            for i in ArryofUrlMediumQuery1:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                # patterns = r'offshore | team | offshore team |maximum| productivity'
                # print(self.pattern);
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=3):
                    ArrayofMediumSentencesQuery1.append(content.text)

                ResultWithoutCertainWord = FetchUrl.removeStringWithCertainWord(ArrayofMediumSentencesQuery1)
                NullFreeArrayofMediumSentencesQuery1 = FetchUrl.removeEmptySpaces(ResultWithoutCertainWord)
                DigitFreeArrayofMediumSentencesQuery1 = FetchUrl.removeDigits(NullFreeArrayofMediumSentencesQuery1)
                PunctuationFreeArrayofMediumSentencesQuery1 = FetchUrl.removePunctuation(DigitFreeArrayofMediumSentencesQuery1)

            Mediumquery2 = Mediumquery1 + 'what are its advantages and Disadvantages?'

            USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            headers = {'User-Agent': USER_AGENT}
            query_key = Mediumquery2
            query_key = query_key.replace(' ', '+')  # replace space in query space with +
            tgt_url = 'https://www.google.com.sg/search?q={}&tbm=isch&tbs=sbd:0'.format(query_key)  # last part is the sort by relv
            r = requests.get(tgt_url, headers=headers)
            ImageArrayofMediumSentencesQuery2 = [n for n in re.findall('"ou":"([a-zA-Z0-9_./:-]+.(?:jpg|jpeg|png))",', r.text)]

            Mediumquery3 = Mediumquery1 + 'example'
            ArryofUrlMediumQuery3 = []
            for FetchedUrl in search(Mediumquery3, tld='com', lang='en', stop=5, pause=2.0):
                ArryofUrlMediumQuery3.append(FetchedUrl)

            ArrayofMediumSentencesQuery3 = []
            for i in ArryofUrlMediumQuery3:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'], limit=1):
                    ArrayofMediumSentencesQuery3.append(content.text)

            NullFreeArrayofMediumSentencesQuery3 = FetchUrl.removeEmptySpaces(ArrayofMediumSentencesQuery3)
            DigitFreeArrayofMediumSentencesQuery3 = FetchUrl.removeDigits(NullFreeArrayofMediumSentencesQuery3)
            PunctuationFreeArrayofMediumSentencesQuery3 = FetchUrl.removePunctuation(DigitFreeArrayofMediumSentencesQuery3)


            final_result = [[PunctuationFreeArrayofMediumSentencesQuery1,ImageArrayofMediumSentencesQuery2,PunctuationFreeArrayofMediumSentencesQuery3], [Mediumquery1, Mediumquery2, Mediumquery3]]

        elif Template == 'Complex':

            Complexquery1 = query
            ArryofUrlComplexQuery1 = []
            for FetchedUrl in search(Complexquery1, tld='com', lang='en', stop=3, pause=2.0):
                ArryofUrlComplexQuery1.append(FetchedUrl)
            print(ArryofUrlComplexQuery1)

            ArrayofComplexSentencesQuery1 = []

            for i in ArryofUrlComplexQuery1:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                # patterns = r'offshore | team | offshore team |maximum| productivity'
                print(self.pattern);
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=3):
                    ArrayofComplexSentencesQuery1.append(content.text)

                ResultWithoutCertainWord = FetchUrl.removeStringWithCertainWord(ArrayofComplexSentencesQuery1)
                NullFreeArrayofComplexSentencesQuery1 = FetchUrl.removeEmptySpaces(ResultWithoutCertainWord)
                DigitFreeArrayofBlankSentencesQuery1 = FetchUrl.removeDigits(NullFreeArrayofComplexSentencesQuery1)
                PunctuationFreeArrayofComplexSentencesQuery1 = FetchUrl.removePunctuation(DigitFreeArrayofBlankSentencesQuery1)

            Complexquery2 = Complexquery1 + 'and what are its advantages and Disadvantages?'

            USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            headers = {'User-Agent': USER_AGENT}
            query_key = Complexquery2
            query_key = query_key.replace(' ', '+')  # replace space in query space with +
            tgt_url = 'https://www.google.com.sg/search?q={}&tbm=isch&tbs=sbd:0'.format(
                query_key)  # last part is the sort by relv
            r = requests.get(tgt_url, headers=headers)
            ImageArrayofComplexSentencesQuery2 = [n for n in re.findall('"ou":"([a-zA-Z0-9_./:-]+.(?:jpg|jpeg|png))",', r.text)]

            Complexquery3 = 'Given example of'+Complexquery1
            ArryofUrlComplexQuery3 = []
            for FetchedUrl in search(Complexquery3, tld='com', lang='en', stop=3, pause=2.0):
                ArryofUrlComplexQuery3.append(FetchedUrl)

            ArrayofComplexSentencesQuery3 = []
            for i in ArryofUrlComplexQuery3:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'],text=re.compile('r Example |Examples'), limit=1):
                    ArrayofComplexSentencesQuery3.append(content.text)

            NullFreeArrayofComplexSentencesQuery3 = FetchUrl.removeEmptySpaces(ArrayofComplexSentencesQuery3)
            DigitFreeArrayofComplexSentencesQuery3 = FetchUrl.removeDigits(NullFreeArrayofComplexSentencesQuery3)
            PunctuationFreeArrayofComplexSentencesQuery3 = FetchUrl.removePunctuation(DigitFreeArrayofComplexSentencesQuery3)

            Complexquery4 =  'diagram of'+Complexquery1

            USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            headers = {'User-Agent': USER_AGENT}
            query_key = Complexquery4
            query_key = query_key.replace(' ', '+')  # replace space in query space with +
            tgt_url = 'https://www.google.com.sg/search?q={}&tbm=isch&tbs=sbd:0'.format(
                query_key)  # last part is the sort by relv
            r = requests.get(tgt_url, headers=headers)
            ImageArrayofComplexSentencesQuery4 = [n for n in re.findall('"ou":"([a-zA-Z0-9_./:-]+.(?:jpg|jpeg|png))",', r.text)]

            final_result = [[PunctuationFreeArrayofComplexSentencesQuery1,ImageArrayofComplexSentencesQuery2,PunctuationFreeArrayofComplexSentencesQuery3,ImageArrayofComplexSentencesQuery4], [Complexquery1,Complexquery2,Complexquery3,Complexquery4]]

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
                for content in soup.find_all(['p'], text=re.compile('r'+self.pattern, re.I), limit=3):
                    ArrayofBlankSentencesQuery1.append(content.text)

                ResultWithoutCertainWord = FetchUrl.removeStringWithCertainWord(ArrayofBlankSentencesQuery1)
                NullFreeArrayofBlankSentencesQuery1 = FetchUrl.removeEmptySpaces(ResultWithoutCertainWord)
                DigitFreeArrayofBlankSentencesQuery1 = FetchUrl.removeDigits(NullFreeArrayofBlankSentencesQuery1)
                PunctuationFreeArrayofBlankSentencesQuery1 = FetchUrl.removePunctuation(DigitFreeArrayofBlankSentencesQuery1)

            final_result = [[PunctuationFreeArrayofBlankSentencesQuery1], [Blankquery1]]


        return final_result


# a = FetchUrl('what is software testing?', 'Medium')
# #a = FetchUrl('what is a bug', 'Blank')
# print(a.fetchDataSet())