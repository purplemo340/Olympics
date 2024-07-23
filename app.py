from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
#from visual import game_info
games_info=pd.read_csv('results/games.csv')
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('Flask_Key')
@app.route('/' , methods=["POST", "GET"])
def home():

    if request.method=="POST":
        game=request.form['Cities']
        print(game)
        return redirect(url_for('game', city=game))
    return render_template("index.html", games=games_info['City-Year'])

@app.route('/game/<city>' , methods=["POST", "GET"])
def game(city):
    return render_template('game.html', city=city)
if __name__ == "__main__":
    app.run(debug=True)
