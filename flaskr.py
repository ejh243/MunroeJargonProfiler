"""
Run Munroe Jargon Profiler Flask app
"""
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask_wtf import FlaskForm
from wtforms import TextAreaField

from jargonprofiler import munroe

# Flask variables
SECRET_KEY = 'development key'

# Flask app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

class TextForm(FlaskForm):
    """
    Form to receive user input of text to be processed.
    """
    text = TextAreaField('text')

@app.route('/', methods=('GET', 'POST'))
def index():
    """
    Index page for Munroe Jargon Profiler Flask app

    It has the form to receive user input
    and provide a visualisation of the result.
    """
    form = TextForm()
    if form.validate_on_submit():
        text = form.data["text"]
        score = munroe.munroe_score(text)
        return render_template(
            'report.html',
            text=colour_text(text, score["tagged_words"]),
            score=score["score"]
        )
    return render_template(
        'index.html',
        form=form
    )

def colour_text(text, word_list):
    """Add colour to text."""
    list_of_words = text.split(" ")  # FIXME This will not get a good match
    coloured_list_of_words = []

    for word in list_of_words:
        if word in word_list:
            coloured_list_of_words.append("<span class=\"text-warning\">{}</span>".format(word))
        else:
            coloured_list_of_words.append(word)

    return " ".join(coloured_list_of_words)

def run(host, port):
    """
    Run Flask app
    """
    app.run(host, port)
