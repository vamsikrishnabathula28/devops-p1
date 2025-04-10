from flask import Flask, render_template
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    logger.info('Home page accessed')
    return render_template('index.html')

if __name__ == '__main__':
    logger.info('Starting Flask application...')
    app.run(host='0.0.0.0', port=8080, debug=True) 