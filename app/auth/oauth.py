from flask import current_app

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
		return url_for('oauth_callback', provider=self.provider_name, _external=True)

	@classmethod
	def get_provider(self, provider_name):
		if self.providers is None:
			self.providers = {}
			for provider_class in self.__subclass__():
				provider = proveder_class()
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
		pass

	def callback():
		pass

	