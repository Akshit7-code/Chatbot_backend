from flask import Flask
from flask_cors import CORS
from app.routes import chatbot_routes
import os  # 🔥 Needed for PORT env var

app = Flask(__name__)

# ✅ Allow requests from your frontend domain
CORS(app, resources={r"/*": {"origins": "https://chatbot-z15l.onrender.com"}})

app.register_blueprint(chatbot_routes)

if __name__ == "__main__":
    # ✅ Bind to 0.0.0.0 and use Render's PORT env var
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
