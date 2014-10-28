from blog import db
from models import QuizPost

db.create_all()

db.session.add(QuizPost("quiz_A","about A"))
db.session.add(QuizPost("quiz_B","about B"))

db.session.commit()