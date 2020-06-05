from gensim import models
from word2vec import Word2Vec, Sent2Vec, LineSentence
import csv
import sklearn


def ExtractWord2Vec(filename):
    sentences = models.word2vec.Text8Corpus(filename)
    # 训练模型，部分参数如下
    model = models.word2vec.Word2Vec(sentences)
    model.wv.save_word2vec_format("model")

def ExtractSent2Vec(filename):
    model = Word2Vec(LineSentence(filename), size=512, window=5, sg=0, min_count=5, workers=8)
    model.save(filename + '.model')
    model.save_word2vec_format(filename + '-01.vec')
    
    model = Sent2Vec(LineSentence(filename), model_file=filename + '.model')
    model.save_sent2vec_format(filename + '-02.vec')


if __name__ == "__main__":
    #ExtractWord2Vec("sample-x.txt")
    ExtractSent2Vec("train-x.txt")
