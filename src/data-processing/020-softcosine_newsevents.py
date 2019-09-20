## News events: softcosine analysis

# This script runs the softcosine analysis between three news outlets: NU.nl, Volkskrant and AD on 2018-11-26 TO 2019-05-26.

from datetime import datetime
from inca import Inca
myinca=Inca()

print('Starting the softcosine similarity...', datetime.now())

myinca.analysis.softcosine_similarity.fit(path_to_model='/mnt/elastic/w2v', source=['nu', 'ad (www)', 'volkskrant (www)'], target=['nu', 'ad (www)', 'volkskrant (www)'], sourcetext='softcosine_processed', targettext='softcosine_processed', from_time='2018-11-26', to_time='2019-05-26', days_before=0, days_after=2, merge_weekend=True, filter_below=2, threshold = 0.2, destination='/mnt/elastic/softcosine_output/')
            
print('Done!!')
print(datetime.now())
