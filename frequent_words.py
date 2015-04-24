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


def frequent_words():
    ''' (file open for reading) -> list

    Return a list of all most frequent k-mers in a given dataset.

    Precondition: Any given dataset should have 4 lines:                
                    line 1 contains the word 'Input';
                    line 2 contains the text to analyze;
                    line 3 contains the value of k;
                    line 4 contains the word 'Output';
                    line 5 contains the expected result. 
        
    '''

    file_name = input("Enter file or hit enter to use a sample dataset: ")

    if len(file_name) < 1 : file_name = "frequentWords.txt"
    dataset = open(file_name, 'r')

    # Make a list of the 5 lines
    lines = dataset.readlines()
    
    dataset.close()

    # Take line 2 as the text to analyze.
    # Then find the index of the first escape character
    # and remove it from the string.
    text = (lines[1])[:lines[1].find('/')]

    # Take line k from line 3.
    # Find the index of the first escape character
    # and remove it from the string.
    # Then cast the result to have an integer number.
    
    k = int((lines[2])[:lines[2].find('/')])

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
           





    
