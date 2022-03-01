from nltk import tokenize
from operator import itemgetter
import math
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 


with open("AwsCloudEngg.txt") as f:
    doc = f.readlines()
    doc = str(doc)
stop_words = set(stopwords.words('english'))
total_words = doc.split()
total_word_length = len(total_words)
print(total_word_length)
#print(doc)
total_sentences = tokenize.sent_tokenize(doc)
total_sent_len = len(total_sentences)
print(total_sent_len)

tf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in tf_score:
            tf_score[each_word] += 1
        else:
            tf_score[each_word] = 1
#Calculating TF
tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())
#print(tf_score)

def check_sent(word, sentences): 
    final = [all([w in x for w in word]) for x in sentences] 
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))

#Calculating IDF
idf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in idf_score:
            idf_score[each_word] = check_sent(each_word, total_sentences)
        else:
            idf_score[each_word] = 1


idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())

#print(idf_score)

tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
#print(tf_idf_score)

def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
    res = list(result.keys())
    return res

print(get_top_n(tf_idf_score, 15))
