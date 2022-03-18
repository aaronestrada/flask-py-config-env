from flask import Flask
from py_config_env import EnvironmentLoader


class FlaskEnvironmentLoader(EnvironmentLoader):
    """
    Class to read environment configuration variables from folder in the root path of the application and set
    to the Flask application configuration

    Each environment file contains the variables that will be stored in a dictionary.
    """

    def init_app(self, application: Flask):
        """
        Initialize Flask application

        :param application: Flask application to initialize with environment variables
        :return:
        """
        # Get variables from file
        variables = self._get_vars()
        for key, value in variables.items():
            application.config[key] = value
