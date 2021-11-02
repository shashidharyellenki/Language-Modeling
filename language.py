"""
Language Modeling Project
Name:shashidhar
Roll No:
"""
# import numpy as np
# import matplotlib.pyplot as plt
from os import read
import language_tests as test

project = "Language" # don't edit this

### WEEK 1 ###

'''
loadBook(filename)
#1 [Check6-1]
Parameters: str
Returns: 2D list of strs
'''
def loadBook(filename):
    open_ = open(filename,"r")
    row=[]
    for line in open_.readlines():
        # print("line:",line)
        temp=[]
            # print("length:",len(line))
        for i in line.split(" "):
            if i!= "\n":
                temp.append(i.strip())
        row.append(temp)
    # print(row)
    return row

# print(loadBook("./data/test2.txt"))
'''
getCorpusLength(corpus)
#2 [Check6-1]
Parameters: 2D list of strs
Returns: int
'''
def getCorpusLength(corpus):
    length=0
    for line in corpus:
        for word in line:
            length+=1
    return length
    


'''
buildVocabulary(corpus)
#3 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def buildVocabulary(corpus):
    uni_value=[]
    for line in corpus:
        for word in line:
            if word not in uni_value:
                uni_value.append(word)
    return uni_value


'''
countUnigrams(corpus)
#4 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countUnigrams(corpus):
    uni_dict={}
    for line in corpus:
        for word in line:
            if word not in uni_dict:
                uni_dict[word]=1
            else:
                uni_dict[word]+=1
    return uni_dict


'''
getStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def getStartWords(corpus):
    start_word=[]
    for word in corpus:
        if word[0] not in start_word:
            start_word.append(word[0])
    return start_word


'''
countStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countStartWords(corpus):
    start_dictionary={}
    for word in corpus:
        if word[0] not in start_dictionary:
            start_dictionary[word[0]]=1
        else:
            start_dictionary[word[0]]+=1
    return start_dictionary


