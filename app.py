from flask import Flask

# entry point of the application
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Happy to learning Flask</h1>"

@app.route('/index', methods=['GET'])
def index():
    return "<h2>Welcome to Index Page</h2>"

# variable rules
@app.route('/sucess/<score>', methods=['GET'])
def sucess(score):
    return "<h2>The person has passed the exam with the score of </h2>" + score

# entry point denotes using the __
if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for hot reloading if we change the thing

    #Flask app url routing
