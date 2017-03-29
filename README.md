# The 'Munroe Meter' Jargon Scoring System

When communicating a complex or unfamiliar concept, jargon creates a barrier for
understanding. There are a number of situations when we are asked to give an explanation
assuming that the audience has no technical or specialised knowledge. This can be
particularly challenging as experts are often unaware when they are using jargon or what
even constitutes jargon. We have developed a tool that identifies jargon, gives the
user a metric to rate the jargon content, and makes suggestions for alternatives.

It improves upon existing tools in this space in many ways:

1. it makes use of the Munroe approach to characterising common language (top 1000 words)
2. it provides many alternative definitions of jargon, including subject-specific lists
3. it enables the user to exclude up to five key words from the jargon score without which
   the article would lose its meaning
4. it provides multiple outputs:
    * multiple metrics based on different definitions of jargon
    * a highlighted version of the text identifing which words to change
    * a word cloud representing the text distinguishing jargon from common words.

This software is designed to take some text (in US English) and calculate the proportion of commonly used words.
A score of 0% means all of the words are jargon, a score of 100% means none of the words are jargon.
Proper nouns, single characters, abbreviations and numbers are excluded from the calculation.
Words are also reduced to their stem
(i.e. plurals are singularised;
the past/future tense is transformed to present tense)
to reduce the false positive rate.

The software can calculate multiple metrics where jargon is classified in several ways.

## Jargon classifications

The first of these is implemented already; others will be added (see issues list on GitHub).

* Munroe: Any word outside of the 1000 most common English words is characterised as jargon.
* Basic English defined by Ogden.
* Words used by a typical 12 year old.
* Output of Lancaster Corpus of Children's Project Writing.
* Commonly used words in specific scientific domains.

## Key future functionality planned

Issue #30 - Flag other charcteristics associated with a high-level comprehension including:
- Any number less than 20 should written out.
- Avoid the use of slashes, especially instead of writing "or".
- Avoid special symbols, particularly things like: ±, ≥, …
- Avoid the use of acronyms.

Issue #14 - Check for it being English, spelling and grammar before analysing.

Issue #31 - Return word cloud with jargon and common words coloured differently.

Issue #13 - Take sound files/clips, transcibe them into text and analyse.

## Running the software

TODO: Some instructions for users wanting just to run the system locally.
Link to a hosted version.

## Getting started as a developer

It is best practice to work on Python projects within a virtual environment,
to avoid conflicts with your main system installation. The `virtualenv` tool
can be installed following the instructions at
https://virtualenv.pypa.io/en/stable/installation/

Clone this Git repository, then navigate to the folder where you cloned it
in a terminal and run the following sequence of commands to set up a virtual
environment and install all the project's dependencies.

(Note for Windows users: these assume a POSIX-style shell, so will work in
git-bash, but not the standard Windows shell. For that, you'll probably need
`python3.exe` in place of `python3`, and `venv\Scripts\activate` as the
second line.)

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

Installing with conda in its own environment.
```
# create conda environment based on environment.yml file
conda env create
# activate the environment
source activate JargonProfiler
```

### Testing

Testing is being done using [pytest][pytest]. To run all the tests, just use

```
pytest test
```

New tests should be written in files inside the `test` folder, named either
`test_*.py` or `*_test.py`. The tests themselves are functions with names
starting `test_` and taking no arguments. They check expected behaviour using
`assert` statements.

See the [pytest documentation][test-discovery] for more details.

### Updating requirements

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

## Download static file

```
bower install
```

## Flask

```
python runserver.py
```

[pytest]: http://doc.pytest.org/en/latest/contents.html
[pip-tools]: https://github.com/nvie/pip-tools
[test-discovery]: http://doc.pytest.org/en/latest/goodpractices.html#test-discovery
