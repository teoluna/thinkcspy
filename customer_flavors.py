from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html><body>
            <h2>Welcome!</h2>
            <form action="/base">
                What's your name? <input type='text' name='username'><br>
                What's your favorite food? <input type='text' name='favfood'><br>
                <input type='submit' value='Continue'>
            </form>
        </body></html>"""

@app.route('/base')
def create_list():
    username = request.args.get('username', 'Danylo')
    favfood = request.args.get('favfood', 'Cookies')
  
    with open('customer_food_data.csv', 'a') as f:
        f.write(username + "," + favfood + "\n") 
    
    return """
        <html><body>
            "You have add data."
        </body></html>"""

@app.route('/customer_food')
def show_data():
    response = """
        <html><body>
            <h1>List of customers and their favorite food:</h1>"""
    
    response2 = """
        </body></html>"""
    
    if os.path.exists('customer_food_data.csv'):
        with open('customer_food_data.csv', 'r+') as f:
            
            for line in f:
                values = line.split(',')

                if len(values) > 1:
                    template = values[0] + " " + values[1]
                    response += str(template) + "<br>"

    return response + response2

# Launch the Flask dev server
app.run(host="localhost", debug=True)