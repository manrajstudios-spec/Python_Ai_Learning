from flask import Flask,render_template

app = Flask(__name__,template_folder='templates')

@app.route('/')
def Hello():
    my_name= 'Manraj'
    my_result = 10 + 10
    my_list = [i for i in range(10) if i % 2 == 0]
    return render_template('index.html',name=my_name,result=my_result,my_list = my_list)

"""
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1,number2):
    return f'{number1} + {number2} = {number1 + number2}'

"""

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5555)