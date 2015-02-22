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
import json



FILTER="enterprise"
FILTER=FILTER.lower()
directory= str(os.path.realpath(__file__)).replace('/clustering/cluste_by_words_frequency.py','')
data_path=directory+'/db/nasdaq.csv'




# 


# sleep(60)


data=pd.read_csv(data_path)

data=data.irow(range(20))

#DATA FILTER

# data=data[data.description.apply(lambda e: FILTER in str(e).lower()) |data.industry.apply(lambda e: FILTER in str(e).lower())|data.Sector.apply(lambda e: FILTER in str(e).lower())]
# data=data.irow(range)
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

n=len(data.description)

MATRIX=np.zeros((n,n))


for i in range(n):
    for j in range(n):
        if j<=i:
            # print i 
            # print j

            interset=[item for item in text_to_vector(data['description'].irow(i)) if item in text_to_vector(data['description'].irow(i))]
            similarity=0
            for item in interset:
                similarity+=min(data['description'].irow(i).count(item),data['description'].irow(j).count(item))
            MATRIX[i][j]=similarity




print MATRIX





# def cosine_similarity(text1,text2):
#     text1=str(text1)
#     text2=str(text2)

#     StopCharacters=[",", "'s",".","\xe2\x80\x99","'"]
#     for item in StopCharacters:
#         # print text1
#         # print text2
#         text1=text1.replace(item,"")
#         text2=text2.replace(item,"")
#     # print "here is text1:",text1
#     # print "here is text2:",text2
#     vec1 = text_to_vector(text1)
#     vec1=dict(vec1)
#     # for item in vec1:
#     vec1=Counter(vec1)

#     vec2 = text_to_vector(text2)
#     vec2=dict(vec2)
#     # vec2.update(ngrams_computation(text2,2))

#     intersection = set(vec1.keys()) & set(vec2.keys())
#     numerator = sum([vec1[x] * vec2[x] for x in intersection])

#     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
#     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
#     denominator = math.sqrt(sum1) * math.sqrt(sum2)

#     # print "vec1:",vec1
#     # print "vec2:",vec2
#     # print "intersection:",intersection
#     # print "numerator:", numerator
#     # print "denominator:",denominator
#     # print "sum1:",sum1
#     # print "sum2:",sum2

#     if not denominator:
#         return 0.0
#     else:
#         # print "my cosine similarity score:", float(numerator) / denominator
#         return float(numerator) / denominator


# documents=list(data['description']+' '+data['industry']+' '+data['Sector'])









# NEW_MATRIX=1.0/(1-float(0.9)*MATRIX)
# # print "+++++++++++++++++++++++"
# # print "++++++++++++++++++"


# # print NEW_MATRIX



NETWORK={"nodes":
                [{"name":{
                        'name':data['Name'].irow(i),
                        'description':data['description'].irow(i),
                        'industry':data['industry'].irow(i),
                        'Sector':data['Sector'].irow(i)
                        },
                "group":data['industry'].irow(i)
                } for i in range(len(data["Name"]))],
        "links":[]
        }

# group_list=[]
# group_order=0
# f=open("link.csv","a")

#interation 1:
for i in range(n):
    # group_order+=1
    # print "here is my group number", group_order
    # print NETWORK['nodes'][j]['name']
    for j in range(n):
        if j<i:
            # if percentileofscore(NEW_MATRIX[i],NEW_MATRIX[i][j])>0.4 and NEW_MATRIX[i][j]>1.001:# and len():
            NETWORK['links'].append({"source":i,"target":j,"value":math.floor(MATRIX[i][j])})
            # print len(data)
            # additional_data_point=str(i)+','+str(j)
            # f.write(additional_data_point)

            # if i<6:
            #     NETWORK['nodes'][j]["group"]=group_order

                    

                #update group lable:
                
# f.close()



# #review:




# # print "+++++++++++++++++"
pprint.pprint(NETWORK)  

f=open('file.json',"w")
f.write(json.dumps(NETWORK))




















#           pass
#   if MATRIX[]


# print MATRIX[0]






















# print MATRIX[0][1]

