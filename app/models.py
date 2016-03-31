class Article(db.Model):
	__tablename__ = 'articles'
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text)
	timestamp = db.Column(db.Datetime, index=True, default=datetime.utcnow)
	