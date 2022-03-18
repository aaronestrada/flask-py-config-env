from flask import Flask
from flask_py_config_env import FlaskEnvironmentLoader

app = Flask(__name__)

# -----------------------------------------
# Environment loader for Flask application
# -----------------------------------------
env_loader = FlaskEnvironmentLoader(env_file='example')
env_loader.init_app(application=app)


@app.route('/hello')
def index():
    person = app.config.get('VARIABLE_DICT')
    return f'Person - {person.get("name")} {person.get("last_name")}'


if __name__ == '__main__':
    app.run(debug=True)
