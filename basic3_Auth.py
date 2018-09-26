from flask import Flask, jsonify, request, make_response
from functools import wraps

app = Flask(__name__)


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'userN' and auth.password == 'passW':
            return f(*args, **kwargs)
        return make_response("could not verify", 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated


@app.route('/', methods=['GET', 'POST'])
@auth_required
def index():
    if (request.method == 'POST'):
        data = request.get_json()
        return jsonify({'you sent': data})
    return 'welcome to page with auth.'


if __name__ == "__main__":
    app.run(debug=True)
