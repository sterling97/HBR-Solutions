from flask import Flask,jsonify


app = Flask(__name__)


@app.route('../app', methods=['GET'])
def index():
    return jsonify({'Mensaje':'Bienvenido'})


if __name__ == "__main__":
    app.run(debug=True)