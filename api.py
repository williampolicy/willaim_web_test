from flask import Flask, request, render_template,jsonify
# ------ Creat a app as flask class ---------------
app = Flask(__name__)
# ------ define fuction ---------------

def do_something(text1,text2):
   text1 = text1.upper()
   text2 = text2.upper()
   combine = text1 + text2
   return combine
# ------ address ---------------
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome.php')
def welcome():
    return render_template('welcome.php')

# ------ /join? ---------------

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word =  request.args.get('text1')
    text2 = request.form['text2']
    #combine = do_something(text1,text2)
    combine = text1
    print('text1=',text1)
    print('word=',word)
    print('combine=',combine)    

    result = {
        "output": combine
    }

    result = {str(key): value for key, value in result.items()}
    print('result2 is',result)
    
    print('result.items() is',result.items())
    
    x = jsonify(result=result)
    print('jsonify(result=result) is : ',x)   

    return jsonify(result=result)


# ------ main ---------------

if __name__ == '__main__':
    app.run(debug=True)