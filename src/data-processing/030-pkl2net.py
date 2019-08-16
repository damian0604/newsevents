#!/usr/bin/env python3

import networkx as nx
from tqdm import tqdm
from glob import glob
from os.path import basename
import pickle

filenames = glob('../../data/raw-private/softcosine_output/*.pkl')

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
        nx.write_pajek(G, '../../data/intermediate/'+basename(fn)[:-3]+'net')
