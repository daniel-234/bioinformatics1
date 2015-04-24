def symbol_to_number(symbol):
    ''' (str) -> int

    Return the corresponding integer of the given symbol.

    Precondition: symbol must be one of DNA nucleotides A, C, G, T. 
    
    >>> symbol_to_number('A')
    0
    >>> symbol_to_number('T')
    3
    '''

    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    else:
        return 3


def pattern_to_number(pattern):
    ''' (str) -> int

    Given a DNA string pattern, return its corresponding integer

    >>> pattern_to_number("")
    0
    >>> pattern_to_number("AGT")
    11
    '''
    
    if pattern == "":
        return 0

    last_symbol = pattern[len(pattern) - 1:]
    
    new_pattern = pattern[:len(pattern) - 1]

    return 4 * pattern_to_number(new_pattern) + symbol_to_number(last_symbol)
