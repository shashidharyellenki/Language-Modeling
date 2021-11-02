# def buildUniformProbs(unigrams):
#     dict_={}
#     temp_list=[]
#     for i  in unigrams:
#         if i not in dict_:
#             dict_[i]=1
#     for x,y in dict_.items():
#         temp_list.append(y/len(dict_))
#     return temp_list


#     # def buildUnigramProbs(unigrams, unigramCounts, totalCount):
#     # result_list=[]
#     # for i in unigrams:
#     #     if i in unigramCounts:
#     #         result_list.append(unigramCounts[i]/totalCount)
#     # return result_list

# message = [] with open(filename) as file1: 

# txt = file1.read().splitlines() 
# for i in txt: 
#     if len(i) !=0: 
#     message .append( i.split(' ') ) 
#     return message

# txt = "shashidhar is a good boy"
# print("using normal split", txt.split(" ")[0])
# print("using newnline delimeter", txt.split("\n")[0])

def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    result_list=[]
    for i in unigrams:
        if i in unigramCounts:
            result_list.append(unigramCounts[i]/totalCount)
    return result_list

import operator
def getTopWords(count, words, probs, ignoreList):
    result_dict={}
    temp_dict={}
    for i in range(len(words)):
        if i not in ignoreList:
            temp_dict[words[i]]=probs[i]
    sorted_hastags = dict( sorted(temp_dict.items(), key=operator.itemgetter(1),reverse=True))
    for k,y in sorted_hastags.items():
        if len(result_dict) != count and k not in ignoreList:
            result_dict[k]=y
    return result_dict