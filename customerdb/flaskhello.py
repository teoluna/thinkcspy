from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html><body>
            <h2>Welcome to the Greeter</h2>
            <form action="/greet">
                What's your name? <input type='text' name='username'><br>
                What's your favorite food? <input type='text' name='favfood'><br>
                <input type='submit' value='Continue'>
            </form>
        </body></html>"""

@app.route('/greet')
def greet():
    username = request.args.get('username', 'World')
    favfood = request.args['favfood']
    if favfood == '':
        msg = 'You did not tell me your favorite food.'
    else:
        msg = 'I like ' + favfood + ', too.'

    return """
        <html><body>
            <h2 style='color:red'>Hello, {0}!</h2>
            {1}
        </html></body>
        """.format(username, msg)

# Launch the Flask dev server
app.run(host="localhost", debug=True)