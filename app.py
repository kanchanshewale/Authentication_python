from flask import Flask
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
import logging

app = Flask(__name__)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

@app.route("/")
def home():
    return {"message": "Auth Service Running"}

if __name__ == "__main__":
    app.run(debug=True)
