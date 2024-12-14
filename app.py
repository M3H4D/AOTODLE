from flask import Flask
import db
from routes.home import home_bp
from routes.classic import classic_bp

app = Flask(__name__)

db.create_tables()

app.register_blueprint(home_bp)

app.register_blueprint(classic_bp)

if __name__ == '__main__':
    app.run(debug = True)