# The 'Munroe Meter' Jargon Scoring System

## Getting started as a developer

It is best practice to work on Python projects within a virtual environment,
to avoid conflicts with your main system installation. The `virtualenv` tool
can be installed following the instructions at
https://virtualenv.pypa.io/en/stable/installation/

Clone this Git repository, then navigate to the folder where you cloned it
in a terminal and run the following sequence of commands to set up a virtual
environment and install all the project's dependencies.

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r test_requirements.txt  # For testing
```

You can then install the project package itself in 'developer mode', so that
changes made to files in your working copy are reflected in the installed
package too:

```
pip install -e .
```

Testing is being done using [pytest][pytest]. To run all the tests, just use

```
pytest
```

The `requirements.txt` file used above is generated from a specification in
`requirements.in` by [pip-tools][pip-tools]. This ensures that we list the
exact versions used of all our dependencies, including indirect ones. If you
are adding a new dependency, add it to `requirements.in` and then run

```
pip install pip-tools  # First time only!
pip-compile
```

To upgrade dependencies to their latest versions use

```
 pip-compile --upgrade
 ```

[pytest]: http://doc.pytest.org/en/latest/contents.html
[pip-tools]: https://github.com/nvie/pip-tools

## Notes for users on how the JargonProfiler works.

This software is designed to take some text (in U.S English) and calculate the proportion of commonly used words: A score of 0% means all of the words are jargon, a score for 100% means none of the words are jargon.
Proper nouns, single characters, abbreviations and numbers are excluded from the calculation. Words are also reduced to their stem (i.e. plurals are singularised; the past/future tense is transformed to present tense) 
Users have the option to specify up to 5 key words which will be excluded from the Jargon detector and therefore ignored when caluclating the score.


The software can calculate multiple metrics where Jargon is classified in several ways.

###Jargon classifications:

Munroe: Any word outside of the 1000 most common english words is characterised as jargon.

###FUTURE DEFINITIONS OF JARGON TO IMPLEMENT (GIT ISSUE #21)
Basic English defined by Ogden
Words used by a typical 12 year old 
Output of Lancaster Corpus of Children's Project Writing 
Commonly used words in Biology
Commonly used words in 

### FUTURE FUNCTIONAILITY TO IMPLEMENT 
GIT ISSUE #30:
Flag other charcteristics associated with a high-level comprehension including:
Any number less than 20 should written out.
Avoid the use of slashes, especially instead of writing "or".
Avoid special symbols, particularly things like: ±, ≥, …
Avoid the use of acronyms.

GIT ISSUE #14:
Check english language, spelling and grammer before analysing.

Return text with jargon words highlighted

GIT ISSUE #31
Return word cloud with jargon and common words coloured differently

GIT ISSUE #13
Take sound files/clips transcibe into text and analyse.
