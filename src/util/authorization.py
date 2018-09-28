from flask import request, make_response
from functools import wraps

# A sample username and password was applied because it was a case study. Authorized users can be stored in database.

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'userN' and auth.password == 'passW':
            return f(*args, **kwargs)
        return make_response("Could not verify", 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated
