from flask import Flask,render_template, request, redirect, url_for, jsonify

# entry point of the application
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Happy to learning Flask</h1>"

@app.route('/index', methods=['GET'])
def index():
    return "<h2>Welcome to Index Page</h2>"

# variable rules
@app.route('/sucess/<int:score>', methods=['GET'])
def sucess(score):
    return "The person has passed the exam with the score of " + str(score)

@app.route('/failure/<int:score>', methods=['GET'])
def failure(score):
    return "The person has failed the exam with the score of " + str(score)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        # for the render template we need to have the form.html in the templates folder
        return render_template('form.html')
    else:
        maths = int(request.form['maths'])
        chemistry = int(request.form['chemistry'])
        physics = int(request.form['physics'])

        avg_marks = (maths + chemistry + physics)/3

        result = ""

        if avg_marks > 50:
            result = "sucess"
        else:
            result ="failure"     
        return redirect(url_for(result, score=avg_marks))      
       # return render_template('form.html', Score=avg_marks)  
    
@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify({'result': a_val+b_val})

# entry point denotes using the __
if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for hot reloading if we change the thing

    #Flask app url routing
