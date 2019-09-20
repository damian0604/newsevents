#!/usr/bin/env python3

import networkx as nx
from tqdm import tqdm
from glob import glob
import os
import pickle


models = [('softcosine', glob('../../data/raw-private/softcosine_output/*.pkl')),
          ('cosine', glob('../../data/raw-private/cosine_output/*.pkl'))]

for modelname, filenames in models:
    print('Processing output of the {} model...\n\n\n'.format(modelname))
    for fn in tqdm(filenames):
        with open(fn, mode='rb') as fi:
            df = pickle.load(fi)
            G = nx.Graph()
            # change int to str (necessary for pajek format)
            df['similarity'] = df['similarity'].apply(str)
            # change column name to 'weights' to faciliate later analysis
            df.rename({'similarity':'weight'}, axis=1, inplace=True) 
            # notes and weights from dataframe
            G = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='weight')
            # write to pajek
            path = '../../data/intermediate/{}/'.format(modelname)
            if not os.path.exists(path):
                os.mkdir(path)
            nx.write_pajek(G, path+os.path.basename(fn)[:-3]+'net')

