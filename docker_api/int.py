from flask import Flask, request
import json
import send2

app = Flask(__name__)


def load_config():
    with open('./configurations.json') as json_file:
        configs = json.load(json_file)
        key = configs['configurations']['key']
        host = configs['configurations']['host']
        print(f"{key}, {host}")
        return key, host


@app.route('/', methods=['GET'])   # POST GET PUT DELETE
def main():
    print("started")
    data = request.get_json() or {}
    city = data['city']
    print(city)
    key = load_config()[0]
    host = load_config()[1]
    response = send2.send(key, host, city)
    json_response = json.loads(response)

    # this can be used to custom construct json response
    # data = {}
    # data['key'] = 'value'
    # json_data = json.dumps(data)

    return json_response['city_name']

main()