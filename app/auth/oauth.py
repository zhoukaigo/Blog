<<<<<<< HEAD
from flask import current_app
=======
from rauth import OAuth2Service
from flask import current_app, url_for, redirect, request, session 
>>>>>>> f2d69d82237baac92bfde3a4dc5193c3721c3c2e

class OAuthSignIn(object):
	providers = None

	def __init__(self, provider_name):
		self.provider_name = provider_name
		credentials = current_app.config['OAUTH_CREDENTIALS'][provider_name]
		self.consumer_id = credentials['id']
		self.consumer_secret = credentials['secret']

	def authorize(self):
		pass

	def callback(self):
		pass

	def get_callback_url(self):
<<<<<<< HEAD
		return url_for('oauth_callback', provider=self.provider_name, _external=True)
=======
		return url_for('auth.oauth_callback', provider=self.provider_name, _external=True)
>>>>>>> f2d69d82237baac92bfde3a4dc5193c3721c3c2e

	@classmethod
	def get_provider(self, provider_name):
		if self.providers is None:
			self.providers = {}
<<<<<<< HEAD
			for provider_class in self.__subclass__():
				provider = proveder_class()
=======
			for provider_class in self.__subclasses__():
				provider = provider_class()
>>>>>>> f2d69d82237baac92bfde3a4dc5193c3721c3c2e
				self.providers[provider.provider_name] = provider
		return self.providers[provider_name]

class FacebookSignIn(OAuthSignIn):
	def __init__(self):
		super(FacebookSignIn, self).__init__('facebook')
		self.service = OAuth2Service(
			name = 'facebook',
			client_id = self.consumer_id,
			client_secret = self.consumer_secret,
			authorize_url = 'https://graph.facebook.com/oauth/authorize',
			access_token_url = 'https://graph.facebook.com/oauth/access_token',
			base_url = 'https://graph.facebook.com/'
		)

	def authorize(self):
<<<<<<< HEAD
		pass

	def callback():
		pass
=======
		return redirect(self.service.get_authorize_url(
			scope='email',
			response_type='code',
			redirect_uri= self.get_callback_url())
		)
		# return '<p>Hello, world!</p>'

	def callback(self):
		if 'code' not in request.args:
			return None, None, None
		data = {'code': request.args['code'], 'grant_type': 'authorization_code', 'redirect_uri': self.get_callback_url()}
		# return data['code'], data['grant_type'], data['redirect_uri']
		oauth_session = self.service.get_auth_session(data=data)
		# return data['code'], data['grant_type'], data['redirect_uri']
		me = oauth_session.get('me?fields=id,email').json()
		return (
			'facebook$' + me['id'],
			me.get('email').split('@')[0],  # Facebook does not provide
											# username, so the email's user
											# is used instead
			me.get('email')
		)
>>>>>>> f2d69d82237baac92bfde3a4dc5193c3721c3c2e


class QQSignIn(OAuthSignIn):
	def __init__(self):
		super(QQSignIn, self).__init__('qq')
		self.service = OAuth2Service(
			name = 'qq',
			client_id = self.consumer_id,
			client_secret = self.consumer_secret,
			authorize_url = 'https://graph.qq.com/oauth2.0/authorize',
			access_token_url = 'https://graph.qq.com/oauth2.0/token',
			base_url = 'https://graph.qq.com/'
		)

	def authorize(self):
		return redirect(self.service.get_authorize_url(
			scope='get_user_info',
			response_type='code',
			state='temp',
			redirect_uri= self.get_callback_url())
		)
		# return '<p>Hello, world!</p>'

	def callback(self):
		if 'code' not in request.args:
			return None, None, None
		# return 'a', 'b', 'c'
		openid_session = self.service.get_auth_session()
		me = oauth_session.get('me?fields=openid').json()
		return me, me, me
		data = {'code': request.args['code'], 'grant_type': 'authorization_code', 'redirect_uri': self.get_callback_url()}
		# return data['code'], data['grant_type'], data['redirect_uri']
		oauth_session = self.service.get_auth_session(data=data)
		# return data['code'], data['grant_type'], data['redirect_uri']
		me = oauth_session.get('me?fields=nickname,year').json()
		return me, me, me
		me = oauth_session.get('me?fields=nickname,year').json()
		return (
			'qq$' + me['id'],
			me.get('email').split('@')[0],  # qq does not provide
											# username, so the email's user
											# is used instead
			me.get('email')
		)