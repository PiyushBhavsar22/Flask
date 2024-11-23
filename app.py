from flask import Flask
'''
It will create an instance of the Flask class,
which will be your WSGI (Web Server Gatway Interface) application
'''

###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the flask"

@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__=="__main__":
    app.run(debug=True)