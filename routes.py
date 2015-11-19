import os
from flask import Flask, render_template, request
from forms import ContactForm

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    return 'Form posted.'

  elif request.method == 'GET':
    return render_template('contact.html', form=form)
