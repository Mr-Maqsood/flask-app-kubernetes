from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Too much fun learning Kubernetes,every day feels like unlocking a new superpower!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

