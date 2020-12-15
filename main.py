import argparse


DICT_FILENAME = 'dictionary.txt'


def load_dictionary(filename):
    ''' Load a file containing all possible words. '''
    with open(filename, 'r') as dictfile:
        dict_words = list(dictfile)
    dict_words = list(map(str.strip, dict_words))
    dict_words = list(map(str.lower, dict_words))
    return filter(lambda x: len(x) > 3, dict_words)


def load_letters(l):
    ''' Load today's letters. Assume first letter is the center letter '''
    center_letter = l[0]
    assert len(set(l)) == 7
    return center_letter, set(l)


if __name__ == '__main__':

    # Set up
    parser = argparse.ArgumentParser(description='Process today\'s letters')
    parser.add_argument('letters')
    dictionary = load_dictionary(DICT_FILENAME)
    center_letter, letters = load_letters(parser.parse_args().letters)

    # Go through each dictionary word, seeing if it's a match!
    # Highlight any potential pangrams
    for word in dictionary:
        if center_letter in word and set(word).issubset(letters):
            if set(word) == set(letters):
                print(word, '  <- PANGRAM')
            else:
                print(word)
