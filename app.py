from flask import Flask
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)

xray_recorder.configure(service='MyApp')
XRayMiddleware(app, xray_recorder)

@app.route('/')
def hello():
    return "Hello X-Ray"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
