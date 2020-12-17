import argparse
import json
import requests
from bs4 import BeautifulSoup


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


def get_puzzle(url='https://www.nytimes.com/puzzles/spelling-bee'):
    response = requests.get(url)
    html_page = response.text
    soup = BeautifulSoup(html_page, 'html.parser')

    # The answers are in embedded Javascript
    script = str(soup.script.contents[0])
    # Remove the only part of the script that's not json
    script = script[18:]
    return json.loads(script)


def get_answers(day='today'):
    assert(day in ['today', 'yesterday'])
    puzzle = get_puzzle()
    return puzzle[day]['pangrams'], puzzle[day]['answers']


def get_letters(day='today'):
    assert(day in ['today', 'yesterday'])
    puzzle = get_puzzle()
    return puzzle[day]['centerLetter'], puzzle[day]['validLetters']


if __name__ == '__main__':

    # Load words
    dictionary = load_dictionary(DICT_FILENAME)

    # Get letters from CLI args
    parser = argparse.ArgumentParser(description='Process today\'s letters')
    parser.add_argument('letters')
    center_letter, letters = load_letters(parser.parse_args().letters)

    # Go through each dictionary word, seeing if it's a match!
    # Highlight any potential pangrams
    for word in dictionary:
        if center_letter in word and set(word).issubset(letters):
            if set(word) == set(letters):
                print(word, '  <- PANGRAM')
            else:
                print(word)

    # Get the letters from the actual puzzle
    center_letter, all_letters = get_letters()

    # Get the answers from the actual puzzle
    pangrams, answers = get_answers()
