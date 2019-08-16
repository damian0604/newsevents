## News events: News preprocessing

# This script preprocesses (lowercase + punctuation removal) the text of dutch-language news articles. The processed text is saved with the key 'softcosine_processed'



import datetime
from inca import Inca
myinca = Inca()


doctype_list = ['nu', 'ad (www)', 'volkskrant (www)']

# Pre-processing: lowercase and punctuation removal
print('Starting with preprocessing...')
print(datetime.datetime.now())

for e in doctype_list:
    try:
        x = 'doctype:"{e}" AND publication_date:[2019-04-15 TO 2019-05-26]'.format(e=e)
        p = myinca.processing.lower_punct(x, 'text', save=True, new_key='softcosine_processed')
        for result in p:
            pass
        print(datetime.datetime.now(), '...done with processing', e)
    except:
        print('It passed this doctype...', e)
        
print('Done with preprocessing!')

