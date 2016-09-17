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
<<<<<<< HEAD
    return render_template('about.html')

@main.route('/resume/')
def resume():
    return render_template('resume.html')
=======
    return render_template('about.html')
>>>>>>> f2d69d82237baac92bfde3a4dc5193c3721c3c2e
