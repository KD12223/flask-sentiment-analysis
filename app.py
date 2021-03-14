import boto3 as boto3
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')


# Determines the sentiment of text and returns the results
@app.route('/analyze', methods=['POST'])
def analyze_text():
    body = request.get_json()
    text = body.get('content')

    if text:
        return jsonify(comprehend.detect_sentiment(Text=text, LanguageCode='en'))
    else:
        raise BadRequest('The content is missing from the request')


# Handles all exceptions
@app.errorhandler(Exception)
def exception_handler(e):
    return jsonify(e.description), e.code


if __name__ == '__main__':
    app.run()
