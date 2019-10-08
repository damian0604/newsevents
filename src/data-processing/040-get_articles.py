#!/usr/bin/env python3

'''
Get all unoique articles ids that have been extracted and retrieve the articles
'''

from tqdm import tqdm
from glob import glob
import pickle
import os
from inca import Inca
import json

myinca = Inca(verbose=False)

# models = [('softcosine', glob('../../data/raw-private/softcosine_output/*.pkl')),
#          ('cosine', glob('../../data/raw-private/cosine_output/*.pkl'))]

models = [('softcosine', glob('/mnt/elastic/softcosine_output/*.pkl')),
          ('cosine', glob('/mnt/elastic/cosine_output/*.pkl'))]



unique_ids = set()
for modelname, filenames in models:
    print('Processing output of the {} model...\n\n\n'.format(modelname))
    for fn in tqdm(filenames):
        with open(fn, mode='rb') as fi:
            df = pickle.load(fi)
            unique_ids = unique_ids.union(set(df['source']))
            unique_ids = unique_ids.union(set(df['target']))



print('Collected IDs of {} unique articles'.format(len(unique_ids)))

path = '../../data/raw-private/articles'
if not os.path.exists(path):
    os.mkdir(path)

fn = path+'/articles_as_json-lines.json'
with open(fn, mode='w') as f:
    for _id in tqdm(unique_ids):
        doc = myinca.database._client.get(id = _id, index='inca')['_source']
        doc['_id'] = _id
        doc.pop('htmlsource')
        doc.pop('META')
        f.write(json.dumps(doc))
        f.write('\n')
    
print('Done. All articles written to {}'.format(fn))
