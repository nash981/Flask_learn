import sys
import os
import glob
import re
import numpy as np
from flask import Markup

# Keras
from PIL import Image, ImageOps

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
filepath = '/home/nash/Pictures/WhatsApp Image 2020-10-26 at 02.33.54.jpeg'
url = 'http://127.0.0.1:5000/predict'
my_img = {'image': open(filepath, 'rb')}
r = request.post(url, files=my_img)

# convert server response into JSON format.
print(r.json())
