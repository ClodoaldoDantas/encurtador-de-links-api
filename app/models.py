from .database import db

class Link(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  original_url = db.Column(db.String(200), nullable=False)
  short_id = db.Column(db.String(10), unique=True, nullable=False)
