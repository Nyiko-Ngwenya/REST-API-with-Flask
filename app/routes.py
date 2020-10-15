from app import app
# https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"