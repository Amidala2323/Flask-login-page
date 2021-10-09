from mysql.connector.errors import DatabaseError


try:

    from os import system
    from flask import Flask, app
    from flask import url_for
    from flask import request
    from flask import render_template
    from flask import redirect
    import mysql.connector as sql_database

except ImportError:

    #system("cls")
    print("Please Install requirments.txt file using pip >> pip install -r requirments.txt")
    pass        


app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def login_page():

    error = None

    if request.method == "POST":

        try:
        
            connection = sql_database.connect(host="localhost",
                                              user="root",
                                              database="mysite_database")

        except DatabaseError:

            print("Can't find a database /:")

    

    """
    if request.method == "POST":

        if request.form['username'] != "admin" or request.form['password'] != "admin":

            error = "username or password currect!! :)"
            
        elif request.form['username'] == "admin" or request.form['password'] == "admin":

            error = "you logined with {} account".format(request.form['username'])
                    
        return render_template('login_page.html', error=error)"""


if __name__ == "__main__":

    app.debug = True
    app.run(host="275.298.21.21")
