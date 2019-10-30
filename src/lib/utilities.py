from collections import Counter
from math import log
import pandas as pd

DECIMALS_IN_OUTPUT = 2
def most_distinguishing_words(corpus1, corpus2, top=10, overrepresented_only=True):
    '''
    Takes to corpora (either as single string or as list of words) as input
    and returns that are most overrepresented in corpus 1, together with
    metrics such as their log-likelihood. The corpora are assumed to be 
    preprocessed (lowercased, without punctuation, etc.)

    For a description of the method, see Paul Rayson and Roger Garside,
    2000. "Comparing corpora using frequencyprofiling," WCC '00: 
    Proceedings of the Workshop on Comparing Corpora, volume 9. 
    doi: http://dx.doi.org/10.3115/1117729.1117730,
    '''

    if type(corpus1) is str:
        corpus1=corpus1.split()
    if type(corpus2) is str:
        corpus2=corpus2.split()
        
    corpus1 = Counter(corpus1)
    corpus2 = Counter(corpus2)
        
    # a = freq in corpus1
    # b = freq in corpus2
    # c = number of words corpus1
    # d = number of words corpus2
    # e1 = expected value corpus1
    # e2 = expected value corpus2

    c = sum(corpus1.values())
    d = sum(corpus2.values())
    ll = {}
    e1dict = {}
    e2dict = {}

    for word in corpus1:
        a = corpus1[word]
        try:
            b = corpus2[word]
        except KeyError:
            b = 0
        e1 = c * (a + b) / (c + d)
        e2 = d * (a + b) / (c + d)
        # llvalue=2 * ((a * log(a/e1)) + (b * log(b/e2)))
        # if b=0 then (b * log(b/e2)=0 and NOT nan. therefore, we cannot use the formula above
        if a == 0:
            part1 = 0
        else:
            part1 = a * log(a / e1)
        if b == 0:
            part2 = 0
        else:
            part2 = b * log(b / e2)
        llvalue = 2 * (part1 + part2)
        ll[word] = llvalue
        e1dict[word] = e1
        e2dict[word] = e2

    for word in corpus2:
        if word not in corpus1:
            a = 0
            b = corpus2[word]
            e2 = d * (a + b) / (c + d)
            llvalue = 2 * (b * log(b / e2))
            ll[word] = llvalue
            e1 = c * (a + b) / (c + d)
            e1dict[word] = e1
            e2dict[word] = e2
        
    # f.write("ll,word,freqcorp1,expectedcorp1,freqcorp2,expectedcorp2\n")
    results = pd.DataFrame(columns = ['loglikelihood', 'word', 'observed corpus 1', 'expected corpus 1', 'observed corpus 2', 'expected corpus 2'])

    i=0
    for word, value in ((k, ll[k]) for k in sorted(ll, key=ll.get, reverse=True)):
        try:
            freqcorp1 = corpus1[word]
        except KeyError:
            freqcorp1 = 0
        try:
            freqcorp2 = corpus2[word]
        except KeyError:
            freqcorp2 = 0
        e1 = e1dict[word]
        e2 = e2dict[word]

        if overrepresented_only==True:
            if freqcorp1 <= e1dict[word]:
                continue

        results = results.append({'loglikelihood':value,
                        'word':word,
                        'observed corpus 1':freqcorp1,
                        'expected corpus 1':round(e1, DECIMALS_IN_OUTPUT),
                        'observed corpus 2':freqcorp2,
                                  'expected corpus 2': round(e2, DECIMALS_IN_OUTPUT)}, ignore_index=True)
        
        i+=1
        if i==top:
            break
    return results
