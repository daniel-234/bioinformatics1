def number_to_symbol(index):
    ''' (int) -> str

    Return the corresponding symbol of the given integer.

    Precondition: 0 <= symbol <= 4. 
    
    >>> number_to_symbol(0)
    'A'
    >>> number_to_symbol(3)
    'T'
    '''

    if index == 0:
        return 'A'
    elif index == 1:
        return 'C'
    elif index == 2:
        return 'G'
    else:
        return 'T'


def number_to_pattern(index, k):
    ''' (int, int) -> str

    Given an index, return its corresponding pattern. 

    >>> number_to_pattern(45, 4)
    'AGTC'
    >>> number_to_pattern(5353, 7)
    'CCATGGC'
    >>> number_to_pattern(7867, 8)
    'ACTGGTGT'
    '''
    
    if k == 1:
        return number_to_symbol(index)

    # prefix_index is the quotient of the division of
    # index by 4
    prefix_index = index // 4

    # the remainders of the same disvision gives us
    # the pattern indexes
    remainder = index % 4

    # find the corresponding pattern symbol
    symbol = number_to_symbol(remainder)

    # The first symbol found is the last to appear in pattern
    return number_to_pattern(prefix_index, k - 1) + symbol
