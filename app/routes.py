from app import app

@app.route('/')
def index():
    return 'hi'


@app.route('/test')
def test():
    return 'test'