# # #1 Ukraine conflict: Why is violence surging?
# # text1=get_text1('http://www.bbc.com/news/world-europe-28969784')


# # #2 Ukraine conflict: US 'may supply arms to Ukraine'

# # text2=get_text1('http://www.bbc.com/news/world-europe-31279621')



# # #3Ukraine crisis: Mother films shelling nearing apartment

# # text3=get_text1('http://www.bbc.com/news/world-europe-31352855')



# # #4 Shinzo Abe re-elected as Japan's prime minister 

# # text4=get_text1('http://www.bbc.com/news/world-asia-30595376')


# # #5 Japan election: Voters back Shinzo Abe as PM wins new term
# # text5=get_text1('http://www.bbc.com/news/world-asia-30444230')


# # #6 Japan PM Shinzo Abe calls snap election in December
# # text6=get_text1('http://www.bbc.com/news/world-asia-30092633')

# # #Does Kim Jong Un's new look reflect a new attitude?
# # text7=get_text1('http://www.cnn.com/2015/02/19/asia/north-korea-kim-jong-un-hair/index.html')


# # #CNN and its analysts are pretty sure that Kim Jong Uns new power hairdo is the start of WWIII
# # text8=get_text1('http://canadafreepress.com/index.php/article/69917')

# # #north-korea-unveils-kim-jong-uns-private-jet
# # text9=get_text1('http://www.hawaiinewsnow.com/story/28127108/north-korea-unveils-kim-jong-uns-private-jet')
# # # documents = ["Human machine interface for lab abc computer applications",
# # #              "A survey of user opinion of computer system response time",
# # #              "The EPS user interface management system",
# # #              "System and human system engineering testing of EPS",
# # #              "Relation of user perceived response time to error measurement",
# # #              "The generation of random binary unordered trees",
# # #              "The intersection graph of paths in trees",
# # #              "Graph minors IV Widths of trees and well quasi ordering",
# # #              "Graph minors A survey"]

# # documents=[text1,text2,text3,text4,text5,text6,text7,text8,text9]

# documents=list(data.product_desc)


#       # if len(documents[i])!=len(documents[i]):
#       #   print i
#       #   print item

# true_k = 6
# vectorizer = TfidfVectorizer(stop_words='english')



# # for item in list(vectorizer):
# #     print item

# # sleep(5)



# X = vectorizer.fit_transform(documents)

# print X


# # sleep(10)
# model = KMeans(n_clusters=true_k, init='k-means++', max_iter=500, n_init=1)
# model.fit(X)
# print("Top terms per cluster:")
# order_centroids = model.cluster_centers_.argsort()[:, ::-1]
# terms = vectorizer.get_feature_names()

# print terms


# sleep(10)
# for i in range(true_k):
#   print "Cluster %d:" % i,

#   list_of_a_cluster=[]
#   for j in range(len(model.labels_)):
#       if int(model.labels_[j])==int(i):
#           print list(data.name)[j]
#           list_of_a_cluster.append(j)
#   print "here is my cluster id", list_of_a_cluster
#   if len(list_of_a_cluster)>2:
#       set1=data['product_desc'][list_of_a_cluster[0]].split(" ")
#       # print set1
#       set2=data['product_desc'][list_of_a_cluster[2]].split(" ")
#       # print set2
#       print "here is the common set"
#       print [item for item in set1 if item in set2]


#       set1=data['product_desc'][list_of_a_cluster[0]].split(" ")
#       # print set1
#       set2=data['product_desc'][list_of_a_cluster[1]].split(" ")
#       # print set2

#       print "here is the common set"
#       print [item for item in set1 if item in set2]


#       set1=data['product_desc'][list_of_a_cluster[0]].split(" ")
#       # print set1
#       set2=data['product_desc'][list_of_a_cluster[3]].split(" ")
#       # print set2

#       print "here is the common set"
#       print [item for item in set1 if item in set2]





#   for ind in order_centroids[i, :10]:
#       print ' %s' % terms[ind],
#   print




# # print "=========="
# # print order_centroids
# # print X

# # print vectorizer

# print model.labels_
