from flask import Flask, render_template, request, redirect, url_for

import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('Flask_Key')
@app.route('/' , methods=["GET"])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
