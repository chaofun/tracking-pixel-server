from flask import Flask, request, send_file
from datetime import datetime
import os

app = Flask(__name__)

LOG_FILE = 'logs.txt'
PIXEL_PATH = os.path.join('static', 'pixel.png')

@app.route('/')
def index():
    return "✅ Tracking Pixel Server is running!"

@app.route('/track/pixel')
def track_pixel():
    # Log the request
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now().isoformat()} | IP:{request.remote_addr} | UA:{request.user_agent}\n")

    # Serve the actual 1x1 PNG
    return send_file(PIXEL_PATH, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
