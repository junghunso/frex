from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://jungso:post9169@cluster0.kbds79b.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/fc_fnb_rank100", methods=["GET"])
def fc_fnb_rank100_get():
    fc_fnb_rank100_list = list(db.fc_fnb_rank100.find({}, {'_id': False}))
    return jsonify({'fc_fnb_rank100': fc_fnb_rank100_list})


@app.route("/fc_fnb_rank200", methods=["GET"])
def fc_fnb_rank200_get():
    fc_fnb_rank200_list = list(db.fc_fnb_rank200.find({}, {'_id': False}))
    return jsonify({'fc_fnb_rank200': fc_fnb_rank200_list})

@app.route("/fc_fnb_up_rank", methods=["GET"])
def fc_fnb_up_rank_get():
    fc_fnb_up_rank_list = list(db.fc_fnb_up_rank.find({}, {'_id': False}))
    return jsonify({'fc_fnb_up_rank': fc_fnb_up_rank_list})

@app.route("/fc_fnb_down_rank", methods=["GET"])
def fc_fnb_down_rank_get():
    fc_fnb_down_rank_list = list(db.fc_fnb_down_rank.find({}, {'_id': False}))
    return jsonify({'fc_fnb_down_rank': fc_fnb_down_rank_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
