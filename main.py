from flask import Flask,render_template
'''
It will create an instance of the Flask class,
which will be your WSGI (Web Server Gatway Interface) application
'''

###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)