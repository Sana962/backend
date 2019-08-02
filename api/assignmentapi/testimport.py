from .ScrapingDataDummy import FetchUrl
from enum import Enum


class Word2Vec:

    def __init__(self, query, template):
        self.query = query
        self.template = template

    def loadFormat(self):
        sd = FetchUrl(self.query, self.template)
        # sd = ScrappingDataDummy.FetchUrl('What is software testing?', 'Simple')
        data = sd.fetchDataSet()
        return data


# v2v = Word2Vec('What is software testing?', 'Simple')
# print(v2v.loadFormat())
