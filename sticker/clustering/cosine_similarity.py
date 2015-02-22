import re, math
from collections import Counter

from itertools import tee, islice
from collections import Counter

from collections import defaultdict
import re
import pprint
import string
from time import sleep
import simplejson

WORD = re.compile(r'\w+')

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)



def text_similarity(text1,text2):

    StopCharacters=[",", "'s",".","\xe2\x80\x99","'"]
    for item in StopCharacters:
        print text1
        print text2
        text1=text1.replace(item,"")
        text2=text2.replace(item,"")
    print "here is text1:",text1
    print "here is text2:",text2
    vec1 = text_to_vector(text1)
    vec1=dict(vec1)
    # for item in vec1:
    vec1=Counter(vec1)

    vec2 = text_to_vector(text2)
    vec2=dict(vec2)
    # vec2.update(ngrams_computation(text2,2))

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    print "vec1:",vec1
    print "vec2:",vec2
    print "intersection:",intersection
    print "numerator:", numerator
    print "denominator:",denominator
    print "sum1:",sum1
    print "sum2:",sum2

    if not denominator:
        return 0.0
    else:
        print "my cosine similarity score:", float(numerator) / denominator
        return float(numerator) / denominator

if __name__ == '__main__':
    text_similarity("I am a student","I am used to a student")


    



