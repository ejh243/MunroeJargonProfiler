'''
Calculate a 'Munroe' score - what proportion of the text comes from the 1000
most common words in English.
'''

from . import util


def get_common():
    '''
    Opens the text file containing the list of 1000 most common words found at
    http://www.ef.co.uk/english-resources/english-vocabulary/top-1000-words/
    removes the newlines and returns them as a list.
    '''
    from pkg_resources import resource_stream
    text = []
    with resource_stream(__name__, '1000common.txt') as f:
        for line in f:
            if line.endswith('\n'):
                text.append(line[0:-1])
            else:
                text.append(line)
    return text


# Get the most common 1000 words from the file, storing this as a module member.
# So we don't need to load it each time we calculate a score.
common = get_common()


def munroe_score(text, verbose=True):
    '''
    Takes raw text, tokenises and stems it, and compares the stems to the set of the stemmed 1000 most common words
    Returns the percentage of words that were in the list of common words

    e.g. if output is 0.61, 61% of words were in the list of the 1000 most common.
    '''
    # Identify proper nouns
    proper_nouns = util.tag_proper_nouns(text)

    # Tokenise text
    all_tokens = util.tokenise(text)

    # Keep a record of how we tagged each item
    tags = ['' for t in all_tokens]

    # Locate proper nouns in text and tag them
    for i, token in enumerate(all_tokens):
        if token in proper_nouns:
            tags[i] = 'proper noun'

    # Remove proper nouns from text
    for proper_noun in proper_nouns:
        tokens = [t for t in all_tokens if t != proper_noun]

    # Make the remaining tokens lowercase and stem them
    stems = util.stem(util.lowercase(tokens))

    # Stem the words so that they match the form of our tokens
    stemmed_common = set(util.stem(common))

    # Count the number of tokens that are in the most common 1000 words
    munroe = 0
    for i, s in enumerate(stems):
        if s in stemmed_common:
            munroe += 1
            tags[i] = 'common'
        else:
            tags[i] = 'not common'

    # If verbose, return some printed output
    if verbose:
        print('You have ' + str(len(stems)) + ' words in your document')
        print('Of these, ' + str(munroe) + ' are in the most common 1000 words!')
        print('Score: ' + str(munroe / len(stems)) + '%')

    return_dict = {
        'basic_score': munroe / len(stems),
        'tagged_words': list(zip(tokens, tags))
    }
    return return_dict
