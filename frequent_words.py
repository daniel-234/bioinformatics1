def pattern_count(text, pattern):
    ''' (str, str) -> (int)

    Return how many times a given pattern appears in text. The program
    accounts for overlapping occurrences.
    Assume len(text) > 0.

    >>> pattern_count('GCGCG', '')
    0
    >>> pattern_count('GCGCG', 'AT')
    0
    >>> pattern_count('G', 'AT')
    0
    >>> pattern_count('GCGCG', 'GCG')
    2
        
    '''

    count = 0
    i = 0

    if pattern == '' or (len(text) < len(pattern)):
        return 0
    else:
        while(i < (len(text) - len(pattern) + 1)):
            if pattern == text[i:i + len(pattern)]:
                count += 1
            i += 1
    
    return count


def frequent_words(text, k):
    ''' (str, int) -> str

    Return all most frequent k-mers in text.

    Precondition: k > 0
    
    >>> frequent_words('ACTGT', 1)
    T
    >>> frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)
    CATG GCAT
    '''

    # a list to store the most frequent words
    fPatterns = []
    # a list to store how many times a specific word appears
    count = []

    # populates count going through text; it stops at |text| - k
    # where it begins the last word of length k
    for i in range(len(text) - k):
        pattern = text[i:i+k]
        count.append(pattern_count(text, pattern))

    # the higher value in list count is the higher frequency
    maxCount = max(count)

    # each word with that frequency is a most frequent word
    for i in range(len(text) - k):
        if(count[i] == maxCount):
            fPatterns.append(text[i:i+k])

    frequentPatterns = []

    # remove duplicates and use frequentPattern to store single
    # values
    for i in range(len(fPatterns)):
        if fPatterns[i] not in frequentPatterns:
            frequentPatterns.append(fPatterns[i])

    print(" ".join(frequentPatterns))

    return frequentPatterns
           





    
