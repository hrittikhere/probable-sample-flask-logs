from flask import Flask
from flask import json

# Create a Flask application
app = Flask(__name__)

# Status Endpoint - GET with Logs
@app.route('/status', methods=['GET'])
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Status request successful')
    return response

# Primary Endpoint - GET with Logs
@app.route("/", methods=['GET'])
def hello():
    app.logger.info('Main request successful')
    return "Hello World!"


# Start the Flask app
if __name__ == "__main__":
    app.run(debug='True', host='0.0.0.0', port=9000)
