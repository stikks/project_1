
class BaseConfig(object):
	SECRET_KEY = 'anok-si-na-moon'
	SQLALCHEMY_DATABASE_URI = "sqlite:///quizzes.db"
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False