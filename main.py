from flask import Flask
from flask_cors import CORS
from app.routes import chatbot_routes

app = Flask(__name__)

# ✅ Allow requests from React
CORS(app, resources={r"/*": {"origins": "https://chatbot-z15l.onrender.com"}})

# Or this for testing (not for production)
# CORS(app)

app.register_blueprint(chatbot_routes)

if __name__ == "__main__":
    app.run(debug=True)
