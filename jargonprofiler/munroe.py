'''
Calculate a 'Munroe' score - what proportion of the text comes from the 1000
most common words in English.
'''

from . import util

import re

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
            text.append(line.decode().strip())
    return text


# Get the most common 1000 words from the file, storing this as a module member.
# So we don't need to load it each time we calculate a score.
common = get_common()
# Stem the words so that they match the form of our tokens
stemmed_common = set(util.stem(common))

def munroe_score(text, exclusions='', verbose=True):
    '''
    Takes raw text, tokenises and stems it, and compares the stems to the set of the stemmed 1000 most common words
    Returns the percentage of words that were in the list of common words
    
    e.g. if output is 0.61, 61% of words were in the list of the 1000 most common. 
    '''
    # Process exclusions
    if exclusions != '':
        exclusions = util.lowercase(re.findall('\w+', exclusions))
    else:
        exclusions = []
    
    # Find all words - alphanumeric strings not separated by punctuation of 1+ length
    words = re.findall('\w+', text)
    
    # Keep a record of how we tagged each item
    tags = ['' for w in words]
    
    # Identify proper nouns
    proper_nouns = util.tag_proper_nouns(text)
    
    # Identify acronyms
    acronyms = util.find_acronyms(text)
    # Tokenise and stem the words. Mark proper nouns and non-alphabetic words in the tag list.
    tokens = []
    for i, word in enumerate(words):
        # Check if the word is a proper noun. If it is, mark it and put an empty string in the list of tokens
        if word in proper_nouns:
            tokens.append('')
            tags[i] = 'proper noun' 
        elif word.lower() in exclusions:
            tokens.append('')
            tags[i] = 'excluded'
        elif word in acronyms:
            tokens.append('')
            tags[i] = 'acronym'            
        else:
            token = util.tokenise(word)
            # If there is more than one token, it means the word was broken by a number, In this case, ignore it
            # If there are no tokens, it means that there were no alphabetic characters in the token. Ignore it
            if len(token) != 1:
                tokens.append('')
                tags[i] = 'not alphabetic'
            else:
                # Stem the word
                tokens.append(util.stem(util.lowercase(token))[0])
            
    

    # Count the number of tokens that are in the most common 1000 words
    munroe = 0
    for i, t in enumerate(tokens):
        if t != '':
            if t in stemmed_common:
                munroe+=1
                tags[i] = 'common'
            else:
                tags[i] = 'not common'
    
    
    # If verbose, return some printed output
    if verbose:
        print('You have '+ str(len(words)) + ' words in your document')
        print('Of these, '+str(munroe)+' are in the most common 1000 words!')
        print('Score: '+str(100*munroe/len([t for t in tokens if t != '']))+'%')
        
    return_dict = {
        'score': munroe/len([t for t in tokens if t != '']),
        'tagged_words': list(zip(words,tags))
    }
    return return_dict


