
export FLASK_APP=api.py 
flask run



# web_test_platfrom_back_from_api_py
web_test_platfrom_back_from_api_py


- begin from api.py

-  python3 api.py 

 * Serving Flask app "api" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 169-469-289
text1= 12
word= None
combine= 12
result2 is {'output': '12'}
result.items() is dict_items([('output', '12')])
jsonify(result=result) is :  <Response 41 bytes [200 OK]>
127.0.0.1 - - [13/Feb/2020 22:03:26] "POST /join HTTP/1.1" 200 -


# when from python -m SimpleHTTPServer 8080, or git.
that not start api.py. 

Just like as follow:

Directory listing for /
.git/
api.py
README.md
scripts/
templates/


# if you just call api.py, and same time use SimpleHTTPServer 8080.  it still not work. 
for you start two server:
1. http://127.0.0.1:5000/   --- back Web Server
2. http://localhost:8080/   ----Front Web Server ,same as www.gibhub.com/....../....