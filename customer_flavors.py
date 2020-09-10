from flask import Flask, request
from datetime import datetime
import os
import mysql.connector

# create connection to the db
mydb = mysql.connector.connect(user='root', password='root', 
host='127.0.0.1', database='mydb')

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html><body>
            <h2>New customer record</h2>
            <form action="/base">
                What's your name? <input type='text' name='username'><br>
                What's your favorite food? <input type='text' name='favfood'><br>
                <input type='submit' value='Submit'>
            </form>
        </body></html>"""

@app.route('/base')
def create_list():
    username = request.args.get('username', 'Danylo')
    favfood = request.args.get('favfood', 'Cookies')
  
    sql = "INSERT INTO customers (name, food) VALUES (%s, %s)"
    val = (username, favfood)
    mycursor.execute(sql, val)

    # make changes to the table 
    mydb.commit()
    
    return """
        <html><body>
            "You have add data successfully."
        </body></html>"""

@app.route('/customer_food')
def show_data():
    response = """
        <html><body>
            <h1>List of customers and their favorite food:</h1>"""
    
    response2 = """
        </body></html>"""
    
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()

    for x in myresult:
        template = x[1] + " " + x[2] + "<br>"
        response += template

    return response + response2

# Launch the Flask dev server
app.run(host="localhost", debug=True)