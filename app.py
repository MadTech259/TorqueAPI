import json

from flask import Flask, request

import manager

app = Flask(__name__)

score_manager = manager.ScoreManager()




@app.route('/paperprotector/leaderboard', methods=['PUT'])
def insert_score():
    score = request.get_json()
    return score_manager.insert_score(score)


@app.route('/paperprotector/leaderboard', methods=['GET'])
def get_leaderboard():
    data = score_manager.get_leaderboard()
    leaderboard = json.dumps(data)
    return leaderboard


if __name__ == '__main__':
    app.run()


