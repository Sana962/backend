import re
import time
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

    def removeEmptySpaces(array):             #Remove empty spaces

        arr = list(filter(str.strip, array))
        return arr

    def removeDigits(array):                  #Remove digits

        pattern = '[0-9]'
        arr = [re.sub(pattern, '', i) for i in array]
        return arr

    def removePunctuation(array):             #Remove punctuation marks

       arr = ["".join( j for j in i if j not in string.punctuation) for i in array]
       return arr

    def removeStringWithCertainWord(array):    #Filter Keywords
        keywordFilter = ['Let','categories', 'Tutorial', '...', '?','let', 'tutorial', ':', 'article', 'Material', 'I would like', 'Types', '@']
        result = [sent for sent in array
                if not any(word in sent for word in keywordFilter)]
        return result

    def fetchDataSet(self):                    # This function contain main working
        Template = self.template
        query = self.query
        obj = PreProcessQuery(self.query)
        self.pattern = obj.getPattern()
        print(self.pattern)

        if Template == 'Medium':
            MediumDefinitionQuery = query
            UrlMediumDefinition = []
            for FetchedUrl in search(MediumDefinitionQuery, tld='com', lang='en', stop=3, pause=2.0):          #Fetching URLS
                print(UrlMediumDefinition.append(FetchedUrl))

            MediumDefinitionSentences = []
            MediumDescriptionSentences = []

            for i in UrlMediumDefinition:

                sauce = requests.get(i)                          # Requesting for Fetched Url
                soup = bs.BeautifulSoup(sauce.content, 'lxml')   # Parsing the page
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=3):     #Fetching paragraph that match the pattern of keywords
                    MediumDefinitionSentences.append(content.text)

                ResultWithoutCertainWord = FetchUrl.removeStringWithCertainWord(MediumDefinitionSentences)
                NullFreeMediumDefinition= FetchUrl.removeEmptySpaces(ResultWithoutCertainWord)
                DigitFreeMediumDefinition = FetchUrl.removeDigits(NullFreeMediumDefinition)
                PunctuationFreeMediumDefinition = FetchUrl.removePunctuation(DigitFreeMediumDefinition)

            MediumDescriptionQuery = 'Full detailed description of'+MediumDefinitionQuery

            UrlMediumDescription = []
            for FetchedUrl in search(MediumDescriptionQuery, tld='com', lang='en', stop=5, pause=2.0):  # Fetching URLS
                print(UrlMediumDescription.append(FetchedUrl))


            for i in UrlMediumDescription:

                sauce = requests.get(i)                          # Requesting for Fetched Url
                soup = bs.BeautifulSoup(sauce.content, 'lxml')   # Parsing the page
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=5):     #Fetching paragraph that match the pattern of keywords
                    MediumDescriptionSentences.append(content.text)

                ResultWithoutCertainWordDescription = FetchUrl.removeStringWithCertainWord(MediumDescriptionSentences)
                NullFreeMediumDescription= FetchUrl.removeEmptySpaces(ResultWithoutCertainWordDescription)
                DigitFreeMediumDescription = FetchUrl.removeDigits(NullFreeMediumDescription)
                PunctuationFreeMediumDescription = FetchUrl.removePunctuation(DigitFreeMediumDescription)

            MediumProsConsQuery = MediumDefinitionQuery + 'what are its advantages and Disadvantages?'

            USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            headers = {'User-Agent': USER_AGENT}
            query_key = MediumProsConsQuery
            query_key = query_key.replace(' ', '+')  # replace space in query space with +
            tgt_url = 'https://www.google.com.sg/search?q={}&tbm=isch&tbs=sbd:0'.format(query_key)  # last part is the sort by relv
            r = requests.get(tgt_url, headers=headers)
            ImageMediumProsCons = [n for n in re.findall('"ou":"([a-zA-Z0-9_./:-]+.(?:jpg|jpeg|png))",', r.text)]

            MediumExampleQuery = MediumDefinitionQuery + 'example'
            UrlMediumExample = []
            for FetchedUrl in search(MediumExampleQuery, tld='com', lang='en', stop=5, pause=2.0):
                UrlMediumExample.append(FetchedUrl)

            MediumExampleSentences = []
            for i in UrlMediumExample:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all('r Example |Examples', limit=2):
                    MediumExampleSentences.append(content.text)

            NullFreeMediumExample = FetchUrl.removeEmptySpaces(MediumExampleSentences)
            DigitFreeMediumExample = FetchUrl.removeDigits(NullFreeMediumExample)
            PunctuationFreeMediumExample = FetchUrl.removePunctuation(DigitFreeMediumExample)

            MediumConculsionuery = MediumDefinitionQuery + 'Conculsion'

            UrlMediumConculsion = []
            for FetchedUrl in search(MediumConculsionuery, tld='com', lang='en', stop=3, pause=2.0):
                print(UrlMediumConculsion.append(FetchedUrl))

            MediumConculsionSentences = []

            for i in UrlMediumConculsion:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=3):
                    MediumConculsionSentences.append(content.text)

                ResultWithoutCertainWord = FetchUrl.removeStringWithCertainWord(MediumConculsionSentences)
                NullFreeMediumConculsion = FetchUrl.removeEmptySpaces(ResultWithoutCertainWord)
                DigitFreeBlankConculsion = FetchUrl.removeDigits(NullFreeMediumConculsion)
                PunctuationFreeMediumConculsion = FetchUrl.removePunctuation(DigitFreeBlankConculsion)


            final_result = [[PunctuationFreeMediumDefinition,ImageMediumProsCons,PunctuationFreeMediumExample,PunctuationFreeMediumDescription,PunctuationFreeMediumConculsion,UrlMediumDefinition], [MediumDefinitionQuery, MediumProsConsQuery, MediumExampleQuery]]

        elif Template == 'Complex':

            ComplexDefinitionQuery = query
            UrlComplexDefinition = []
            for FetchedUrl in search(ComplexDefinitionQuery, tld='com', lang='en', stop=3, pause=2.0):
                UrlComplexDefinition.append(FetchedUrl)

            ComplexDefinitionSentences = []
            ComplexDescriptionSentences = []

            for i in UrlComplexDefinition:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=3):
                    ComplexDefinitionSentences.append(content.text)

                ResultWithoutCertainWordDefinition = FetchUrl.removeStringWithCertainWord(ComplexDefinitionSentences)
                NullFreeComplexDefinition = FetchUrl.removeEmptySpaces(ResultWithoutCertainWordDefinition)
                DigitFreeBlankDefinition = FetchUrl.removeDigits(NullFreeComplexDefinition)
                PunctuationFreeComplexDefinition = FetchUrl.removePunctuation(DigitFreeBlankDefinition)

            ComplexProsConsquery = ComplexDefinitionQuery + 'and what are its advantages and Disadvantages?'

            USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            headers = {'User-Agent': USER_AGENT}
            query_key = ComplexProsConsquery
            query_key = query_key.replace(' ', '+')  # replace space in query space with +
            tgt_url = 'https://www.google.com.sg/search?q={}&tbm=isch&tbs=sbd:0'.format(
                query_key)  # last part is the sort by relv
            r = requests.get(tgt_url, headers=headers)
            ImageComplexProsCons = [n for n in re.findall('"ou":"([a-zA-Z0-9_./:-]+.(?:jpg|jpeg|png))",', r.text)]

            ComplexExamplequery = 'Given example of'+ComplexDefinitionQuery
            UrlComplexExample = []
            for FetchedUrl in search(ComplexExamplequery, tld='com', lang='en', stop=3, pause=2.0):
                UrlComplexExample.append(FetchedUrl)

            ComplexExampleSentences = []
            for i in UrlComplexExample:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'],text=re.compile('r Example |Examples'), limit=5):
                    ComplexExampleSentences.append(content.text)

            NullFreeComplexExample = FetchUrl.removeEmptySpaces(ComplexExampleSentences)
            DigitFreeComplexExample = FetchUrl.removeDigits(NullFreeComplexExample)
            PunctuationFreeComplexExample = FetchUrl.removePunctuation(DigitFreeComplexExample)

            UrlComplexDescription = []
            for FetchedUrl in search(ComplexDefinitionQuery, tld='com', lang='en', start=2, stop=6, pause=2.0):
                UrlComplexDescription.append(FetchedUrl)

            for i in UrlComplexDescription:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=10):
                    ComplexDescriptionSentences.append(content.text)

                ResultWithoutCertainWordDescription = FetchUrl.removeStringWithCertainWord(ComplexDescriptionSentences)
                NullFreeComplexDescription = FetchUrl.removeEmptySpaces(ResultWithoutCertainWordDescription)
                DigitFreeBlankDescription = FetchUrl.removeDigits(NullFreeComplexDescription)
                PunctuationFreeComplexDescription = FetchUrl.removePunctuation(DigitFreeBlankDescription)

            ComplexDiagramquery =  'diagram of'+ComplexDefinitionQuery

            USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            headers = {'User-Agent': USER_AGENT}
            query_key = ComplexDiagramquery
            query_key = query_key.replace(' ', '+')  # replace space in query space with +
            tgt_url = 'https://www.google.com.sg/search?q={}&tbm=isch&tbs=sbd:0'.format(
                query_key)  # last part is the sort by relv
            r = requests.get(tgt_url, headers=headers)
            ImageComplexDiagram = [n for n in re.findall('"ou":"([a-zA-Z0-9_./:-]+.(?:jpg|jpeg|png))",', r.text)]

            UrlComplexConculsion = []
            for FetchedUrl in search(ComplexDefinitionQuery, tld='com', lang='en', start=3, stop=6, pause=2.0):
                UrlComplexConculsion.append(FetchedUrl)
            ComplexConculsionSentences =[]

            for i in UrlComplexConculsion:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=5):
                    ComplexConculsionSentences.append(content.text)

                ResultWithoutCertainWordConculsion = FetchUrl.removeStringWithCertainWord(ComplexConculsionSentences)
                NullFreeComplexConculsion = FetchUrl.removeEmptySpaces(ResultWithoutCertainWordConculsion)
                DigitFreeBlankConculsion = FetchUrl.removeDigits(NullFreeComplexConculsion)
                PunctuationFreeComplexConculsion = FetchUrl.removePunctuation(DigitFreeBlankConculsion)

            final_result = [[PunctuationFreeComplexDefinition,ImageComplexProsCons,PunctuationFreeComplexExample,ImageComplexDiagram,PunctuationFreeComplexDescription,PunctuationFreeComplexConculsion,UrlComplexDefinition], [ComplexDefinitionQuery,ComplexProsConsquery,ComplexExamplequery,ComplexDiagramquery]]

        else:
            BlankDefinitionquery = query
            UrlBlankDefinition = []
            for FetchedUrl in search(BlankDefinitionquery, tld='com', lang='en', stop=1, pause=2.0):
                UrlBlankDefinition.append(FetchedUrl)

            BlankDefiitionSentences = []
            for i in UrlBlankDefinition:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'], re.compile('r'+self.pattern, re.I)):
                    BlankDefiitionSentences.append(content.text)

                ResultWithoutCertainWordDefinition = FetchUrl.removeStringWithCertainWord(BlankDefiitionSentences)
                NullFreeBlankDefinition = FetchUrl.removeEmptySpaces(ResultWithoutCertainWordDefinition)
                DigitFreeBlankDefinition = FetchUrl.removeDigits(NullFreeBlankDefinition)
                PunctuationFreeBlankDefinition = FetchUrl.removePunctuation(DigitFreeBlankDefinition)

            BlankDescriptionquery = 'Full detailed description of' + BlankDefinitionquery

            UrlBlankDescription = []
            for FetchedUrl in search(BlankDescriptionquery, tld='com', lang='en', stop=5, pause=2.0):
                UrlBlankDescription.append(FetchedUrl)

            BlankDescriptionSentences = []
            for i in UrlBlankDescription:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=3):
                    BlankDescriptionSentences.append(content.text)

                ResultWithoutCertainWordDescription = FetchUrl.removeStringWithCertainWord(BlankDescriptionSentences)
                NullFreeBlankDescription = FetchUrl.removeEmptySpaces(ResultWithoutCertainWordDescription)
                DigitFreeBlankDescription = FetchUrl.removeDigits(NullFreeBlankDescription)
                PunctuationFreeBlankDescription = FetchUrl.removePunctuation(DigitFreeBlankDescription)

            final_result = [[PunctuationFreeBlankDefinition,PunctuationFreeBlankDescription,UrlBlankDefinition,UrlBlankDescription], [BlankDefinitionquery]]


        return final_result


#a = FetchUrl('what is software testing?', 'Easy')
#a = FetchUrl('what is a bug', 'Blank')
#print(a.fetchDataSet())

