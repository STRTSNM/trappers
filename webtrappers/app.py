import model
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_url', methods=['POST'])
def check_url():
    data = request.get_json(silent=True) or {}
    url = data.get("url", "")

    score = 42  

    return jsonify({"score": score})


@app.route('/check_text', methods=['POST'])
def check_text():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")

    score = model.infer(text)

    return jsonify({"score": score})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

