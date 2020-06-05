from flask import Flask 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def test_route():
    return "burn world"

if __name__ == "__main__":
    app.run()
    