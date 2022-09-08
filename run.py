import os, sys
import datetime
from pathlib import Path
from typing import List, Dict
from collections import namedtuple, OrderedDict
from dataclasses import dataclass

import cv2
import numpy as np
import random as r

from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, send, emit

from loguru import logger

r.seed(125)
logger.add(sys.stdout)  # TODO: configure loguru

app = Flask(__name__, static_folder='./static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def hello():
    # return render_template('index.html')
    logger.info('Send client index.html')
    with open('./index.html', mode='r') as f:
        s = f.readlines()
    html_string = ''.join(s)
    return html_string


# ================================================================
#                        File routing
# - models, js, css, sourcmaps, textures, etc.
# ================================================================
@app.route('/models/<path:path>', methods=['GET'])
def send_model(path):
    logger.info('Send model {}'.format(path))
    return send_from_directory('models', path)

@app.route('/js/<path:path>', methods=['GET'])
def send_js(path):
    logger.info('Send js {}'.format(path))
    return send_from_directory('js', path, mimetype='text/javascript')

@app.route('/sourcemaps/<path:path>', methods=['GET'])
def send_sourcemaps(path):
    logger.info('Send sourcemaps {}'.format(path))
    return send_from_directory('sourcemaps', path, mimetype='text/javascript')

@app.route('/css/<path:path>', methods=['GET'])
def send_css(path):
    logger.info('Send css {}'.format(path))
    return send_from_directory('css', path, mimetype='text/css')

@app.route('/textures/<path:path>', methods=['GET'])
def send_texture(path):
    logger.info('Send texture {}'.format(path))
    return send_from_directory('textures', path)

@app.route('/images/<path:path>', methods=['GET'])
def send_image(path):
    logger.info('Send image {}'.format(path))
    return send_from_directory('images', path)


# @app.route('/static/<path:path>', methods=['GET'])
# def send_static(path):
#     return send_from_directory('static', path)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5001, debug=False)
