import flask


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    print("Hello World")


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)