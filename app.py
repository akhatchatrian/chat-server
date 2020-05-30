from flask import Flask 

app = Flask(__name__)

@app.route('/')
def test_route():
    return "hello world"

if __name__ == "__main__":
    app.run()
