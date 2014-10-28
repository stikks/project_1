from blog import db

class QuizPost(db.Model):
	__tablename__ = "quizzes"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	about = db.Column(db.String, nullable=False)

	def __init__(self, name, about):
		self.name = name
		self.about = about

	def __repr__(self):
		return "{}-{}".format(self.name, self.about) 