from flask import Flask
from controllers.cliente.cliente_controller import cliente_bp

app = Flask(__name__)
app.register_blueprint(cliente_bp)

if __name__ == '__main__':
    app.run(debug=True)