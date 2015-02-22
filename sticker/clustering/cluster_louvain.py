from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from time import sleep
import pandas as pd 
from collections import Counter
import numpy as np
import re, math
from collections import Counter
from itertools import tee, islice
from collections import defaultdict
import pprint
from time import sleep
import simplejson
import os
from scipy.stats import percentileofscore
import math
import pprint


FILTER="healthcare"
FILTER=FILTER.lower()
directory= str(os.path.realpath(__file__)).replace('/clustering/cluster.py','').replace('/clustering/cluster_louvain.py','')
data_path=directory+'/db/nasdaq.csv'


# sleep(10)


data=pd.read_csv(data_path)
data=data[data.description.apply(lambda e: FILTER in str(e).lower()) |data.industry.apply(lambda e: FILTER in str(e).lower())|data.Sector.apply(lambda e: FILTER in str(e).lower())]
print len(data)
data=data.irow(range(50))
# print len(data)
WORD = re.compile(r'\w+')


stopwords = ["na", "the", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost",
            "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and",
            "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as", "at", "back", "be", "became",
            "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides",
            "between", "beyond", "bill", "both", "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt",
            "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else",
            "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few",
            "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from",
            "front", "full", "further", "get", "give", "go", "had", "has", "hasnt",
            "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself",
            "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into",
            "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many",
            "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must",
            "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none",
            "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto",
            "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps",
            "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she",
            "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something",
            "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their",
            "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon",
            "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru",
            "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until",
            "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever",
            "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while",
            "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet",
            "you", "your", "yours", "yourself", "yourselves", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "1.", "2.", "3.", "4.", "5.", "6.", "11",
            "7.", "8.", "9.", "12", "13", "14", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            "terms", "CONDITIONS", "conditions", "values", "interested.", "care", "sure", ".", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]", ":", ";", ",", "<", ".", ">", "/", "?", "_", "-", "+", "=",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "contact", "grounds", "buyers", "tried", "said,", "plan", "value", "principle.", "forces", "sent:", "is,", "was", "like",
            "discussion", "tmus", "diffrent.", "layout", "area.", "thanks", "thankyou", "hello", "bye", "rise", "fell", "fall", "psqft.", "http://", "km", "miles","  "]




for i in range(len(data['description'])):
	# print data['description'][i]
	for item in stopwords:
		item=' '+item+' '
		# print documents[i]
		# tem=data['description'][i]
		data['description'][i]=data['description'].irow(i).replace(item,' ')


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)



def my_cosine_similarity(text1,text2):
    text1=str(text1)
    text2=str(text2)
    StopCharacters=[",", "'s",".","\xe2\x80\x99","'"]
    for item in StopCharacters:
        # print text1
        # print text2
        text1=text1.replace(item,"")
        text2=text2.replace(item,"")
    # print "here is text1:",text1
    # print "here is text2:",text2
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

    # print "vec1:",vec1
    # print "vec2:",vec2
    # print "intersection:",intersection
    # print "numerator:", numerator
    # print "denominator:",denominator
    # print "sum1:",sum1
    # print "sum2:",sum2

    if not denominator:
        return 0.0
    else:
        # print "my cosine similarity score:", float(numerator) / denominator
        return float(numerator) / denominator


documents=list(data['description']+' '+data['industry']+' '+data['Sector'])


n=len(data.description)

MATRIX=np.zeros((n,n))
MATRIX=1.0/(1-float(0.9)*MATRIX)
for i in range(n):
    for j in range(n):
        MATRIX[i][j]=math.floor(MATRIX[i][j])

for i in range(n):
	for j in range(n):
		MATRIX[i][j]=my_cosine_similarity(documents[i],documents[j])


# print MATRIX
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
# input data


import urllib, zipfile, StringIO, xlrd, community
from matplotlib import rcParams





# input data
D = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        v = MATRIX[i][j]
        if v: D[i][j] = 1

D = D.T # 100 x 32
D

S = cosine_similarity(D) # 100 x 100
S[S <= 0.49999] = 0 # using < 0.5 is not working well here for some reason
S[S != 0] = 1
S


# S as adjacency matrix
G = nx.from_numpy_matrix(S)

# Louvain method for community detection
partition = community.best_partition(G)



rcParams['figure.figsize'] = 12, 8

pos = nx.spring_layout(G, k=0.05)
colors = 'bgrcmykw'
for i, com in enumerate(set(partition.values())):
    if i<8:
        print i
        list_nodes = [nodes for nodes in partition.keys()
                                    if partition[nodes] == com]
        nx.draw_networkx_nodes(G, pos, list_nodes,
                                node_size=100, node_color=colors[i])

nx.draw_networkx_edges(G, pos, alpha=0.5);
plt.show()


