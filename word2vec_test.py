# -*- coding: utf-8 -*-
import gensim
import numpy as np
model = gensim.models.Word2Vec.load("tc.model")

for item in model.most_similar('aws',topn=50):
    print item[0],item[1]



