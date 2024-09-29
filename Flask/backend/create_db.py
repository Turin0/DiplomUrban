from flask import Flask
from models.game import Game, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        game2 = Game(title='Dark souls', size=30.3, cost=2000, image='2', description='da', reviews='da')
        db.session.add_all([game2,])
        db.session.commit()
