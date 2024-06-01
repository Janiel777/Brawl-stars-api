from flask import Flask
from src.main import get_player_info

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

# @app.route('/player/<tag>')
# def player(tag):
#     player_info = get_player_info(tag)
#     if player_info:
#         return f"Player: {player_info['name']}, Trophies: {player_info['trophies']}"
#     else:
#         return "Player not found", 404

if __name__ == '__main__':
    app.run(debug=True)
