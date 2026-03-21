from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__, static_folder='.')
CORS(app)

GEMINI_BASE = "https://generativelanguage.googleapis.com"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/proxy/gemini', methods=['POST'])
def proxy_gemini():
    api_key = request.headers.get('X-API-Key')
    if not api_key:
        return jsonify({'error': 'No API key provided'}), 401

    data = request.get_json()
    model = data.get('model', 'gemini-2.0-flash-exp')
    endpoint = f"{GEMINI_BASE}/v1beta/models/{model}:generateContent"

    try:
        resp = requests.post(
            endpoint,
            params={'key': api_key},
            json=data.get('payload'),
            timeout=120
        )
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
