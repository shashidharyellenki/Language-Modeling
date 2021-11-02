def buildUniformProbs(unigrams):
    dict_={}
    temp_list=[]
    for i  in unigrams:
        if i not in dict_:
            dict_[i]=1
    for x,y in dict_.items():
        temp_list.append(y/len(dict_))
    return temp_list


    def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    result_list=[]
    for i in unigrams:
        if i in unigramCounts:
            result_list.append(unigramCounts[i]/totalCount)
    return result_list