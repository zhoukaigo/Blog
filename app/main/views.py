from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/archives/')
def archives():
    return render_template('archives.html')

@main.route('/about/')
def about():
    return render_template('about.html')

@main.route('/resume/')
def resume():
    return render_template('resume.html')
