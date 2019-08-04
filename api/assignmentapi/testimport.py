import gensim

# from .DocSim import DocSim
# from .ScrapingDataDummy import FetchUrl
from api.assignmentapi.DocSim import DocSim
from api.assignmentapi.ScrapingDataDummy import FetchUrl


class Word2Vec:

    def __init__(self, query, template):
        self.query = query
        self.template = template
        print("Class instantiated")
        # model = gensim.models.KeyedVectors.load_word2vec_format(
        #     r'C:\Users\abc\Desktop\GoogleNews-vectors-negative300.bin', binary=True)
        # stopwords_path = "C:\\Users\\abc\Desktop\Backend\data\stopwords_en.txt"
        # with open(stopwords_path, 'r') as fh:
        #     stopwords = fh.read().split(",")
        # self.ds = DocSim(model, stopwords=stopwords)

    def loadFormat(self):
        print("Fetching urls")
        sd = FetchUrl(self.query, self.template)
        # sd = ScrappingDataDummy.FetchUrl('What is software testing?', 'Simple')
        data = sd.fetchDataSet()
        print(data)
        print("Urls fetched, going for similrity check")
        final_response =  []
        # for index, value in enumerate(data[0]):
            # print(data[1][index], value)
            # final_response.append(self.ds.calculate_similarity(data[1][index], value))
        # print(final_response)
        return final_response

v2v = Word2Vec('What is software testing?', 'Simple')
v2v.loadFormat()
