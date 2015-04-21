def pattern_count(text, pattern):
    ''' (str, str) -> (int)

    Return how many times a given pattern appears in text. The program
    accounts for overlapping occurrences.

    Precondition: len(text) > 0

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
            if pattern == text[i:i + 3]:
                count += 1
            i += 1
    
    return count
