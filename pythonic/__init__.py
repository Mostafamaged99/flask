from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_modals import Modal
from pythonic.config import Config
#from flask_admin import Admin

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate(db)
login_manager = LoginManager()
ckeditor = CKEditor()
modal = Modal()
#admin = Admin()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    modal.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)

    from pythonic.lessons.routes import lessons
    from pythonic.users.routes import users
    from pythonic.main.routes import main
    from pythonic.courses.routes import courses_bp
    from pythonic.errors.handlers import errors
    from pythonic.adminbp.routes import admin_bp

    app.register_blueprint(main)
    app.register_blueprint(courses_bp)
    app.register_blueprint(lessons)
    app.register_blueprint(users)
    app.register_blueprint(errors)
    app.register_blueprint(admin_bp)

    return app