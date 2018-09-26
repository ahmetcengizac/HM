from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        data = request.get_json("")

        return jsonify({'you sent': data})
    else:
        return jsonify({"about": "hello"})


@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num * 10})


if __name__ == "__main__":
    app.run(debug=True)

## curl command :
## curl -X POST -H "Content-Type: Application/json" -d "{ \"Ahmet\" : \"10.10.1977\" }" http://127.0.0.1:5000/
