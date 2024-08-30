import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import g, Flask, flash, redirect, render_template, url_for
from flask_caching import Cache
from flask_login import LoginManager, current_user
from flask_mail import Mail

from config import Config
from classes.user import User

login_manager = LoginManager()
cache = Cache()
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    login_manager.init_app(app)
    cache.init_app(app)
    mail.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    @app.errorhandler(401)
    def unauthorized(e):
        flash('You need to be logged in to view this page.', 'warning')
        return redirect(url_for('auth.login'))
    
    app.register_error_handler(401, unauthorized)

    @app.before_request
    def load_logged_in_user():
        g.user = current_user
    
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))
    
    from home.routes import Home
    from auth.routes import Auth
    from mycalendar.routes import MyCalendar
    from messaging.routes import Messaging
    from search.routes import Search

    app.register_blueprint(Home, url_prefix='/home')
    app.register_blueprint(Auth, url_prefix='/auth')
    app.register_blueprint(Messaging, url_prefix='/messaging')
    app.register_blueprint(Search, url_prefix='/search')
    app.register_blueprint(MyCalendar, url_prefix='/myCalendar')



    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
