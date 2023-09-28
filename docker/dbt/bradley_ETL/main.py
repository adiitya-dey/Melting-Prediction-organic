import flask
import subprocess

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    try:
        # subprocess.run(['dbt','deps', '--profiles-dir','.', '--project-dir', 'bradley_clean_data/'], check=True, text=True)
        subprocess.run(['dbt','debug','--target','prod', '--profiles-dir','.', '--project-dir', 'bradley_clean_data/'], check=True, text=True)
        subprocess.run(['dbt','run','--target','prod', '--profiles-dir','.', '--project-dir', 'bradley_clean_data/'], check=True, text=True)
    except subprocess.CalledProcessError as e:
        return f"Error running the subprocess: {e}"
    else:
        return f"Subprocess executed successfully."


if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)