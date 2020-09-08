from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """<html><body>
        <h1>Hello, world!</h1>
        Click <a href='/red'>here</a> for the text in red.
        The time is {0}.</body></html>""".format(
            str(datetime.now()))

@app.route('/red')
def hello_red():
    return """<html><body>
    <h2 style='color:red'>Hello, world!</h2>
    </html></body>"""

# Launch the Flask dev server
app.run(host="0.0.0.0", port=80, debug=True)