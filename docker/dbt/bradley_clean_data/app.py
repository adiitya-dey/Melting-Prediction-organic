import flask
import subprocess

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    try:
        subprocess.run(['sh', 'scripts.sh'], check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running the shell script: {e}")
    else:
        print(f"Shell script executed successfully.")


    return '<h1>DBT triggered</h1>'


if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)