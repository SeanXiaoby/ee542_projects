import time

import boto3
from flask import Flask, render_template, jsonify
from flask_googlemaps import GoogleMaps, Map, icons
from dynaconf import FlaskDynaconf
from datetime import datetime
import json
from toMQTT import MQTT

# configure google map
api = 'AIzaSyCTyOx7jvfsWzqoKBHNuIQOijE6S-c3oW4'
app = Flask(__name__)
GoogleMaps(app, key=api)
FlaskDynaconf(app)

# connect to dynamodb
client = boto3.client('dynamodb')

# connect to MQTT
mqtt = MQTT()
speaker = False


def set_alarm(alarm):
    global speaker
    if alarm and not speaker:
        mqtt.push_message_mqtt("alert")
        speaker = True


def read_db():
    response = client.scan(
        TableName='final',
    )
    markers = []
    record = False
    for item in response['Items']:
        m = dict()
        m["xdotId"] = item['xdotId']['N']
        m['lat'] = item['lat']['N']
        m['lng'] = item['lng']['N']
        if item['moved']['BOOL']:
            record = True
        else:
            record = False
        m['moved'] = item['moved']['BOOL']
        now = datetime.now()
        m['timestamp'] = now.strftime("%H:%M:%S, %Y-%m-%d")
        markers.append(m)
        set_alarm(record)
    return markers


def read_db_time():
    response = client.scan(
        TableName='final',
    )
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S, %Y-%m-%d")

    return current_time

@app.route("/")
def map_created_in_view():

    return render_template("web.html", init_data=read_db())


@app.route("/update_markers", methods=['GET'])
def update_markers():
    return jsonify(result = read_db())


@app.route("/sound_alarm")
def sound_alarm():
    mqtt.push_message_mqtt("alert")
    print("Alarm sound!")
    return ("sound!")


@app.route("/stop_alarm")
def stop_alarm():
    global speaker
    mqtt.push_message_mqtt("stop")
    speaker = False
    print("Alarm stop!")
    return ("stop!")


if __name__ == "__main__":
    app.run(port=5050, debug=True)
