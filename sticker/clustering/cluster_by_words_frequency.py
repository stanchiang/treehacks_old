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


def search(keyword):
    FILTER=keyword
    FILTER=FILTER.lower()
    directory= str(os.path.realpath(__file__)).replace('/clustering/cluster_by_words_frequency.py','')
    data_path=directory+'/db/nasdaq.csv'




    # 


    # sleep(60)


    data=pd.read_csv(data_path)

    data=data.irow(range(20))
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
       
        for item in stopwords:
            item=' '+item+' '
            data['description'][i]=data['description'].irow(i).replace(item,' ')


    def text_to_vector(text):
        words = WORD.findall(text)
        return Counter(words)

    n=len(data.description)

    MATRIX=np.zeros((n,n))




    '''based'''

    NETWORK_BASE={"nodes":
                    [{"name":{
                            'name':data['Name'].irow(i),
                            'description':data['description'].irow(i),
                            'industry':data['industry'].irow(i),
                            'Sector':data['Sector'].irow(i),
                            'z_score':data['z_score'].irow(i),
                            '$_last_5_day':data['$_last_5_day'].irow(i),
                            },
                    "group":"NA"}],
            "links":[]
            }

    '''#Network base on category:'''
    NETWORK1={"nodes":
                    [{"name":{
                            'name':data['Name'].irow(i),
                            'description':data['description'].irow(i),
                            'industry':data['industry'].irow(i),
                            'Sector':data['Sector'].irow(i),
                            'z_score':data['z_score'].irow(i),
                            '$_last_5_day':data['$_last_5_day'].irow(i),
                            },
                    "group":data['industry'].irow(i)} for i in range(len(data["Name"]))],
            "links":[]
            }

    for i in range(n):
        for j in range(n):
            if j<i:
                if data['Sector'].irow(i)==data['Sector'].irow(j):
                # if percentileofscore(NEW_MATRIX[i],NEW_MATRIX[i][j])>0.4 and NEW_MATRIX[i][j]>1.001:# and len():
                    NETWORK1['links'].append({"source":i,"target":j,"value":data['Sector'].irow(i)})
                # print len(data)
                # additional_data_point=str(i)+','+str(j)
                # f.write(additional_data_point)

    pprint.pprint(NETWORK1)  

    f=open(directory+'data1.json',"w")
    f.write(json.dumps(NETWORK1))



    '''#CORRELATION VS''' 
    NETWORK2={"nodes":
                    [{"name":{
                            'name':data['Name'].irow(i),
                            'description':data['description'].irow(i),
                            'industry':data['industry'].irow(i),
                            'Sector':data['Sector'].irow(i),
                            'z_score':data['z_score'].irow(i),
                            '$_last_5_day':data['$_last_5_day'].irow(i),
                            },
                    "group":"NA"} for i in range(len(data["Name"]))],
            "links":[]
            }
    # # group_list=[]
    group_order=0
    # # f=open("link.csv","a")

    #interation 1:
    for i in range(n):
        group_order+=1
        # print "here is my group number", group_order
        # print NETWORK['nodes'][j]['name']
        # for j in range(n):
            # if j<i:
                # if math.floor(MATRIX[i][j])>8
        if percentileofscore(data['$_last_5_day'],data['$_last_5_day'].irow(i))>0.6 and data['$_last_5_day'].irow(i)>0 :# and len():
            NETWORK2['nodes'][i]['group']='postive'
            # NETWORK4['links'].append({"source":i,"target":j,"value":math.floor(MATRIX[i][j])})
            # print len(data)
            # additional_data_point=str(i)+','+str(j)
            # f.write(additional_data_point)
        elif percentileofscore(data['$_last_5_day'],data['$_last_5_day'].irow(i))<0.4 and data['$_last_5_day'].irow(i)<0:

             NETWORK2['nodes'][i]['group']='negative'
                # if i<3:
                #     NETWORK['nodes'][j]["group"]=group_order

    for i in range(n):
        for j in range(n):
            if j<i:
                if NETWORK2['nodes'][i]['group']==NETWORK2['nodes'][j]['group'] and NETWORK2['nodes'][j]['group']!='NA' :
                    NETWORK2['links'].append({"source":i,"target":j,"value":NETWORK2['nodes'][j]['group']})


    pprint.pprint(NETWORK2)  

    f=open(directory+'data2.json',"w")
    f.write(json.dumps(NETWORK2))

             


    '''network 3 z score'''
    NETWORK3={"nodes":
                    [{"name":{
                            'name':data['Name'].irow(i),
                            'description':data['description'].irow(i),
                            'industry':data['industry'].irow(i),
                            'Sector':data['Sector'].irow(i),
                            'z_score':data['z_score'].irow(i),
                            '$_last_5_day':data['$_last_5_day'].irow(i),
                            },
                    "group":"NA"} for i in range(len(data["Name"]))],
            "links":[]
            }
    # # group_list=[]
    group_order=0
    # # f=open("link.csv","a")

    #interation 1:
    for i in range(n):
        group_order+=1
        # print "here is my group number", group_order
        # print NETWORK['nodes'][j]['name']
        # for j in range(n):
            # if j<i:
                # if math.floor(MATRIX[i][j])>8
        if data['z_score'].irow(i)>2:# and len():
            NETWORK3['nodes'][i]['group']='high positive'
            # NETWORK4['links'].append({"source":i,"target":j,"value":math.floor(MATRIX[i][j])})
            # print len(data)
            # additional_data_point=str(i)+','+str(j)
            # f.write(additional_data_point)
        elif data['z_score'].irow(i)<-2:

             NETWORK3['nodes'][i]['group']='high negative'

        else:
            NETWORK3['nodes'][i]['group']='neutrual'


    for i in range(n):
        for j in range(n):
            if j<i:
                if NETWORK3['nodes'][i]['group']==NETWORK2['nodes'][j]['group'] and NETWORK2['nodes'][j]['group']!='NA' :
                    NETWORK3['links'].append({"source":i,"target":j,"value":NETWORK3['nodes'][i]['group']})


    pprint.pprint(NETWORK3)  

    f=open(directory+'data3.json',"w")
    f.write(json.dumps(NETWORK3))


    '''network 4: semantic'''


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




    # print MATRIX




    NETWORK4={"nodes":
                    [{"name":{
                            'name':data['Name'].irow(i),
                            'description':data['description'].irow(i),
                            'industry':data['industry'].irow(i),
                            'Sector':data['Sector'].irow(i),
                            'z_score':data['z_score'].irow(i),
                            '$_last_5_day':data['$_last_5_day'].irow(i),
                            },
                    "group":"NA"} for i in range(len(data["Name"]))],
            "links":[]
            }

    # group_list=[]
    group_order=0
    # f=open("link.csv","a")

    #interation 1:
    for i in range(n):
        group_order+=1
        # print "here is my group number", group_order
        # print NETWORK['nodes'][j]['name']
        for j in range(n):
            if j<i:
                # if math.floor(MATRIX[i][j])>8
                if percentileofscore(MATRIX[i],MATRIX[i][j])>0.3 and MATRIX[i][j]>15:# and len():
                    NETWORK4['links'].append({"source":i,"target":j,"value":math.floor(MATRIX[i][j])})
                    if  NETWORK4['nodes'][i]['group']=='NA':
                        NETWORK4['nodes'][i]['group']=group_order
                    if  NETWORK4['nodes'][j]['group']=='NA': 
                        NETWORK4['nodes'][j]['group']=group_order    

    pprint.pprint(NETWORK4)  

    f=open(directory+'data4.json',"w")
    f.write(json.dumps(NETWORK4))
    return None 

if __name__ == '__main__':
    search("enterprise")