# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
This basic example loads a pre-trained model from the web and uses it to
generate sentence embeddings for a given list of sentences.
"""

import sys

sys.path.append('..')
from text2vec import SBert
from text2vec import Word2Vec


def compute_emb(model):
    # Embed a list of sentences
    sentences = ['卡',
                 '银行卡',
                 '如何更换花呗绑定银行卡',
                 '花呗更改绑定银行卡',
                 'This framework generates embeddings for each input sentence',
                 'Sentences are passed as a list of string.',
                 'The quick brown fox jumps over the lazy dog.']
    sentence_embeddings = model.encode(sentences)

    print(type(sentence_embeddings), sentence_embeddings.shape)

    # The result is a list of sentence embeddings as numpy arrays
    for sentence, embedding in zip(sentences, sentence_embeddings):
        print("Sentence:", sentence)
        print("Embedding:", embedding)
        print("")


sbert_model = SBert('paraphrase-multilingual-MiniLM-L12-v2')
compute_emb(sbert_model)

w2v_model = Word2Vec('w2v-light-tencent-chinese')
compute_emb(w2v_model)