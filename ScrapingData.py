import time
import bs4 as bs
import requests

class FetchUrl:

    Template = 'Simple'
    if Template == 'Simple':
        try:
            from googlesearch import search
            import requests
        except ImportError:
            print("No module named 'google' found")

        Simplequery1 = 'what is project managment?'
        ArryofUrlSimpleQuery1 = []
        for FetchedUrl in search(Simplequery1, tld='com', lang='en', stop=2, pause=2.0):
            ArryofUrlSimpleQuery1.append(FetchedUrl)

        ArrayofSimpleSentencesQuery1 = []

        for i in ArryofUrlSimpleQuery1:

            sauce = requests.get(i)
            # time.sleep(3)
            soup = bs.BeautifulSoup(sauce.content, 'lxml')
            for content in soup.find_all(['p']):
                ArrayofSimpleSentencesQuery1.append(content.text)
        print(ArryofUrlSimpleQuery1)
        print('...................')
        print('...................')
        print('...................')

        SimpleQuery2 = Simplequery1 + 'what are its advantages and Disadvantages pros and cons benefits ?'
        ArryofUrlSimpleQuery2 = []
        for FetchedUrl in search(SimpleQuery2, tld='com', lang='en', stop=2, pause=2.0):
            ArryofUrlSimpleQuery2.append(FetchedUrl)
        print(ArryofUrlSimpleQuery2)

        ArrayofSimpleSentencesQuery2 = []

        for i in ArryofUrlSimpleQuery2:

            sauce = requests.get(i)
            # time.sleep(3)
            soup = bs.BeautifulSoup(sauce.content, 'lxml')
            for content in soup.find_all(['p']):
                ArrayofSimpleSentencesQuery2.append(content.text)



        print('...................')
        print('...................')
        print('...................')

        Simplequery3 = Simplequery1 + 'example'
        ArryofUrlSimpleQuery3 = []
        for FetchedUrl in search(Simplequery3, tld='com', lang='en', stop=2, pause=2.0):
            ArryofUrlSimpleQuery3.append(FetchedUrl)
        print(ArryofUrlSimpleQuery3)

        ArrayofSimpleSentencesQuery3 = []

        for i in ArryofUrlSimpleQuery2:

            sauce = requests.get(i)
            # time.sleep(3)
            soup = bs.BeautifulSoup(sauce.content, 'lxml')
            for content in soup.find_all(['p']):
                ArrayofSimpleSentencesQuery3.append(content.text)

        print('...................')
        print('...................')
        print('...................')

    elif Template == 'Medium':
        try:
            from googlesearch import search
            import requests
        except ImportError:
            print("No module named 'google' found")

        Mediumquery1 = 'What is software testing?'
        ArryofUrlMediumQuery1 = []
        for FetchedUrl in search(Mediumquery1, tld='com', lang='en', stop=5, pause=2.0):
            ArryofUrlMediumQuery1.append(FetchedUrl)

        ArrayofMediumSentencesQuery1 = []

        for i in ArryofUrlMediumQuery1:

            sauce = requests.get(i)
            # time.sleep(3)
            soup = bs.BeautifulSoup(sauce.content, 'lxml')
            for content in soup.find_all(['p']):
                ArrayofMediumSentencesQuery1.append(content.text)
        print('...................')
        print('...................')
        print('...................')

        Mediumquery2 = Mediumquery1 + 'what are its advantages and Disadvantages?'
        ArryofUrlMediumQuery2 = []
        for FetchedUrl in search(Mediumquery2, tld='com', lang='en', stop=5, pause=2.0):
            ArryofUrlMediumQuery2.append(FetchedUrl)

        ArrayofMediumSentencesQuery2 = []

        for i in ArryofUrlMediumQuery2:

            sauce = requests.get(i)
            # time.sleep(3)
            soup = bs.BeautifulSoup(sauce.content, 'lxml')
            for content in soup.find_all(['p']):
                ArrayofMediumSentencesQuery2.append(content.text)

        print('...................')
        print('...................')
        print('...................')

        Mediumquery3 = Mediumquery1 + 'example'
        ArryofUrlMediumQuery3 = []
        for FetchedUrl in search(Mediumquery3, tld='com', lang='en', stop=5, pause=2.0):
            ArryofUrlMediumQuery3.append(FetchedUrl)

        ArrayofMediumSentencesQuery3 = []
        for i in ArryofUrlMediumQuery3:

            sauce = requests.get(i)
            # time.sleep(3)
            soup = bs.BeautifulSoup(sauce.content, 'lxml')
            for content in soup.find_all(['p']):
                ArrayofMediumSentencesQuery3.append(content.text)


        print('...................')
        print('...................')
        print('...................')

        Mediumquery4 = Mediumquery1 + 'with diagram'
        ArryofUrlMediumQuery4 = []
        for FetchedUrl in search(Mediumquery4, tld='com', lang='en', stop=5, pause=2.0):
            ArryofUrlMediumQuery4.append(FetchedUrl)

        ArrayofMediumSentencesQuery4 = []
        for i in ArryofUrlMediumQuery4:

            sauce = requests.get(i)
            # time.sleep(3)
            soup = bs.BeautifulSoup(sauce.content, 'lxml')
            for content in soup.find_all(['p']):
                ArrayofMediumSentencesQuery4.append(content.text)

        print('...................')
        print('...................')
        print('...................')

    elif Template == 'Complex':
        try:
            from googlesearch import search
            import requests
        except ImportError:
            print("No module named 'google' found")

        Complexquery1 = 'What is software testing?'
        ArryofUrlComplexQuery1 = []
        for FetchedUrl in search(Complexquery1, tld='com', lang='en', stop=5, pause=2.0):
            ArryofUrlComplexQuery1.append(FetchedUrl)

        ArrayofComplexSentencesQuery1 = []

        for i in ArryofUrlComplexQuery1:

            sauce = requests.get(i)
            # time.sleep(3)
            soup = bs.BeautifulSoup(sauce.content, 'lxml')
            for content in soup.find_all(['p']):
                ArrayofComplexSentencesQuery1.append(content.text)
        print('...................')
        print('...................')
        print('...................')

        Complexquery2 = Complexquery1 + 'what are its advantages and Disadvantages?'
        ArryofUrlComplexQuery2 = []
        for FetchedUrl in search(Complexquery2, tld='com', lang='en', stop=5, pause=2.0):
            ArryofUrlComplexQuery2.append(FetchedUrl)

        ArrayofComplexSentencesQuery2 = []

        for i in ArryofUrlComplexQuery2:

            sauce = requests.get(i)
            # time.sleep(3)
            soup = bs.BeautifulSoup(sauce.content, 'lxml')
            for content in soup.find_all(['p']):
                ArrayofComplexSentencesQuery2.append(content.text)

        print('...................')
        print('...................')
        print('...................')

        Complexquery3 = Complexquery1 + 'example'
        ArryofUrlComplexQuery3 = []
        for FetchedUrl in search(Complexquery3, tld='com', lang='en', stop=5, pause=2.0):
            ArryofUrlComplexQuery3.append(FetchedUrl)

        ArrayofComplexSentencesQuery3 = []
        for i in ArryofUrlComplexQuery3:

            sauce = requests.get(i)
            # time.sleep(3)
            soup = bs.BeautifulSoup(sauce.content, 'lxml')
            for content in soup.find_all(['p']):
                ArrayofComplexSentencesQuery3.append(content.text)


        print('...................')
        print('...................')
        print('...................')

        Complexquery4 = Complexquery1 + 'with diagram'
        ArryofUrlComplexQuery4 = []
        for FetchedUrl in search(Complexquery4, tld='com', lang='en', stop=5, pause=2.0):
            ArryofUrlComplexQuery4.append(FetchedUrl)

        ArrayofComplexSentencesQuery4 = []
        for i in ArryofUrlComplexQuery4:

            sauce = requests.get(i)
            # time.sleep(3)
            soup = bs.BeautifulSoup(sauce.content, 'lxml')
            for content in soup.find_all(['p']):
                ArrayofComplexSentencesQuery4.append(content.text)

        print('...................')
        print('...................')
        print('...................')


    else:
        try:
            from googlesearch import search
            import requests
        except ImportError:
            print("No module named 'google' found")

        Blankquery1 = 'What is software testing?'
        ArryofUrlBlankQuery1 = []
        for FetchedUrl in search(Blankquery1, tld='com', lang='en', stop=2, pause=2.0):
            ArryofUrlBlankQuery1.append(FetchedUrl)

        ArrayofBlankSentencesQuery1 = []

        for i in ArryofUrlBlankQuery1:

            sauce = requests.get(i)
            # time.sleep(3)
            soup = bs.BeautifulSoup(sauce.content, 'lxml')
            for content in soup.find_all(['p']):
                ArrayofBlankSentencesQuery1.append(content.text)
