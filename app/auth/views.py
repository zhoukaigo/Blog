from flask import render_template
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
	pass
	return render_template('auth/login.html')