'''
countBigrams(corpus)
#6 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def countBigrams(corpus):
    dict_ = {} 
    for i in corpus: 
        for j in range(len(i)-1): 
            if i[j] not in dict_: 
                dict_[i[j]] = {} 
            if i[j+1] not in dict_[i[j]]: 
                dict_[i[j]][i[j+1]] = 1 
            else: dict_[i[j]][i[j+1]] +=1 
    return dict_
    


### WEEK 2 ###

'''
buildUniformProbs(unigrams)
#1 [Check6-2]
Parameters: list of strs
Returns: list of floats
'''
def buildUniformProbs(unigrams):
    dict_={}
    temp_list=[]
    for i  in unigrams:
        if i not in dict_:
            dict_[i]=1
    for x,y in dict_.items():
        temp_list.append(y/len(dict_))
    return temp_list


'''
buildUnigramProbs(unigrams, unigramCounts, totalCount)
#2 [Check6-2]
Parameters: list of strs ; dict mapping strs to ints ; int
Returns: list of floats
'''
def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    result_list=[]
    for i in unigrams:
        if i in unigramCounts:
            result_list.append(unigramCounts[i]/totalCount)
    return result_list


'''
buildBigramProbs(unigramCounts, bigramCounts)
#3 [Check6-2]
Parameters: dict mapping strs to ints ; dict mapping strs to (dicts mapping strs to ints)
Returns: dict mapping strs to (dicts mapping strs to (lists of values))
'''
def buildBigramProbs(unigramCounts, bigramCounts):
    nesteddict = {}
    for prevWord in bigramCounts:
        word = []
        prob = []
        for key,value in bigramCounts[prevWord].items():
            word.append(key)
            prob.append(value / unigramCounts[prevWord]) 
            temp = {}
            temp["words"] =word
            temp["probs"] = prob
        nesteddict[prevWord] = temp
    return nesteddict
   


'''
getTopWords(count, words, probs, ignoreList)
#4 [Check6-2]
Parameters: int ; list of strs ; list of floats ; list of strs
Returns: dict mapping strs to floats
'''
import operator
def getTopWords(count, words, probs, ignoreList):
    result_dict={}
    temp_dict={}
    for i in range(len(words)):
        if words[i] not in ignoreList:
            temp_dict[words[i]]=probs[i]
    sorted_hastags = dict( sorted(temp_dict.items(), key=operator.itemgetter(1),reverse=True))
    for k,y in sorted_hastags.items():
        if len(result_dict) != count and k not in ignoreList:
            result_dict[k]=y
    return result_dict 
# print(getTopWords(3, 
#         [ "hello", "and", "welcome", "to", "15-110", ".", "we're", "happy", "have", "you"], 
#         [ 1/12, 1/12, 1/12, 2/12, 1/12, 2/12, 1/12, 1/12, 1/12, 1/12 ], 
#         [ ".", "hello", "and", "15-110", "we're", "have", "you"]))


'''
generateTextFromUnigrams(count, words, probs)
#5 [Check6-2]
Parameters: int ; list of strs ; list of floats
Returns: str
'''
from random import choices
def generateTextFromUnigrams(count, words, probs):
    str_=""
    for i in range(count):
        temp = choices(words, weights=probs)
        # print(temp)
        str_+=temp[0]+" "
    return str_
# words = [ "hello", "world", "again" ]
# probs = [ 2/5, 2/5, 1/5 ]
# sentence = generateTextFromUnigrams(5, words, probs)
# print(sentence)


'''
generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs)
#6 [Check6-2]
Parameters: int ; list of strs ; list of floats ; dict mapping strs to (dicts mapping strs to (lists of values))
Returns: str
'''
def generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs):
    sentence = ""
    rword = choices(startWords, weights = startWordProbs)
    sentence += rword[0]
    lst = sentence
    for i in range(count-1):
        if lst != '.':
            if lst in bigramProbs:
                lst = choices(bigramProbs[lst]["words"], weights = bigramProbs[lst]["probs"])[0]
                sentence = sentence + ' ' + lst
        else:
            rword = choices(startWords, weights = startWordProbs)
            sentence =sentence+' '+ rword[0]
            lst = rword[0]
    return sentence
    


### WEEK 3 ###

ignore = [ ",", ".", "?", "'", '"', "-", "!", ":", ";", "by", "around", "over",
           "a", "on", "be", "in", "the", "is", "on", "and", "to", "of", "it",
           "as", "an", "but", "at", "if", "so", "was", "were", "for", "this",
           "that", "onto", "from", "not", "into" ]

'''
graphTop50Words(corpus)
#3 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
import matplotlib.pyplot as plt
def graphTop50Words(corpus):
    vocabulary = buildVocabulary(corpus)
    count= countUnigrams(corpus)
    length = getCorpusLength(corpus)
    unique_prob = buildUnigramProbs(vocabulary,count,length)
    result = getTopWords(50, vocabulary, unique_prob, ignore)
    return barPlot(result,"top-50-words")


