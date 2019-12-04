import re
import time
import string
from .PreprocessingOnQuery import PreProcessQuery
#from api.assignmentapi.PreprocessingOnQuery import PreProcessQuery
import bs4 as bs
import requests
from googlesearch import search


class FetchUrl:

    def __init__(self, query, template,course):      #constuctor #self refering to instance of object like this in java
        self.query = query
        self.template = template
        self.course = course

    # def removeEmptySpaces(array):             #Remove empty spaces
    #
    #     arr = list(filter(str.strip, array))
    #     return arr

    # def removeDigits(array):                  #Remove digits
    #
    #     pattern = '[0-9]'
    #     arr = [re.sub(pattern, '', i) for i in array]
    #     return arr

    def removePunctuation(array):             #Remove punctuation marks

       arr = ["".join( j for j in i if j not in string.punctuation) for i in array]
       return arr

    def removeStringWithCertainWord(array):    #Filter Keywords
        keywordFilter = ['learn', 'Learn','Figure','figure','what','What','-','Let','categories', 'Tutorial', '...','let', 'tutorial', ':', 'article', 'Material', 'I would like', 'Types', '@', 'types', 'what if', 'Following', 'following', 'here', 'Here']
        result = [sent for sent in array
                if not any(word in sent for word in keywordFilter)]
        return result

    # def RemoveDuplicateSentences(array):      #Remove duplicate keywords
    #
    #     result= list(dict.fromkeys(array))
    #     return result

    def fetchDataSet(self):                    # This function contain main working
        Template = self.template
        query = self.query
        course = self.course
        obj = PreProcessQuery(self.query)
        self.pattern = obj.getPattern()
        print(self.pattern)

        if Template == 'Medium':
            MediumDefinitionQuery = query+'in'+course
            UrlMediumDefinition = []
            for FetchedUrl in search(MediumDefinitionQuery, tld='com', lang='en', stop=5, pause=2.0):          #Fetching URLS
                print(UrlMediumDefinition.append(FetchedUrl))

            MediumDefinitionSentences = []
            MediumDescriptionSentences = []

            for i in UrlMediumDefinition:

                sauce = requests.get(i)                          # Requesting for Fetched Url
                soup = bs.BeautifulSoup(sauce.content, 'lxml')   # Parsing the page
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=5):     #Fetching paragraph that match the pattern of keywords
                    MediumDefinitionSentences.append(content.text)

                MediumDefinitiondoc = [w.strip() for w in MediumDefinitionSentences if len(w.strip()) >= 35]
                MediumDefinitionWithoutDuplicate = list(dict.fromkeys(MediumDefinitiondoc))
                ResultWithoutCertainWord = FetchUrl.removeStringWithCertainWord(MediumDefinitionWithoutDuplicate)
                PunctuationFreeMediumDefinition = FetchUrl.removePunctuation(ResultWithoutCertainWord)

            MediumDescriptionQuery = 'Full detailed description of'+MediumDefinitionQuery+ 'in'+course

            UrlMediumDescription = []
            for FetchedUrl in search(MediumDescriptionQuery, tld='com', lang='en', stop=10, pause=2.0):  # Fetching URLS
                print(UrlMediumDescription.append(FetchedUrl))


            for i in UrlMediumDescription:

                sauce = requests.get(i)                          # Requesting for Fetched Url
                soup = bs.BeautifulSoup(sauce.content, 'lxml')   # Parsing the page
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=10):     #Fetching paragraph that match the pattern of keywords
                    MediumDescriptionSentences.append(content.text)

                MediumDescriptiondoc = [w.strip() for w in MediumDescriptionSentences if len(w.strip()) >= 35]
                MediumDescriptionWithoutDuplicate = list(dict.fromkeys(MediumDescriptiondoc))
                ResultWithoutCertainWordDescription = FetchUrl.removeStringWithCertainWord(MediumDescriptionWithoutDuplicate)
                PunctuationFreeMediumDescription = FetchUrl.removePunctuation(ResultWithoutCertainWordDescription)

            MediumProsConsQuery = MediumDefinitionQuery + 'what are its advantages and Disadvantages?'+'in'+course

            USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            headers = {'User-Agent': USER_AGENT}
            query_key = MediumProsConsQuery
            query_key = query_key.replace(' ', '+')  # replace space in query space with +
            tgt_url = 'https://www.google.com.sg/search?q={}&tbm=isch&tbs=sbd:0'.format(query_key)  # last part is the sort by relv
            r = requests.get(tgt_url, headers=headers)
            ImageMediumProsCons = [n for n in re.findall('"ou":"([a-zA-Z0-9_./:-]+.(?:jpg|jpeg|png))",', r.text)]

            MediumExampleQuery = MediumDefinitionQuery + 'example'+'in'+course
            UrlMediumExample = []
            for FetchedUrl in search(MediumExampleQuery, tld='com', lang='en', stop=5, pause=2.0):
                UrlMediumExample.append(FetchedUrl)

            MediumExampleSentences = []
            for i in UrlMediumExample:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all('r Example |Examples', limit=5):
                    MediumExampleSentences.append(content.text)

            MediumExampledoc = [w.strip() for w in MediumExampleSentences if len(w.strip()) >= 35]
            MediumExampleWithoutDuplicate = list(dict.fromkeys(MediumExampledoc))
            PunctuationFreeMediumExample = FetchUrl.removePunctuation(MediumExampleWithoutDuplicate)

            final_result = [[PunctuationFreeMediumDefinition,ImageMediumProsCons,PunctuationFreeMediumExample,PunctuationFreeMediumDescription,UrlMediumDefinition,[query]], [MediumDefinitionQuery, MediumProsConsQuery, MediumExampleQuery]]

        elif Template == 'Complex':

            ComplexDefinitionQuery = query+'in'+course
            UrlComplexDefinition = []
            ComplexDefinitionSentences = []
            ComplexDescriptionSentences = []
            for FetchedUrl in search(ComplexDefinitionQuery, tld='com', lang='en', stop=5, pause=2.0):
                UrlComplexDefinition.append(FetchedUrl)

            for i in UrlComplexDefinition:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=5):
                    ComplexDefinitionSentences.append(content.text)

                ComplexDefinitiondoc = [w.strip() for w in ComplexDefinitionSentences if len(w.strip()) >= 35]
                ComplexDefinitionWithoutDuplicate = list(dict.fromkeys(ComplexDefinitiondoc))
                ResultWithoutCertainWordDefinition = FetchUrl.removeStringWithCertainWord(ComplexDefinitionWithoutDuplicate)
                PunctuationFreeComplexDefinition = FetchUrl.removePunctuation(ResultWithoutCertainWordDefinition)

            ComplexProsConsquery = ComplexDefinitionQuery + 'and what are its advantages and Disadvantages?'+'in'+course

            USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            headers = {'User-Agent': USER_AGENT}
            query_key = ComplexProsConsquery
            query_key = query_key.replace(' ', '+')  # replace space in query space with +
            tgt_url = 'https://www.google.com.sg/search?q={}&tbm=isch&tbs=sbd:0'.format(query_key)  # last part is the sort by relv
            r = requests.get(tgt_url, headers=headers)
            ImageComplexProsCons = [n for n in re.findall('"ou":"([a-zA-Z''0-9_./:-]+.(?:jpg|jpeg|png))",', r.text)]

            ComplexExamplequery = 'Given example of'+ComplexDefinitionQuery+'in'+course
            UrlComplexExample = []
            for FetchedUrl in search(ComplexExamplequery, tld='com', lang='en', stop=3, pause=2.0):
                UrlComplexExample.append(FetchedUrl)

            ComplexExampleSentences = []
            for i in UrlComplexExample:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'],text=re.compile('r Example |Examples'), limit=5):
                    ComplexExampleSentences.append(content.text)

            ComplexExampledoc = [w.strip() for w in ComplexExampleSentences if len(w.strip()) >= 35]
            ComplexExampleWithoutDuplicate = list(dict.fromkeys(ComplexExampledoc))
            PunctuationFreeComplexExample = FetchUrl.removePunctuation(ComplexExampleWithoutDuplicate)

            ComplexDescriptionquery = 'Full detailed description of' + ComplexDefinitionQuery+'in'+course
            UrlComplexDescription = []
            for FetchedUrl in search(ComplexDescriptionquery, tld='com', lang='en', stop=10, pause=2.0):
                UrlComplexDescription.append(FetchedUrl)

            for i in UrlComplexDescription:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=10):
                    ComplexDescriptionSentences.append(content.text)

                ComplexDescriptiondoc = [w.strip() for w in ComplexDescriptionSentences if len(w.strip()) >= 35]
                ComplexDescriptionWithoutDuplicate = list(dict.fromkeys(ComplexDescriptiondoc))
                ResultWithoutCertainWordDescription = FetchUrl.removeStringWithCertainWord(ComplexDescriptionWithoutDuplicate)
                PunctuationFreeComplexDescription = FetchUrl.removePunctuation(ResultWithoutCertainWordDescription)

            ComplexDiagramquery =  'diagram of'+ComplexDefinitionQuery+'in'+course

            USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            headers = {'User-Agent': USER_AGENT}
            query_key = ComplexDiagramquery
            query_key = query_key.replace(' ', '+')  # replace space in query space with +
            tgt_url = 'https://www.google.com.sg/search?q={}&tbm=isch&tbs=sbd:0'.format(
                query_key)  # last part is the sort by relv
            r = requests.get(tgt_url, headers=headers)
            ImageComplexDiagram = [n for n in re.findall('"ou":"([a-zA-Z0-9_./:-]+.(?:jpg|jpeg|png))",', r.text)]

            ComplexConculsionquery = 'Conculsion of' + ComplexDefinitionQuery+'in'+course
            UrlComplexConculsion = []
            for FetchedUrl in search(ComplexConculsionquery, tld='com', lang='en', start=3, stop=6, pause=2.0):
                UrlComplexConculsion.append(FetchedUrl)
            ComplexConculsionSentences =[]

            for i in UrlComplexConculsion:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=5):
                    ComplexConculsionSentences.append(content.text)

                ComplexConculsiondoc = [w.strip() for w in ComplexConculsionSentences if len(w.strip()) >= 35]
                ComplexConculsionWithoutDuplicate = list(dict.fromkeys(ComplexConculsiondoc))
                ResultWithoutCertainWordConculsion = FetchUrl.removeStringWithCertainWord(ComplexConculsionWithoutDuplicate)
                PunctuationFreeComplexConculsion = FetchUrl.removePunctuation(ResultWithoutCertainWordConculsion)

            final_result = [[PunctuationFreeComplexDefinition,ImageComplexProsCons,ImageComplexDiagram,PunctuationFreeComplexExample,PunctuationFreeComplexDescription,PunctuationFreeComplexConculsion,UrlComplexDefinition,[query]], [ComplexDefinitionQuery,ComplexProsConsquery,ComplexExamplequery,ComplexDiagramquery]]

        else:
            BlankDefinitionquery = query+'in'+course
            print(BlankDefinitionquery)
            UrlBlankDefinition = []

            for FetchedUrl in search(BlankDefinitionquery, tld='com', lang='en', stop=5, pause=2.0):
                UrlBlankDefinition.append(FetchedUrl)

            BlankDefiitionSentences = []
            for i in UrlBlankDefinition:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                print(re.compile(self.pattern, re.I))
                for content in soup.find_all(['p'],text=re.compile('r' + self.pattern, re.I), limit=5):
                    BlankDefiitionSentences.append(content.text)
                # print("############")
                # print(BlankDefiitionSentences)

                BlankDefinitiondoc = [w.strip() for w in BlankDefiitionSentences if len(w.strip()) >= 35]
                BlankDescriptionWithoutDuplicate = list(dict.fromkeys(BlankDefinitiondoc))
                ResultWithoutCertainWordBlankDefinition = FetchUrl.removeStringWithCertainWord(BlankDescriptionWithoutDuplicate)
                PunctuationFreeBlankDefinition = FetchUrl.removePunctuation(ResultWithoutCertainWordBlankDefinition)

            BlankDescriptionquery = 'Full detailed description of' + BlankDefinitionquery+'in'+course

            UrlBlankDescription = []
            for FetchedUrl in search(BlankDescriptionquery, tld='com', lang='en', stop=10, pause=2.0):
                UrlBlankDescription.append(FetchedUrl)

            BlankDescriptionSentences = []
            for i in UrlBlankDescription:

                sauce = requests.get(i)
                soup = bs.BeautifulSoup(sauce.content, 'lxml')
                for content in soup.find_all(['p'], text=re.compile('r' + self.pattern, re.I), limit=10):
                    BlankDescriptionSentences.append(content.text)
                # print("****************8")
                # print(BlankDescriptionSentences)

                BlankDescriptiondoc = [w.strip() for w in BlankDescriptionSentences if len(w.strip()) >= 35]
                BlankDefinitionWithoutDuplicate = list(dict.fromkeys( BlankDescriptiondoc))
                ResultWithoutCertainWordDescription = FetchUrl.removeStringWithCertainWord(BlankDefinitionWithoutDuplicate)
                PunctuationFreeBlankDescription = FetchUrl.removePunctuation(ResultWithoutCertainWordDescription)

            final_result = [[PunctuationFreeBlankDefinition,PunctuationFreeBlankDescription,UrlBlankDefinition,[query]], [BlankDefinitionquery,BlankDescriptionquery]]


        return final_result


# a = FetchUrl('what is database?', 'easy', 'computer science')
# #a = FetchUrl('what is a bug', 'Blank')
# a.fetchDataSet()

