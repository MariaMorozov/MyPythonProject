import json
import argparse
import send
from logs import logger


def load_key():
    with open('./configurations.json') as json_file:
        configs = json.load(json_file)
        key = (configs['configurations']['key'])
    # print(key)
    return key


def load_host():
    with open('./configurations.json') as json_file:
        configs = json.load(json_file)
        host = (configs['configurations']['host'])
    # print(host)
    return host


def main():
    parser = argparse.ArgumentParser(description='Weather in your city')
    parser.add_argument('-c', '--city', dest='city', help='city', default='Modiin')

    args = parser.parse_args()
    city = args.city
    #    print(city)
    logger.info("Parameters passed are " + str(args))
    my_response = send.send(load_key(), load_host(), city)

    print(my_response)


main()
# send.test()
