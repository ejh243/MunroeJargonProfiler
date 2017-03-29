from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

class TextForm(FlaskForm):
    text = StringField('text')

@app.route('/')
def index():
    form = TextForm()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
