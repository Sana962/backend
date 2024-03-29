import gensim
# from DocSim import DocSim
# import DocSim
from .DocSim import DocSim
from .ScrapingDataDummy import FetchUrl
# from ScrapingDataTest import  FetchUrl
#from api.assignmentapi.DocSim import DocSim
#from api.assignmentapi.ScrapingDataDummy import FetchUrl


class Word2Vec:

    def __init__(self, query, template,course):
        self.query = query
        self.template = template
        self.course = course

        # model = gensim.models.KeyedVectors.load_word2vec_format(r'C:\Users\abc\Desktop\GoogleNews-vectors-negative300.bin', binary=True)
        # stopwords_path = "C:\\Users\\abc\Desktop\Backend\data\stopwords_en.txt"
        # with open(stopwords_path, 'r') as fh:
        #      stopwords = fh.read().split(",")
        # self.ds = DocSim(model, stopwords=stopwords)

    def loadFormat(self):
        sd = FetchUrl(self.query, self.template,self.course)
        #sd = FetchUrl('What is software testing?', 'Simple')
        data = sd.fetchDataSet()
        # print(data)
        # final_response =  []
        # for index, value in enumerate(data[0]):
        #     # final_response.append(value)
        #     # print(final_response)
        #     afterSim = self.ds.calculate_similarity(data[1][index], value)
        #     #print(afterSim)
        #     final_response.append(afterSim)
        #     #print(final_response)
        return data

#v2v = Word2Vec('how to perform testing?', 'Blank')
#print(v2v.loadFormat())
