import gensim
# from DocSim import DocSim
# import DocSim
#from .DocSim import DocSim
#from .ScrapingDataDummy import FetchUrl
# from ScrapingDataTest import  FetchUrl
from api.assignmentapi.DocSim import DocSim
from api.assignmentapi.ScrapingDataDummy import FetchUrl


class Word2Vec:

    def __init__(self, query, template):
        self.query = query
        self.template = template

        #model = gensim.models.KeyedVectors.load_word2vec_format(r'C:\Users\abc\Desktop\GoogleNews-vectors-negative300.bin', binary=True)
        # stopwords_path = "C:\\Users\\abc\Desktop\Backend\data\stopwords_en.txt"
        # with open(stopwords_path, 'r') as fh:
        #      stopwords = fh.read().split(",")
        # self.ds = DocSim(model, stopwords=stopwords)

    def loadFormat(self):
        sd = FetchUrl(self.query, self.template)
        #sd = FetchUrl('What is software testing?', 'Simple')
        data = sd.fetchDataSet()
        return data
        final_response =  []
        # for index, value in enumerate(data[0]):
        #     # final_response.append(value)
        #     # print(final_response)
        #     afterSim = self.ds.calculate_similarity(data[1][index], value)
        #     #print(afterSim)
        #     final_response.append(afterSim)
        #     #print(final_response)
        # return final_response

v2v = Word2Vec('How to get maximum productivity from an offshore team?', 'Blank')
print(v2v.loadFormat())
