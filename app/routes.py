from flask import Blueprint, request, jsonify
from .chatbot import get_response

chatbot_routes = Blueprint('chatbot', __name__)

@chatbot_routes.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        print("📩 Received message:", data)

        message = data.get("message", "")
        if not message:
            return jsonify({"response": "No message provided."}), 400

        response = get_response(message)
        return jsonify({"response": response})
    
    except Exception as e:
        print("❌ Internal Server Error:", str(e))
        return jsonify({"error": str(e)}), 500
