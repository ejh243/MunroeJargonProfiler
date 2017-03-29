"""
Run Munroe Jargon Profiler Flask app
"""
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField

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
    text = StringField('text')

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
            text=text,
            score=score
        )
    return render_template(
        'index.html',
        form=form
    )

def run(host, port):
    """
    Run Flask app
    """
    app.run(host, port)
