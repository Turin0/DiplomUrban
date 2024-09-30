from flask import Flask, render_template, request
from models.game import db, Game, Post

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def main():
    page_name = 'Новости игр'
    posts = Post.query.all()
    return render_template('main.html', posts=posts, title=page_name, page_name=page_name)


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


@app.route('/post_add', methods=['GET', 'POST'])
def company_create_page():
    if request.method == 'GET':
        title = 'Добавление поста'
        page_name = title
        return render_template('post_add.html', title=title, page_name=page_name)
    elif request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        reviews_ = request.form.get('reviews')
        new_company = Post(
            title=title,
            description=description,
            reviews=reviews_
        )
        db.session.add(new_company)
        db.session.commit()
        return render_template('success.html')
    return


if __name__ == '__main__':
    app.run(port=8000, debug=True)
