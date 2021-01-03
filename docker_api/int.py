from flask import Flask
from flask import request
import json
import send

app = Flask(__name__)


def load_config():
    with open('./configurations.json') as json_file:
        configs = json.load(json_file)
        key = configs['configurations']['key']
        host = configs['configurations']['host']
        return key, host


@app.route('/', methods=['POST'])
def main():
    data = request.get_json() or {}
    city = data['city']
    key = load_config()[0]
    host = load_config()[1]
    response = send.send(key, host, city)
    json_response = json.loads(response)

    # this can be used to custom construct json response
    # data = {}
    # data['key'] = 'value'
    # json_data = json.dumps(data)

    return json_response
    # ['city_name']