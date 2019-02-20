import sys
from gensim.models.doc2vec import Doc2Vec

id1, id2 = sys.argv[1], sys.argv[2]

m = Doc2Vec.load('review.doc2vec.model')

print('--- Calculating the similarity between sentences ---')
f = open('new_line.txt', 'r')
for i, line in enumerate(f):
    if i > 80000: break
    if i == id1:
        print('Sentence1:')
        print(line)
    if i == id2:
        print('Sentence2')
        print(line)
f.close()

similarity = m.docvecs.similarity(1, 5)
print('the similarity is: %d' %similarity)
