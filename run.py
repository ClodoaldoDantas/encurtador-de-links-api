import os
from flask import Flask
from flasgger import Swagger
from app.models import db
from app.routes import bp

def create_app():
  app = Flask(__name__)

  swagger_template = {
    "info": {
        "title": "API de Links",
        "version": "1.0.0",
        "description": "API para criar e listar links encurtados"
    }
  }

  Swagger(app, template=swagger_template)

  BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
  db_path = os.path.join(BASE_DIR, 'links.db')

  app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)
  app.register_blueprint(bp)

  with app.app_context():
    db.create_all() 

  return app

app = create_app()

if __name__ == "__main__":
  app.run(debug=True)