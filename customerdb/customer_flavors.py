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
    
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    print(myresult)

    is_duplicate = False

    for row in myresult:
        if row[1] == username and row[2] == favfood:
            is_duplicate = True

    if not is_duplicate:

        sql = "INSERT INTO customers (name, food) VALUES (%s, %s)"
        val = (username, favfood)
        mycursor.execute(sql, val)

        # make changes to the table 
        mydb.commit()

        return """
        <html><body>
            You have add data.
        </body></html>"""

    else:
        return """
        <html><body>
            The user already exists.
        </body></html>"""
    

@app.route('/customer_food')
def show_data():
    response = """
        <html><head>
        <style>
        table {
            width:100%;
        }
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 15px;
            text-align: left;
        }
        tr:nth-child(even) {
            background-color: #eee;
        }
        tr:nth-child(odd) {
            background-color: #fff;
        }
        th {
            background-color: black;
            color: white;
        }
        </style>
        </head></body>
            <h2>List of customers and their favorite food:</h2>
            <table>
            <tr>
                <th>Name</th>
                <th>Favorite food</th> 
            </tr>"""
    
    response2 = """
        </table></body></html>"""
    
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()

    for x in myresult:
        template = "<tr> <td>" + x[1] + "</td> <td>" + x[2] + "</td> </tr>"
        response += template

    return response + response2

# Launch the Flask dev server
app.run(host="localhost", debug=True)