
from collections import Counter as mset

words1='hello yyyyyyy yzyzyzyzyzyz mellow well yo kellow lellow abcdefhijkl hi is yellow just here to add strings fellow lellow llleow'.split()
letters1='l e l o h m f y z a b w'.replace(' ','')
words2='sad das day mad den foot ball down touch pass play'.split()
letters2='z a d f o n'.replace(' ','')


def findMaxSizeWords(wordlist,letters):
    words,size = [],0
    #test if each word's non-unique intersection is the same length as the word
    for w in wordlist:
        if len(list((mset(w) & mset(letters)).elements()))==len(w)>=size:
            if len(w)>size:
                size,words = len(w),[]
                words.append(w)
            else:
                words.append(w)
    return words,size


largestWords, largestLength = findMaxSizeWords(words1,letters1)
print '1) size=',largestLength,' words=',largestWords

largestWords, largestLength = findMaxSizeWords(words2,letters2)
print '2) size=',largestLength,' words=',largestWords