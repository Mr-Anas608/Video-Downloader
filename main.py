from flask import Flask, render_template

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sample')
def sample():
    return render_template('sample.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
