import gensim
import random

path = './model/idwiki_word2vec_300.model'
id_w2v = gensim.models.word2vec.Word2Vec.load(path)
my_file = open("kata-dasaroriginal.txt", "r")
data = my_file.read()
data_into_list = data.split("\n")
secret_word = random.choice(data_into_list)
my_file.close()
for i in data_into_list:
    secret_word = random.choice(data_into_list)
    if secret_word in list(id_w2v.wv.vocab):
        print(secret_word)
        print(id_w2v.wv.similarity(secret_word, secret_word))
        print(id_w2v.wv.most_similar(secret_word, topn=100))
        break
    else:
        print('gada kata')
        continue
# # print('////')
# print(list(id_w2v.wv.vocab))
# # print(random.choice(list(id_w2v.wv.vocab)))