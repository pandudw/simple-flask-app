from flask import Flask 

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Well done! You Successfully deployed your flask app, Now you can start building your app.'
    
    @app.route('/info')
    def info():
        return 'Author: Pandu'


    return app
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)