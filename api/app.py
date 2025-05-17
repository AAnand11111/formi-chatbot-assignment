from flask import Flask
import json
import os


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/knowledge', methods=['POST'])
def get_knowledge():
    data = request.get_json()
    query = data.get('query', '').lower()

    # Load knowledge base (adjust path if needed)
    kb_path = os.path.join(os.path.dirname(__file__), '../knowledge_base/outlets.json')
    with open(kb_path, 'r') as f:
        knowledge = json.load(f)

    # Simple logic: check for outlet name in query
    for city in knowledge:
        for outlet in knowledge[city]:
            if outlet.replace('_', ' ') in query:
                info = knowledge[city][outlet]
                return jsonify({
                    "outlet": outlet.replace('_', ' ').title(),
                    "contact": info.get("contact", "N/A"),
                    "timings": info.get("timings", {}),
                    "closures": info.get("closures", [])
                })
    return jsonify({"response": "Sorry, I couldn't find info for that outlet."})

