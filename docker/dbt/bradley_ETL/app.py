import flask
import subprocess

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    try:
        subprocess.run(['sh', './bradley_clean_data/scripts.sh'], check=True, text=True)
    except subprocess.CalledProcessError as e:
        return f"Error running the shell script: {e}"
    else:
        return f"Shell script executed successfully."


if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)