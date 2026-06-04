from flask import Flask, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/daily_number', methods=['GET'])
def get_daily_number():

    today = datetime.now().strftime("%Y-%m-%d")

    random.seed(today)

    response = random.randint(10000, 99999)

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=6000)