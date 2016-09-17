<<<<<<< HEAD
from flask import render_template
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
=======
from flask import render_template, url_for, redirect
from . import auth
from .oauth import OAuthSignIn
from flask.ext.login import current_user, login_user

@auth.route('/login/', methods=['GET', 'POST'])
>>>>>>> f2d69d82237baac92bfde3a4dc5193c3721c3c2e
def login():
	pass
	return render_template('auth/login.html')

<<<<<<< HEAD
=======
@auth.route('/authorize/<provider>/')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()
    # return render_template('auth/login.html')

@auth.route('/callback/<provider>/')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    oauth = OAuthSignIn.get_provider(provider)
    temp = str(type(oauth))
    social_id, username, email = oauth.callback()
    # return render_template('auth/login.html', code=social_id, grant_type=username, redirect_uri=email)
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('main.index'))
    
    user = User.query.filter_by(social_id=social_id).first()

    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('main.index'))
>>>>>>> f2d69d82237baac92bfde3a4dc5193c3721c3c2e
