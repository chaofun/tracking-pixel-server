from flask import Flask, request, send_file
import datetime
import os

app = Flask(__name__)

LOGFILE = "logs.txt"

@app.route('/track/pixel')
def track_pixel():
    email_id = request.args.get('id', 'unknown')
    user_agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    timestamp = datetime.datetime.now()

    with open(LOGFILE, 'a') as f:
        f.write(f"{timestamp}\tID:{email_id}\tIP:{ip}\tUA:{user_agent}\n")

    return send_file(os.path.join('static', 'pixel.png'), mimetype='image/png')

@app.route('/')
def home():
    return "Tracking Pixel Server is running!"

if __name__ == "__main__":
    app.run()
