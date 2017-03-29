'''
Utility functions useful for multiple scoring metrics.
'''

import re
import nltk

# This NLTK package is needed by tag_proper_nouns
nltk.download('averaged_perceptron_tagger')

# This one is needed by sent_tokenize
nltk.download('punkt')


def tokenise(text):
    '''Takes raw text and returns a list of tokens.

    At present, tokens are:
    - 2+ characters long
    - Alphabetic (numbers are automatically excluded)
    '''
    text = text.encode('ascii', 'ignore').decode('utf-8')
    tokens = re.findall("[A-Za-z]{3,}", text)
    return list(tokens)


def tag_proper_nouns(text):
    '''
    Takes raw text, tags it using a part-of-speech tagger and returns a set of the proper nouns

    Will be slow for large pieces of text!

    Requires averaged_perceptron_tagger from nltk (not all nltk packages are downloaded via pip)
    can get this package by using nltk.download() in python shell
    '''
    proper_nouns = set()
    sentences = nltk.tokenize.sent_tokenize(text)
    for sent in sentences:
        tagged_sent = nltk.tag.pos_tag(tokenise(sent))
        proper_nouns.update([word for word, pos in tagged_sent if pos == 'NNP'])
    return proper_nouns


def find_acronyms(text):
    '''A simple acronym finder using regular expressions.'''
    UU = r"\w*[A-Z][A-Z]\w*"
    U2 = r"\w*\d\w*[A-Z]\w*|\w*[A-Z]\w*\d\w*"
    UlU = r"[A-Z]\w*[A-Z]"
    regex = r"\b(" + UU + r'|' + U2 + r'|' + UlU + r')s?\b'
    return re.findall(regex, text)


def lowercase(tokens):
    '''Given a list of tokens, return a list of the lowercase versions.'''
    return [t.lower() for t in tokens]


def stem(tokens):
    '''Find the stems for each of a list of tokens.

    This returns a standardised form of words, removing 'ing', 's', etc.

    At present we use the Porter stemmer (least aggressive form of stemming).
    Alternates are snowball and lancaster.
    '''
    stemmer = nltk.stem.PorterStemmer()
    return [stemmer.stem(t) for t in tokens]


def read_file(filename):
    '''Read the text from a file as a one-line string.

    Whitespace (newlines etc) is stripped from the ends of each line,
    and the lines joined with a single space character.
    '''
    text = ''
    with open(filename, 'r') as f:
        for line in f:
            text += ' ' + line.strip()
    return text
