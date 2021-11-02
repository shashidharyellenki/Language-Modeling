  #2ndfunciton
  length=0
    for line in corpus:
        for word in line:
            length+=1
    return length

def buildVocabulary(corpus):
    uni_value=[]
    for line in corpus:
        for word in line:
            if word not in uni_value:
                uni_value.append(word)
    return uni_value


message = [] with open(filename) as file1: txt = file1.read().splitlines() for i in txt: if len(i) !=0: message .append( i.split(' ') ) return message