'''
graphTopStartWords(corpus)
#4 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTopStartWords(corpus):
    words = getStartWords(corpus)
    count=countStartWords(corpus)
    uni_code = buildUnigramProbs(words, count,len(corpus))
    result = getTopWords(50,words,uni_code,ignore)
    # print(len(result))
    return barPlot(result,"first-word")
    
    
# corpuss = loadBook("data/test1.txt")
# print("this function:",graphTopStartWords(corpuss))
'''
graphTopNextWords(corpus, word)
#5 [Hw6]
Parameters: 2D list of strs ; str
Returns: None
'''
def graphTopNextWords(corpus, word):
    uni_count = countUnigrams(corpus)
    bigram_count = countBigrams(corpus) #dict
    words = buildUnigramProbs([i for i in bigram_count[word]],bigram_count[word],sum(bigram_count[word].values()))#3rd
    # next_word = buildBigramProbs(uni_count, bigram_count)
    top_10 = getTopWords(10,[i for i in bigram_count[word]], words, ignore)
    return barPlot(top_10, "topNextWords")


'''
setupChartData(corpus1, corpus2, topWordCount)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int
Returns: dict mapping strs to (lists of values)
'''
def setupChartData(corpus1, corpus2, topWordCount):
    corpus_1_voc, corpus_2_voc= buildVocabulary(corpus1), buildVocabulary(corpus2)
    corpus_1_count, corpus_2_count = countUnigrams(corpus1),countUnigrams(corpus2)
    corpus_1_length, corpus_2_length = getCorpusLength(corpus1),getCorpusLength(corpus2)
    probs_1_corpus, probs_2_corpus = buildUnigramProbs(corpus_1_voc,corpus_1_count, corpus_1_length ),buildUnigramProbs(corpus_2_voc,corpus_2_count, corpus_2_length ) #probs untayi shashidhar
    top_n_corpus1,top_n_corpus2 = getTopWords(topWordCount,corpus_1_voc,probs_1_corpus,ignore),getTopWords(topWordCount,corpus_2_voc,probs_2_corpus,ignore)
    list_=[]
    for k,y in top_n_corpus1.items():
        list_.append(k)
    for a,z in top_n_corpus2.items():
        if a not in list_:
            list_.append(a)
    prob1_list=[]
    prob2_list=[]
    for key in range(len(list_)):
        if list_[key] in corpus_1_voc:
            index_ = corpus_1_voc.index(list_[key])
            prob1_list.append(probs_1_corpus[index_])
        else:
            prob1_list.append(0)
        if list_[key] in corpus_2_voc:
            index2 = corpus_2_voc.index(list_[key])
            prob2_list.append(probs_2_corpus[index2])
    result_dict={}
    result_dict["topWords"] = list_
    result_dict["corpus1Probs"]=prob1_list
    result_dict["corpus2Probs"] = prob2_list
    return result_dict


'''
graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; str ; 2D list of strs ; str ; int ; str
Returns: None
'''
def graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title):
    data = setupChartData(corpus1, corpus2,numWords)
    sideBySideBarPlots(data['topWords'], data['corpus1Probs'], data['corpus2Probs'], name1, name2, title)
    return


'''
graphTopWordsInScatterplot(corpus1, corpus2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int ; str
Returns: None
'''
def graphTopWordsInScatterplot(corpus1, corpus2, numWords, title):
    data = setupChartData(corpus1,corpus2,numWords)
    scatterPlot(data['corpus1Probs'], data['corpus2Probs'], data['topWords'],title)
    return


### WEEK 3 PROVIDED CODE ###

"""
Expects a dictionary of words as keys with probabilities as values, and a title
Plots the words on the x axis, probabilities as the y axis and puts a title on top.
"""
def barPlot(dict, title):
    import matplotlib.pyplot as plt

    names = []
    values = []
    for k in dict:
        names.append(k)
        values.append(dict[k])

    plt.bar(names, values)

    plt.xticks(rotation='vertical')
    plt.title(title)

    plt.show()

"""
Expects 3 lists - one of x values, and two of values such that the index of a name
corresponds to a value at the same index in both lists. Category1 and Category2
are the labels for the different colors in the graph. For example, you may use
it to graph two categories of probabilities side by side to look at the differences.
"""
def sideBySideBarPlots(xValues, values1, values2, category1, category2, title):
    import matplotlib.pyplot as plt

    w = 0.35  # the width of the bars

    plt.bar(xValues, values1, width=-w, align='edge', label=category1)
    plt.bar(xValues, values2, width= w, align='edge', label=category2)

    plt.xticks(rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Note that this limits the graph to go from 0x0 to 0.02 x 0.02.
"""
def scatterPlot(xs, ys, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xs, ys)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xs[i], ys[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.xlim(0, 0.02)
    plt.ylim(0, 0.02)


    # a bit of advanced code to draw a y=x line
    ax.plot([0, 1], [0, 1], color='black', transform=ax.transAxes)

    plt.show()
# scatterPlot([1,2,3],[10,15,16] ,["A","B","V",],"testing scatterplot")


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    # print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    # test.week1Tests()
    # print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    # test.runWeek1()

    ## Uncomment these for Week 2 ##

    # print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    # test.week2Tests()
    # print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    # test.runWeek2()


    ## Uncomment these for Week 3 ##

    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    test.runWeek3()

    # test.testLoadBook()
    # test.testGetCorpusLength()
    # test.testBuildVocabulary()
    # test.testCountUnigrams()4
    # test.testGetStartWords()
    # test.testCountStartWords()
    # test.testBuildUniformProbs()
    # test.testBuildUnigramProbs()
    # test.testGetTopWords()
    # test.testGenerateTextFromUnigrams()
    # test.testGenerateTextFromBigrams()