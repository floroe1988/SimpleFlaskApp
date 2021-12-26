from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html = "<h3>Hello better World</h3>"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
