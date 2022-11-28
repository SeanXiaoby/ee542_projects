import boto3
from flask import Flask, render_template
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
        mqtt.push_message("alarm!")
        speaker = True
    elif not alarm and speaker:
        mqtt.push_message("stop!")
        speaker = False


def read_db():
    response = client.scan(
        TableName='final',
    )
    markers = []
    record = False
    for item in response['Items']:
        m = dict()
        m["infobox"] = item['xdotId']['N']
        m['lat'] = item['lat']['N']
        m['lng'] = item['lng']['N']
        if item['moved']['BOOL']:
            m['icon'] = icons.dots.red
            record = True
        else:
            m['icon'] = icons.dots.blue
        markers.append(m)
    set_alarm(record)
    return markers

def read_db_time() :
    response = client.scan(
        TableName='final',
    )
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S, %Y-%m-%d")

    return current_time


@app.route("/")
def map_created_in_view():
    xdot_map = Map(
        identifier="xdot_map",
        varname="xdot_map",
        lat=34.022699,
        lng=-118.285034,
        markers=read_db(),
        style="height:400px;width:55%;margin:0;color:#242f3e;",
    )

    temp_markers = read_db()

    return render_template("web.html", xdot_map=xdot_map, key=api, timestamp = read_db_time(), lat = temp_markers[0]['lat'], lng = temp_markers[0]['lng'])


if __name__ == "__main__":
    app.run(port=5050, debug=True)
