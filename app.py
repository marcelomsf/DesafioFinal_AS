from flask import Flask
from controllers.cliente.cliente_controller import cliente_bp
from models.cliente import Cliente
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


db.init_app(app)

app.register_blueprint(cliente_bp)

if __name__ == '__main__':
    app.run(debug=True)