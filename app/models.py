from app import db


class Books(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), index=True)
	type_of_book = db.Column(db.String(64))
	synopsis = db.Column(db.String(512))
	publisher = db.Column(db.String(128))
	publication_date = db.Column(db.DateTime)
	languge = db.Column(db.String(64))
	isbn = db.Column(db.String(64))

	def __repr__(self):
		return 'Book {}'.format(self.name)


class FacebookPosts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	heading = db.Column(db.String(128))
	body = db.Column(db.String(1024))
	publication_date = db.Column(db.DateTime)
	post_link = db.Column(db.String(128))

	def __repr__(self):
		return 'Heading {}'.format(self.heading)
