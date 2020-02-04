from flask import Flask

app = Flask(__name__)

def greet():
    greeting = 'Hello World from BenchSci!'
    return greeting

@app.route('/hello')
def helloIndex():
    return greet()

app.run(host='0.0.0.0', port= 8080)
