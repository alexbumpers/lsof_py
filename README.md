# lsof_py
lsof_py is a self-hosted solution to getting process information on specific ports using a browser-based GUI. It is built with Flask and Python and is essentially a wrapper around `lsof -i:$PORT_NUMBER`

## Installation and Start
To install, simply clone the git repo and run:
`pip install -r requirements.txt`

Then set `FLASK_APP` equal to the app entry point:
`export FLASK_APP=app.py`

To run, use the following command, and feel free to use your desired port number instead of the given one:
`flask run --host=localhost --port=80`

## Use
Open your browser up to `localhost` and simply enter in the desired port that you'd like to get process information for.


