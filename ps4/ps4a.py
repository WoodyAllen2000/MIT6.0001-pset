def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return [sequence]
    else:
        a_sequence = sequence[1: len(sequence)]
        a = sequence[0]
        final_list = []
        for i in get_permutations(a_sequence):
            relay_list = list(i)
            for m in range(len(relay_list) + 1):
                model = relay_list[::]
                model.insert(m, a)
                new_sequence = ''.join(model)
                final_list.append(new_sequence)
        return final_list






if __name__ == '__main__':
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)

    seq = input("请输入一个单词:")
    test_list = get_permutations(seq)
    print(test_list)

