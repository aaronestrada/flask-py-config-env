# Python Configuration Environment loader for Flask applications

This extension allows loading configuration files containing variables in a Python script, to then access to them via
the `config` dictionary variable from the Flask application. The extension is built on top of
the [py-config-env](https://github.com/aaronestrada/py-config-env) extension.

## Requirements

* Python >= 3.6
* Flask >= 2.0.3
* [py-config-env](https://github.com/aaronestrada/py-config-env)

## Motivation

Applications might have a configuration file containing variables that will be different in each environment. This
extension reads a configuration file containing variables in Python, to then access to them via the `config` variable
from the Flask application.

## How to use the extension

For more information about the use of the FlaskEnvironmentLoader, please visit
the [py-config-env](https://github.com/aaronestrada/py-config-env) parent repository.

`test_application.py`

```python
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
```

`Run application`

```bash
FLASK_APP=test_application.py FLASK_ENV=development FLASK_DEBUG=1 flask run
```

`cURL to read values from variables`

```bash
curl http://127.0.0.1:5000/hello
```
