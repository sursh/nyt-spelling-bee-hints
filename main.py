def load_dictionary(filename):
    with open(filename, 'r') as dictfile:
        dict_words = list(dictfile).strip().lower()
    return dict_words


def load_letters(l):
    ''' Assume first letter is the center letter '''
    center_letter = l[0]
    assert len(set(l)) == 7
    return center_letter, set(l)


if __name__ == '__main__':

    dict_filename = 'dictionary.txt'
    dictionary = load_dictionary(dict_filename)

    # TODO load these with args
    center_letter, letters = load_letters('hlucant')

    for word in dictionary:
        if center_letter in word and set(word).issubset(letters):
            print(word)
