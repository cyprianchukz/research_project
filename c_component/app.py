from flask import Flask, jsonify
import requests
from ctypes import CDLL

app = Flask(__name__)

lib = CDLL('./libcollate.so')

@app.route('/collate-data', methods=['GET'])
def collate_data():
    lib.process_data()
    source1 = requests.get('https://api.mock1.com/data').json()
    source2 = requests.get('https://api.mock2.com/data').json()

    collated_data = {
        "source1": source1,
        "source2": source2
    }
    return jsonify(collated_data)

if __name__ == '__main__':
    app.run(debug=True)
