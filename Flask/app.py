from flask import Flask, render_template
from models.game import db, Game


app = Flask(__name__,static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def main():
    page_name = 'Главная страница'
    return render_template('main.html', title=page_name, page_name=page_name)


@app.route('/reviews/')
def reviews():
    games_list = Game.query.all()
    page_name = 'Обзоры игр'
    return render_template('reviews.html', games=games_list, title=page_name, page_name=page_name)


@app.route('/game_id/<int:game_id>')
def game_page(game_id):
    page_name = 'Обзор'
    game = Game.query.filter(Game.id == game_id)
    print(game_id)
    return render_template('game.html', game=game, page_name=page_name, title=page_name)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
