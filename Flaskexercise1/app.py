from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():


    number = request.form.get('number')
    
    response="No number provided!"

    if not str(number).isnumeric():
        response="Input is not an integer"
    else:
        iseven=(int(number)%2)==0
        if iseven:
            response="Number is even"
        else:
            response="Number is odd"

    print(number)
    return render_template('index.html', response=response)

if __name__ == "__main__":
    app.run(debug=True)