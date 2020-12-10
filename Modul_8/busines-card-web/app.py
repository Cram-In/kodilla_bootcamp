from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about_me.html', methods=['GET'])
def about_me():
    return render_template("about_me.html")

@app.route('/contact_me.html')
def contact_me():
    return render_template("contact_me.html")

@app.route('/index.html')
def menu():
    return render_template("index.html")
