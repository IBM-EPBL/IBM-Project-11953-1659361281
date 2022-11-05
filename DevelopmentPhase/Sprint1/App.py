from flask import Flask,render_template

app = Flask(_name_)

@app.route("/")

def login():
    return render_template('login.html')
