import gensim
from ScrapingData import FetchUrl
from gensim.models.keyedvectors import KeyedVectors
from DocSim import DocSim


class word2vec:

    model = gensim.models.KeyedVectors.load_word2vec_format(r'C:\Users\abc\Desktop\GoogleNews-vectors-negative300.bin', binary=True)
    stopwords_path = "./data/stopwords_en.txt"
    with open(stopwords_path, 'r') as fh:
        stopwords = fh.read().split(",")
    ds = DocSim(model,stopwords=stopwords)

    source_doc =  FetchUrl.Simplequery3
    target_docs = FetchUrl.ArrayofSimpleSentencesQuery1
    print(source_doc, target_docs)
    sim_scoresSimpleQ1 = ds.calculate_similarity(source_doc, target_docs)
    print(sim_scoresSimpleQ1)

    print("#########################################################")
    print("#########################################################")
    print("#########################################################")





