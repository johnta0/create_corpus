#!/usr/bin/env python

from gensim.models import doc2vec
import sys


"""
1. LabeledSentence をつくりたい
2. 
3. 
"""

def generate_tagged_document(wakati_path):
    print("Opening file...")
    wakati_file = open(wakati_path, 'r')
    tagged_doc = []
    for i, line in enumerate(wakati_file):
        if i > 80000: break
        print("%d行目を解析中..." %i)
        words = []
        for word in line.split():
            words.append(word)
        tagged_doc.append(doc2vec.TaggedDocument(words=words, tags=[i]))
    wakati_file.close()
    return tagged_doc


wakati_path = 'review_wakati.txt'

model = doc2vec.Doc2Vec(documents=sentences, vector_size=5, window=2, min_count=1, workers=4)

fname = 'review.doc2vec.model'
model.save(fname)


