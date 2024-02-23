from flask import Flask, session, g
import config
from exts import db, mail
from models import UserModel
from blueprints.search import bp as search_bp
from blueprints.user import bp as user_bp
from blueprints.bertopic_analysis import bp as analysis_bp

from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(search_bp)
app.register_blueprint(user_bp)
app.register_blueprint(analysis_bp)


@app.before_request
def my_before_request():
    user_email = session.get("user_id")
    if user_email:
        user = UserModel.query.filter( UserModel.email == user_email ).first()
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)


@app.context_processor
def my_context_processor():
    return {"user": g.user}


if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0')