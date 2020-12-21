from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    #ORM
    db.init_app(app)
    migrate.init_app(app, db) #config.py파일에 작성한 항목을 app.config환경변수로 부르기 위해

    from . import models #모델가져오기


    #블루프린트
    from .views import main_view, question_views, answer_views
    app.register_blueprint(main_view.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app