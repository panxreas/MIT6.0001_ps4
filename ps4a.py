# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    l = []
    
    if len(sequence) == 1:
        return list(sequence)
    else:
        recursion = get_permutations(sequence[1:])
        next_val = sequence[0]
        for items in recursion:

            for char in range(len(items) + 1):
                letters = list(items)
                letters.insert(char, next_val)
                l.append(''.join(letters))
                letters = []
    
    return l
    




print(sorted(list(set(get_permutations("smash")))))






if __name__ == '__main__':

    pass 

