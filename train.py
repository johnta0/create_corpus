#!/usr/bin/env python

from gensim.models import word2vec
import sys

sentences = word2vec.LineSentence(sys.argv[1])
model = word2vec.Word2Vec(sentences=sentences,
                          sg=1, # 0: CBOW, 1: Skip-gram
                          window=5, # max distance from input word
                          min_count=5, # filter by occurence frequency
                          )
model.save(sys.argv[2])
