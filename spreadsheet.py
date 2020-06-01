from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    req_data = request.get_json(force = True)

    return ''

if __name__ == "__main__":
    app.run(debug=True)
