from distutils.core import setup

setup(
    name='flask-py-config-env',
    version='1.0',
    description='Read environment variables from configuration file, accessible from a dictionary (adapted to Flask applications)',
    license='BSD',
    author='Aaron Estrada Poggio',
    author_email='aaron.estrada.poggio@gmail.com',
    url='https://github.com/aaronestrada/flask-py-config-env',
    packages=['flask_py_config_env'],
    python_requires='>=3.6',
    install_requires=[
        'Flask>=2.0.3',
        'git+https://git@github.com/aaronestrada/py-config-env.git@1.0'
    ]
)
