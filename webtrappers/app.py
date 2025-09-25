import model
from flask import Flask, request, jsonify

app = Flask(__name__)

#curl -X POST http://127.0.0.1:5000/check_url      -H "Content-Type: application/json"      -d '{"url": "https://google.com"}'

@app.route('/check_url', methods=['POST'])
def check_url():
    data = request.get_json(silent=True) or {}
    url = data.get("url", "")

    score = model.inferURL(url)
    print("URL : ", score)

    return jsonify({"score": score})


@app.route('/check_text', methods=['POST'])
def check_text():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")

    score = model.inferText(text)

    return jsonify({"score": score})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

