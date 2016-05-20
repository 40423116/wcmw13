from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<font color=#2200AA>Hello, World!"