from flask import Flask,make_response , request

app = Flask(__name__)

# This function is set_type_data cookie using key and value
@app.route('/set_type_data')
def setcookie():
    resp = make_response('setting cookie')
    resp.set_cookie('framework', 'flask')
    return resp

if __name__ == '__main__':
    app.run(debug =True )