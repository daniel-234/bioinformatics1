def pattern_count():
    ''' (file open for reading) -> int

    Return how many times a given pattern appears in text. The program
    accounts for overlapping occurrences.

    Precondition: Any given dataset should have 5 lines:                
                    line 1 contains the word 'Input';
                    line 2 contains the text to analyze;
                    line 3 contains the pattern to search for in text;
                    line 4 contains the word 'Output';
                    line 5 contains the expected result. 
    '''


    file_name = input("Enter file or hit enter to use a sample dataset: ")

    if len(file_name) < 1 : file_name = "PatternCount.txt"
    dataset = open(file_name, 'r')

    # Make a list of the 5 lines
    lines = dataset.readlines()
    
    dataset.close()

    # Take line 2 as the text to analyze.
    # Then find the index of the first escape character
    # and remove it from the string.
    text = (lines[1])[:lines[1].find('/')]
    
    # Take line 3 as the pattern to search for in text.
    # Then find the index of the first escape character
    # and remove it from the string.
    pattern = (lines[2])[:lines[2].find('/')]

    # Take line 5 as the desired output.
    # Find the index of the first escape character
    # and remove it from the string.
    # Then cast the result to have an integer number. 
    given_output = int((lines[4])[:lines[4].find('/')])

    # Count the occurrences
    count = 0
    i = 0

    # Pattern is expected to be shorter than text
    if pattern == '' or (len(text) < len(pattern)):
        return 0
    else:
        # The search should stop when the last portion of
        # text to analyze is equal to the length of pattern.
        # The next slice would give a text shorter than pattern.
        while(i < (len(text) - len(pattern) + 1)):
            if pattern == text[i:i + len(pattern)]:
                count += 1
            i += 1
    
    if count == given_output:
        return count
    else:
        return "Result = " + str(count) + " do not correspond to given output"
